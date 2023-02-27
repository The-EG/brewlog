---
layout: post
title: We'll Wheat Again
date: 2023-02-26
tags:
  - weissbier
brew_type: beer
image: /assets/well wheat again/white-wheat.png
images:
 - src: /assets/well wheat again/brewday.png
   desc: a not rainy brew day!
 - src: /assets/well wheat again/white-wheat.png
   desc: White Wheat
 - src: /assets/well wheat again/pilsen.png
   desc: German Pilsen
 - src: /assets/well wheat again/original-gravity.png
   desc: OG = 1.049

ferm_history:
  - date: 2023-02-26 16:30:00
    temp: 71.8
  - date: 2023-02-27 15:30:00
    temp: 71.5

recipe:
  type: All Grain
  style: 10A - Weissbier
  size: 2.6 gallon
  efficiency: 68%
  est_og: 1.053
  est_fg: 1.011
  est_abv: 5.6%
  color: 4.0
  ibus: 10
  boil_time: 60 min
  yeast: LalBrew Munic Classic
  ferm_time: 10 days
  ferm_temp: 70F
  fermentables:
    - name: White Wheat
      amount: 3.39 lbs
      perc: 67.0%
    - name: Pilsen (GE)
      amount: 1.81 lbs
      perc: 33.0%
    - name: Rice Hulls
      amount: 0.25 lbs
      perc: "-"
  mash:
    - name: Mash In
      strike_temp: 164F
      amount: 2 gallons
      target_temp: 153F
      time: 60 min
  sparge: batch sparge, 1 step, 2.5 gallons @ 182F
  hops:
    - name: Liberty
      type: Boil
      aa: 4.3%
      ibu: 8.5
      amount: 0.25 oz
      time: 60 min
    - name: Irish Moss
      type: Boil
      amount: 0.5 tsp
      time: 10 min
    - name: Liberty
      type: Boil
      aa: 4.3%
      ibu: 1.7
      amount: 0.25 oz
      time: 2 min
  package_type: 
  package_date: 
  carb_priming: 
  og: 1.049
  fg: 
  abv:
---
A Weihenstephaner clone.

 - Got 1 qt extra from sparge, boiled 90 minutes instead of 60
 - May have been from leak in mash tun?
 
 - 2.6 gallons into fermenter
 - Oxygenated worth for ~30-45 seconds prior to pitching
 - Pitched 1 pkg @ ~72F on 2023-02-26 16:05

{% include ferm-temp-chart.html %}

{% include other_brews.markdown %}
