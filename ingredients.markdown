---
layout: page
title: Ingredients
permalink: /ingredients/
---

{% comment %}

{% assign grains = site.posts | grain_weights %}
{% assign hops = site.posts | boil_ingr_weights %}

{% assign grain_total = 0 %}
{% assign hops_total = 0 %}
{% for grain in grains %}
	{% assign grain_total = grain_total | plus: grain[1] %}
{% endfor %}
{% for hop in hops %}
	{% assign hops_total = hops_total | plus: hop[1] %}
{% endfor %}

Here're some of the ingredients I've brewed with over the years...

## Mash Ingredients / Grain: {{ grain_total | format_weight }} total
{% for grain in grains %}
 - {{ grain[0] }}: {{ grain[1] | format_weight -}}
{% endfor %}

## Boil Ingredients / Hops: {{ hops_total | format_weight }} total
{% for hop in hops %}
{%- if hop[1]>0 -%}
 - {{ hop[0] }}: {{ hop[1] | format_weight }}
{% endif -%}
{% endfor %}

{% endcomment %}