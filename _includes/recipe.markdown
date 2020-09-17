# Recipe: {% if page.recipe.name %}{{ page.recipe.name }}{% else %}{{ page.title }}{% endif %}
{% if page.recipe.style %}_{{ page.recipe.style %}}_{% endif %}  

| **Type** | {{ page.recipe.type }} | **Batch Size** | {{ page.recipe.size }}
| **Boil Time** | {{ page.recipe.boil_time }} | **Est. Efficiency** | {{ page.recipe.efficiency }}
| **Est. Original Gravity** | {{ page.recipe.est_og }} | **Est. Final Gravity** | {{ page.recipe.est_fg }}
| **Est. Color** | {{ page.recipe.color }} | **Est. IBU** | {{ page.recipe.ibus }}
| **Est. ABV** | {{ page.recipe.est_abv }} 

## Fermentables

|---
| Name | Amount | %
|-|-|-
{% for fermentable in page.recipe.fermentables -%}
| {{fermentable.name}} | {{fermentable.amount}} | {{fermentable.perc}}
{% endfor -%}
|---

## Mash

|---
| Step | Strike Temp | Amount | Target Temp | Time
|-|-|-
{% for step in page.recipe.mash -%}
| {{ step.name }} | {{ step.strike_temp }} | {{ step.amount }} | {{ step.target_temp }} | {{ step.time }}
{% endfor -%}
|---

{% if page.recipe.sparge %}
## Sparge
{{ page.recipe.sparge }}
{% endif %}

## Hops/Boil

|---
| Name | AA% | Amount | Type | Time | IBUs/%
|-|-|-|-|-|-
{% for hops in page.recipe.hops -%}
| {{ hops.name }} | {% if hops.aa %}{{hops.aa}}{%else%}-{%endif%} | {{ hops.amount }} | {{ hops.type }} | {{ hops.time}} | {% if hops.ibu %}{{ hops.ibu }}{% else %}{%if hops.perc%}{{hops.perc}}{%else%}-{%endif%}{%endif%}
{% endfor -%}
|---

## Fermentation
**Yeast:** {{ page.recipe.yeast }}  
**Fermentation:** {{ page.recipe.ferm_time }} @ {{ page.recipe.ferm_temp }}

## Packaging
**Packaging Type:** {{ page.recipe.package_type }}  
**Packaged on:** {{ page.recipe.package_date }}  
**Carbonation:** {{ page.recipe.carb_priming }}

## Final Result
**Original Gravity:** {{ page.recipe.og }}  
**Final Gravity:** {{ page.recipe.fg }}  
**ABV:** {{ page.recipe.abv }}


## Notes
{{ page.recipe.notes }}
