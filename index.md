---
title: Latest Notes
description: Short notes on product, learnings, and ideas worth keeping.
---

## What this is
short notes, lessons learnt, tools explored, and occasional longer thoughts on product, technology, building things, and just life in general (yes, that includes poetry)

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
