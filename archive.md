---
layout: default
title: Devlog Archive 📚
permalink: /archive/
---

# 📚 Devlog Archive

All my devlog entries, organized by month.

---

{% assign logs = site.pages | where_exp:"p","p.url contains '/logs/'" | sort: "url" | reverse %}
{% assign current_year = "" %}
{% assign current_month = "" %}

{% for p in logs %}
  {% assign parts = p.url | split:'/' %}
  {% assign date_str = parts[2] %}
  {% assign year = date_str | slice:0,4 %}
  {% assign month = date_str | slice:0,7 %}

  {%- if year != current_year -%}
    {%- if current_year != "" -%}
      {%- if current_month != "" -%}</ul></div>{%- endif -%}
    </details>
    {%- endif -%}
    <details class="archive-year">
      <summary>{{ year }}</summary>
    {%- assign current_year = year -%}
    {%- assign current_month = "" -%}
  {%- endif -%}

  {%- if month != current_month -%}
    {%- if current_month != "" -%}</ul></div>{%- endif -%}
    <div class="archive-month">
      <h3>{{ month }}</h3>
      <ul>
    {%- assign current_month = month -%}
  {%- endif -%}

  <li><a href="{{ p.url | relative_url }}">{{ date_str }} — {{ p.title | default: "Devlog" }}</a></li>
{% endfor %}

{% if current_month != "" %}</ul></div>{% endif %}
{% if current_year != "" %}</details>{% endif %}
