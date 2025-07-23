---
layout: default
title: My Notes
---

# My Notes

Welcome to my notes collection! Click any note to read.

<ul>
  {% assign notes = site.static_files | where_exp: "item", "item.path contains 'notes/' and item.extname == '.md'" %}
  {% for note in notes %}
    <li><a href="{{ note.path | relative_url }}">{{ note.name | replace: '.md', '' }}</a></li>
  {% endfor %}
</ul> 