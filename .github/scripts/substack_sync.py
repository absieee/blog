"""Send newly published posts to Substack as drafts, and notes as Substack Notes.

Sent files are recorded in .substack-sent.json so each one goes out once.
  --seed     mark every current published file as sent, without sending anything
  --dry-run  list what would be sent

Needs SUBSTACK_COOKIES (browser cookie string) and SUBSTACK_PUBLICATION_URL.
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".substack-sent.json"
SITE = "https://absieee.github.io/blog"
FOLDERS = ("_posts", "_notes")


def read(path):
    text = path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return {}, text
    return yaml.safe_load(m.group(1)) or {}, m.group(2)


def pending(sent):
    for folder in FOLDERS:
        for path in sorted((ROOT / folder).glob("*.md")):
            rel = path.relative_to(ROOT).as_posix()
            if rel in sent:
                continue
            fm, body = read(path)
            if fm.get("published", True) is False:
                continue
            yield rel, fm, body


def slug(rel):
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", Path(rel).stem)


def blog_url(rel, fm):
    if rel.startswith("_notes/"):
        return f"{SITE}/notes/{slug(rel)}/"
    cats = fm.get("categories") or []
    if isinstance(cats, str):
        cats = cats.split()
    return "/".join([SITE, *cats, slug(rel)]) + "/"


def clean(body):
    # Old posts use Jekyll image paths; the library uploads local files by vault path.
    return body.replace("{{ site.baseurl }}/assets/", "assets/").strip()


def send_post(api, rel, fm, body):
    markdown = clean(body) + f"\n\n---\n\n*Originally published on [my blog]({blog_url(rel, fm)}).*"
    result = api.create_draft_from_markdown(
        title=fm.get("title") or slug(rel),
        subtitle=fm.get("summary") or "",
        markdown=markdown,
    )
    return f"draft {result['draft']['id']}"


def send_note(api, body):
    from substack.mdrender import markdown_to_doc

    # Notes are text-only for now: drop image lines rather than fail the upload.
    text = re.sub(r"^\s*!\[[^\]]*\]\([^)]*\)\s*$", "", clean(body), flags=re.M)
    doc = {"type": "doc", "attrs": {"schemaVersion": "v1"}, "content": markdown_to_doc(text, api=api)}
    response = api._session.post(
        "https://substack.com/api/v1/comment/feed",
        json={"bodyJson": doc, "tabId": "for-you", "surface": "feed", "replyMinimumRole": "everyone"},
    )
    response.raise_for_status()
    return f"note {response.json().get('id')}"


def save(sent):
    STATE.write_text(json.dumps(sent, indent=2, sort_keys=True) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    sent = json.loads(STATE.read_text()) if STATE.exists() else {}
    todo = list(pending(sent))

    if args.seed:
        for rel, _, _ in todo:
            sent[rel] = "seeded"
        save(sent)
        print(f"seeded {len(todo)} files")
        return
    if not todo:
        print("nothing new to send")
        return
    if args.dry_run:
        for rel, fm, _ in todo:
            print(f"would send {rel} -> {blog_url(rel, fm)}")
        return
    if not os.environ.get("SUBSTACK_COOKIES"):
        print("SUBSTACK_COOKIES not set; skipping")
        return

    from substack import Api

    api = Api(
        cookies_string=os.environ["SUBSTACK_COOKIES"],
        publication_url=os.environ.get("SUBSTACK_PUBLICATION_URL") or None,
    )
    failed = False
    for rel, fm, body in todo:
        try:
            sent[rel] = send_note(api, body) if rel.startswith("_notes/") else send_post(api, rel, fm, body)
            print(f"sent {rel}: {sent[rel]}")
        except Exception as e:
            failed = True
            print(f"failed {rel}: {e}", file=sys.stderr)
        save(sent)  # after each send, so a later crash can't cause a duplicate
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
