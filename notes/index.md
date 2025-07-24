---
layout: default
title: My Notes
---

# My Notes

Welcome to my notes collection! Click any note to read.

{% assign folders = "Computer Networks and Communication,Git,Java,Full-Stack Development,Google Cybersecurity" | split: "," %}

{% for folder in folders %}
  <h2>{{ folder }}</h2>
  {% assign subdirs = site.pages | map: 'dir' | uniq | sort %}
  {% assign folder_subdirs = subdirs | where_exp: 'd', 'd contains "notes/' | append: folder | append: '/"' %}
  {% assign folder_pages = site.pages | where_exp: 'p', 'p.dir == "notes/' | append: folder | append: '/"' %}
  {% if folder_pages.size > 0 %}
    <ul>
      {% for page in folder_pages %}
        {% if page.path contains '.md' and page.url != '/notes/' %}
          <li><a href="{{ page.url | relative_url }}">{{ page.title | default: page.name | replace: '.md', '' }}</a></li>
        {% endif %}
      {% endfor %}
    </ul>
  {% endif %}
  {% for subdir in folder_subdirs %}
    {% assign subdir_name = subdir | split: '/' | last %}
    <h3 style="margin-left:1em;">{{ subdir_name }}</h3>
    <ul>
      {% for page in site.pages %}
        {% if page.dir == subdir and page.path contains '.md' and page.url != '/notes/' %}
          <li style="margin-left:1em;"><a href="{{ page.url | relative_url }}">{{ page.title | default: page.name | replace: '.md', '' }}</a></li>
        {% endif %}
      {% endfor %}
    </ul>
  {% endfor %}
{% endfor %} 