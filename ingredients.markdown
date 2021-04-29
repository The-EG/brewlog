---
layout: page
title: Ingredients
permalink: /ingredients/
---

Here're some of the ingredients I've brewed with over the years...

## Mash Ingredients / Grain
{% for fermentable in site.data.ingredients.fermentables %}
 - {{ fermentable.name }}: {{ fermentable.amount_str -}}
{% endfor %}

## Boil Ingredients / Hops
{% for hops in site.data.ingredients.hops %}
{%- if hops.amount>0 -%}
 - {{ hops.name }}: {{ hops.amount_str }}
{% endif -%}
{% endfor %}
