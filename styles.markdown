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
{%- for beer in style.items %}
   - [{{ beer.title }}]({{ beer.url | relative_url }}) _- {{ beer.date | date: site.minima.date_format }}_
{%- endfor %} 
{%- endfor %}
