---
layout: default
title: Devlog Archive 📚
permalink: /archive/
---

# 📚 Devlog Archive

All my devlog entries, organized by year and month.

<div class="archive-controls">
  <button id="expand-all" class="archive-btn" aria-label="Expand all years">Expand All</button>
  <button id="collapse-all" class="archive-btn" aria-label="Collapse all years">Collapse All</button>
  <input type="text" id="archive-search" class="archive-search" placeholder="Search entries..." aria-label="Search archive entries">
</div>

---

{% assign logs = site.pages | where_exp:"p","p.url contains '/logs/'" | sort: "url" | reverse %}

{% comment %} First pass: count entries per year and month {% endcomment %}
{% assign year_counts = "" | split: "," %}
{% assign month_counts = "" | split: "," %}
{% for p in logs %}
  {% assign parts = p.url | split:'/' %}
  {% assign date_str = parts[2] %}
  {% assign year = date_str | slice:0,4 %}
  {% assign month = date_str | slice:0,7 %}
  {% assign year_counts = year_counts | push: year %}
  {% assign month_counts = month_counts | push: month %}
{% endfor %}

{% assign current_year = "" %}
{% assign current_month = "" %}
{% assign year_count = 0 %}
{% assign month_count = 0 %}

<div id="archive-container">
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
    
    {% comment %} Count entries for this year {% endcomment %}
    {% assign year_count = 0 %}
    {% for y in year_counts %}
      {% if y == year %}
        {% assign year_count = year_count | plus: 1 %}
      {% endif %}
    {% endfor %}
    
    <details class="archive-year" data-year="{{ year }}">
      <summary aria-expanded="false">
        <span class="year-label">{{ year }}</span>
        <span class="year-count">({{ year_count }})</span>
      </summary>
    {%- assign current_year = year -%}
    {%- assign current_month = "" -%}
    {%- assign month_count = 0 -%}
  {%- endif -%}

  {%- if month != current_month -%}
    {%- if current_month != "" -%}</ul></div>{%- endif -%}
    
    {% comment %} Count entries for this month {% endcomment %}
    {% assign month_count = 0 %}
    {% for m in month_counts %}
      {% if m == month %}
        {% assign month_count = month_count | plus: 1 %}
      {% endif %}
    {% endfor %}
    
    <div class="archive-month" data-month="{{ month }}">
      <h2 class="archive-month-heading">{{ month }} <span class="month-count">({{ month_count }})</span></h2>
      <ul>
    {%- assign current_month = month -%}
  {%- endif -%}

  {% assign excerpt = p.content | strip_html | strip_newlines | truncatewords: 15 %}
  <li class="archive-entry" data-date="{{ date_str }}" data-title="{{ p.title | default: 'Devlog' | downcase }}">
    <a href="{{ p.url | relative_url }}" class="archive-link" data-excerpt="{{ excerpt | escape }}">
      <span class="archive-date">{{ date_str }}</span>
      <span class="archive-title"> — {{ p.title | default: "Devlog" }}</span>
    </a>
  </li>
{% endfor %}

{% if current_month != "" %}</ul></div>{% endif %}
{% if current_year != "" %}</details>{% endif %}
</div>

<script src="{{ '/assets/js/archive.js' | relative_url }}"></script>