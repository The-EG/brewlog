---
layout: post
title: "Weihenstephaner Clone"
date: 2018-03-04
tags:
  - clone
  - weissbier
brew_type: beer

recipe:
  type: "All Grain"
  style: "Weissbier"
  size: "3 gallon"
  efficiency: 72%
  est_og: 1.053
  est_fg: 1.013
  est_abv: 5.2
  color: 3.8
  ibus: 13.8
  boil_time: "60 min"
  yeast: "WY3068"
  ferm_time: "10 days"
  ferm_temp: 72F
  fermentables:
    - name: "Wheat (German)"
      amount: "3 lbs 12 oz"
      perc: 62.5%
    - name: "Pilsner (German)"
      amount: "2 lbs"
      perc: 33.3%
    - name: "Rice Hulls"
      amount: "4 oz"
      perc: 4.2%
  mash:
    - name: "Mash In"
      strike_temp: "164F"
      amount: "8 qt"
      target_temp: "153F"
      time: "60 min"
    - name: "Mash Out"
      strike_temp: "210F"
      amount: "3.25 qt"
      target_temp: "168F"
      time: "10 min"
  sparge: fly sparge
  hops:
    - name: "Hallertau"
      type: "Boil"
      aa: 2.7%
      ibu: 13.8
      amount: "0.7 oz"
      time: "60 min"
    - name: "Irish Moss"
      type: "Boil"
      amount: "0.5 tsp"
      time: "15 min"
    - name: "Hallertau"
      aa: 2.7%
      type: "Aroma"
      amount: "0.5 oz"
      time: "0 min"
  package_type: "Keg"
  package_date: 2018-03-18
  carb_priming:
  og: 1.045
  fg: 1.009
  abv: 4.7%
  notes: >-
---

{% include other_brews.markdown %}
{% include recipe.markdown %}
