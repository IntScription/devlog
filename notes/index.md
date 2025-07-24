---
layout: default
title: My Notes
---

# My Notes

Welcome to my notes collection! Click any note to read.

{% assign folders = "Computer Networks and Communication,Git,Java,Full-Stack Development,Google Cybersecurity" | split: "," %}

{% for folder in folders %}
  <h2>{{ folder }}</h2>
  <ul>
    {% for page in site.pages %}
      {% if page.path contains 'notes/' and page.path contains folder and page.path contains '.md' and page.url != '/notes/' and page.dir contains folder %}
        <li><a href="{{ page.url | relative_url }}">{{ page.title | default: page.name | replace: '.md', '' }}</a></li>
      {% endif %}
    {% endfor %}
  </ul>
{% endfor %} 