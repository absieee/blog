# Working with Claude on this blog

## Authorship

This blog is written by me. I use Claude to move faster — drafting, editing, scaffolding — but the voice and the published words are mine.

## Commit messages

- Do not add `Co-Authored-By: Claude ...` trailers.
- Do not add "Generated with Claude Code" or any AI-attribution lines.
- Write commits as if I authored them.

## Posts

- Posts live in `_posts/` with the filename pattern `YYYY-MM-DD-slug.md`.
- Images live in `assets/images/YYYY-MM-DD-slug/` and are referenced with `{{ site.baseurl }}/assets/images/...`.
- Spellcheck runs in CI via `.github/workflows/typos.yml` and locally via `.git/hooks/pre-commit`.

## Categories

- Categories on posts and the homepage link to `/category/<name>/` landing pages.
- Landing pages are stub files in `category/` (e.g. `category/til.md`) that use the `category` layout.
- **When introducing a new category in a post's frontmatter, also add a matching stub** or the link will 404. Stub template:

  ```yaml
  ---
  layout: category
  category: <name>
  permalink: /category/<name>/
  ---
  ```
