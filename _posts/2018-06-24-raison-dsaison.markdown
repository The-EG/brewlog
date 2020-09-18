---
layout: post
title: "Raison D'Saison"
date: 2018-06-24
tags:
  - saison
  - brewing classic styles
brew_type: beer

recipe:
  type: "All Grain"
  style: "25B - Saison"
  size: "4.25 gallon"
  efficiency: 72%
  est_og: 1.064
  est_fg: 1.006
  est_abv: 7.5%
  color: 5.7
  ibus: 26.5
  boil_time: "90 min"
  yeast: "WY3724"
  ferm_time: "10 days"
  ferm_temp: 68F
  fermentables:
    - name: "Pilsner (German)"
      amount: "7 lbs 5 oz"
      perc: 77.5%
    - name: "Munich"
      amount: "10 oz"
      perc: 6.6%
    - name: "Wheat"
      amount: "10 oz"
      perc: 6.6%
    - name: "Crystal 60L"
      amount: "2 oz"
      perc: 1.3%
  mash:
    - name: "Mash In"
      strike_temp: "157F"
      amount: "11 qt"
      target_temp: "147F"
      time: "60 min"
    - name: "Mash Out"
      strike_temp: "206F"
      amount: "7 qt"
      target_temp: "168F"
      time: "10 min"
  sparge: fly sparge
  hops:
    - name: "Sugar, Table"
      type: "Boil"
      perc: 7.9%
      amount: "12 oz"
      time: "60 min"
    - name: "Hallertau"
      type: "Boil"
      aa: 4.5%
      ibu: 26.5
      amount: "1.24 oz"
      time: "60 min"
    - name: "Irish Moss"
      type: "Boil"
      amount: "0.5 tsp"
      time: "15 min"
    - name: "Hallertau"
      aa: 4.5%
      type: "Aroma"
      amount: "0.75 oz"
      time: "0 min"
  package_type: "Keg"
  package_date: 2018-10-08
  carb_priming:
  og: 1.061
  fg: 1.003
  abv: 7.6%
  notes: >-
---
From the book Brewing Classic Styles
{% include other_brews.markdown %}
{% include recipe.markdown %}
