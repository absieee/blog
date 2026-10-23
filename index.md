---
title: Latest Notes
description: Short notes on product, learnings, and ideas worth keeping.
---

short notes, lessons learnt, tools explored, and occasional longer thoughts on product, technology, building things, and just life in general (yes, that includes poetry)

{% assign latest_posts = site.posts | concat: site.notes | sort: 'date' | reverse %}
{% for post in latest_posts %}
<article class="post-card">
  <p class="post-meta">{{ post.date | date: "%-d %B %Y" }}{% if post.categories and post.categories.size > 0 %} · {% for c in post.categories %}<a href="{{ '/category/' | append: c | append: '/' | relative_url }}">{{ c }}</a>{% unless forloop.last %} / {% endunless %}{% endfor %}{% endif %}</p>
  {% if post.categories contains 'notes' %}
  <div class="note-body">{% include body.html html=post.content %}</div>
  <p><a href="{{ post.url | relative_url }}">link</a></p>
  {% else %}
  <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
  {% if post.summary %}
  <p>{{ post.summary }}</p>
  {% endif %}
  {% endif %}
</article>
{% endfor %}
