---
name: new-blog-post
description: Use when starting a new post on the personal Jekyll blog at ~/Desktop/CODE/personal/blog. Creates the post file with correct frontmatter and a category stub if the category is new.
---

# new-blog-post

Scaffolds a new post for the Jekyll blog at `~/Desktop/CODE/personal/blog`.

## What to ask the user (if not supplied in args)

1. **Slug** — the URL-safe filename portion (e.g. `my-new-post`)
2. **Title** — display title (lowercase, the blog's style)
3. **Categories** — one or more from the existing set: `til`, `product`, `tech`, `personal` — or a new one
4. **Summary** — one-sentence description shown on the homepage

If the user types `/new-blog-post my post title`, treat it as the title and derive the slug from it.

## Post file

Filename pattern: `_posts/YYYY-MM-DD-<slug>.md` using today's date.

Before creating the file, run this to get the correct timestamp and UTC offset:

```bash
date '+%Y-%m-%d %H:%M:%S %z'
```

Use the output verbatim in the `date` field:

```yaml
---
title: <title>
date: 2026-06-04 14:32:00 +0100
categories: [<cat1>, <cat2>]
summary: <one-sentence summary>
---
```

Leave a blank line after the closing `---` so the user can start writing immediately.

## Category stubs

Existing stubs: `til`, `product`, `tech`, `personal` (files in `category/`).

If any requested category doesn't have a stub yet, create `category/<name>.md`:

```yaml
---
layout: category
category: <name>
permalink: /category/<name>/
---
```

Warn the user if you created a new stub so they know to commit it alongside the post.

## After creating the file

Tell the user the file path so they can open it directly. Nothing else needed — they'll do the writing.
