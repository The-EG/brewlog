---
layout: page
title: By Name
permalink: /ByName/
---
Brews grouped by name!
{% assign brew_names = site.posts | group_by_exp: "item", "item.title" | sort: "name" %}
{% for recipe in brew_names %}
 - {{ recipe.name }}
 {% for brew in recipe.items %}
   {%-if forloop.first <> true %} | {% endif -%}
   [{{ brew.date | date: site.minima.date_format }}]({{brew.url | relative_url}})
 {%- endfor %}
{%- endfor %}
