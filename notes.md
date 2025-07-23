---
layout: default
title: My Notes
---

# My Notes

Welcome to my notes collection! Click any note to read.

<ul>
  {% for page in site.pages %}
    {% if page.path contains 'notes/' and page.path contains '.md' and page.url != '/notes/' %}
      <li><a href="{{ page.url | relative_url }}">{{ page.title | default: page.name | replace: '.md', '' }}</a></li>
    {% endif %}
  {% endfor %}
</ul>
