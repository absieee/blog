<%*
const title = (await tp.system.prompt("Post title")) || "untitled";
const slug = title.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
await tp.file.rename(tp.date.now("YYYY-MM-DD") + "-" + slug);
-%>
---
title: <% title %>
date: <% tp.date.now("YYYY-MM-DD HH:mm:ss ZZ") %>
categories: []
summary: 
published: false
---

