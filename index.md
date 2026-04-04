---
title: Latest Notes
description: Short notes on product, systems, and ideas worth keeping.
---

## What this is

This is my TIL-style blog: short notes, lessons learned, and occasional longer thoughts on product, technology, and building things.

## Start here

{% assign latest_posts = site.posts %}
{% for post in latest_posts %}
<article class="post-card">
  <p class="post-meta">{{ post.date | date: "%-d %B %Y" }}{% if post.categories and post.categories.size > 0 %} · {{ post.categories | join: " / " }}{% endif %}</p>
  <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
  {% if post.summary %}
  <p>{{ post.summary }}</p>
  {% endif %}
</article>
{% endfor %}
