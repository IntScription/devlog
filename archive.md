---
layout: default
title: Devlog Archive 📚
permalink: /archive/
---

# 📚 Devlog Archive

All my devlog entries, organized by month.

---

{% assign logs = site.pages | where_exp:"p","p.url contains '/logs/'" | sort: "url" | reverse %}
{% assign current_month = "" %}
{% for p in logs %}
  {% assign parts = p.url | split:'/' %}
  {% assign date_str = parts[2] %}
  {% assign month = date_str | slice:0,7 %}
  {% if month != current_month %}
    {% if current_month != "" %}</ul>{% endif %}
    <h3>{{ month }}</h3>
    <ul>
    {% assign current_month = month %}
  {% endif %}
  <li><a href="{{ p.url | relative_url }}">{{ date_str }} — {{ p.title | default: "Devlog" }}</a></li>
{% endfor %}
{% if current_month != "" %}</ul>{% endif %}

