# blog

This repository contains a lightweight Jekyll blog designed to publish on GitHub Pages.

## Expected URL

Because this repository should be named `blog`, the site will publish at:

`https://absieee.github.io/blog/`

If the repository is still named something else on GitHub, rename it in the repository settings so the URL and `_config.yml` stay aligned.

## How to write a new post

1. Create a new Markdown file in `_posts/`
2. Name it like `YYYY-MM-DD-title-goes-here.md`
3. Add front matter at the top:

```md
---
title: My new note
date: 2026-04-04 18:30:00 +0100
categories: [product]
summary: One-line summary for the homepage.
---
```

4. Write the post in Markdown below that block
5. Commit and push to `main`

## Good categories to start with

- `product`
- `engineering`
- `notes`

## Local preview

If you want to run the site locally later:

1. Install Ruby and Bundler
2. Run `bundle install`
3. Run `bundle exec jekyll serve`

## Deployment

This repo includes a GitHub Actions workflow that builds and deploys the site to GitHub Pages on every push to `main`.
