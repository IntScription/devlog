---
layout: default
title: My Notes
---

# My Notes

Welcome to my notes collection! Click any note to read.

<h2>Computer Networks and Communication</h2>
<ul>
  {% for page in site.pages %}
    {% if page.path contains 'notes/Computer Networks and Communication/' and page.path contains '.md' and page.url != '/notes/' %}
      <li><a href="{{ page.url | relative_url }}">{{ page.title | default: page.name | replace: '.md', '' }}</a></li>
    {% endif %}
  {% endfor %}
</ul>

<h2>Git</h2>
<ul>
  {% for page in site.pages %}
    {% if page.path contains 'notes/Git/' and page.path contains '.md' and page.url != '/notes/' %}
      <li><a href="{{ page.url | relative_url }}">{{ page.title | default: page.name | replace: '.md', '' }}</a></li>
    {% endif %}
  {% endfor %}
</ul>

<h2>Java</h2>
<ul>
  {% for page in site.pages %}
    {% if page.path contains 'notes/Java/' and page.path contains '.md' and page.url != '/notes/' %}
      <li><a href="{{ page.url | relative_url }}">{{ page.title | default: page.name | replace: '.md', '' }}</a></li>
    {% endif %}
  {% endfor %}
</ul>

<h2>Full-Stack Development</h2>
<ul>
  {% for page in site.pages %}
    {% if page.path contains 'notes/Full-Stack Development/' and page.path contains '.md' and page.url != '/notes/' %}
      <li><a href="{{ page.url | relative_url }}">{{ page.title | default: page.name | replace: '.md', '' }}</a></li>
    {% endif %}
  {% endfor %}
</ul>

<h2>Google Cybersecurity</h2>
<ul>
  {% for page in site.pages %}
    {% if page.path contains 'notes/Google Cybersecurity/' and page.path contains '.md' and page.url != '/notes/' %}
      <li><a href="{{ page.url | relative_url }}">{{ page.title | default: page.name | replace: '.md', '' }}</a></li>
    {% endif %}
  {% endfor %}
</ul> 