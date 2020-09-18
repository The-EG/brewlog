---
layout: page
title: Styles
permalink: /styles/
---
Here are the styles I've brewed so far...
## Beer
{% assign beer_styles = site.posts | where_exp: "item", "item.brew_type == 'beer'" | group_by_exp: "item", "item.recipe.style" %}
{% for style in beer_styles %}
 - {{ style.name }}
{%- assign beer_names = style.items | group_by_exp: "item", "item.title" -%}
{%- for name in beer_names %}
   - {{ name.name }}
{%- for beer in name.items -%}
     {%if forloop.first <> true %} | {% endif %}
     [{{ beer.date | date: site.minima.date_format }}]({{ beer.url | relative_url }})
{%- endfor %}
{%- endfor %} 
{%- endfor %}
