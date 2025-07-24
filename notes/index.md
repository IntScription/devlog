---
layout: default
title: My Notes
---

# My Notes

Welcome to my notes collection! Click any note to read.

<h2>Computer Networks and Communication</h2>
<ul>
  <li><a href="{{ '/notes/Computer Networks and Communication/CNC Outline' | relative_url }}">CNC Outline (Index)</a></li>
  {% for page in site.pages %}
    {% if page.path contains 'notes/Computer Networks and Communication/' and page.path contains '.md' and page.url != '/notes/' and page.name != 'CNC Outline.md' %}
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
  <li><a href="{{ '/notes/Java/My Java Collection' | relative_url }}">My Java Collection (Index)</a></li>
  {% for page in site.pages %}
    {% if page.path contains 'notes/Java/' and page.path contains '.md' and page.url != '/notes/' and page.name != 'My Java Collection.md' %}
      <li><a href="{{ page.url | relative_url }}">{{ page.title | default: page.name | replace: '.md', '' }}</a></li>
    {% endif %}
  {% endfor %}
</ul>

<h2>Full-Stack Development</h2>
<ul>
  <li><a href="{{ '/notes/Full-Stack Development/Index/Full Stack' | relative_url }}">Full Stack (Index)</a></li>
  {% for page in site.pages %}
    {% if page.path contains 'notes/Full-Stack Development/' and page.path contains '.md' and page.url != '/notes/' and page.name != 'Full Stack.md' %}
      <li><a href="{{ page.url | relative_url }}">{{ page.title | default: page.name | replace: '.md', '' }}</a></li>
    {% endif %}
  {% endfor %}
</ul>

<h2>Google Cybersecurity</h2>
<ul>
  <li><a href="{{ '/notes/Google Cybersecurity/Index/Google Cybersecurity' | relative_url }}">Google Cybersecurity (Index)</a></li>
  {% for page in site.pages %}
    {% if page.path contains 'notes/Google Cybersecurity/' and page.path contains '.md' and page.url != '/notes/' and page.name != 'Google Cybersecurity.md' %}
      <li><a href="{{ page.url | relative_url }}">{{ page.title | default: page.name | replace: '.md', '' }}</a></li>
    {% endif %}
  {% endfor %}
</ul> 