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
