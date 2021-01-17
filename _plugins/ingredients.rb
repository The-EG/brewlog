module Jekyll
  module IngredientsFilters
    def format_weight(amount)
      lbs = amount.floor
      oz = (amount - amount.floor) * 16.0
      w = ""
      if lbs > 0
        w += "%0.0f lbs" % [lbs]
      end
      if oz > 0
        if lbs > 0
          w += " "
        end
        w += "%0.1f oz" % [oz]
      end
      return w
    end
    
    def parse_weight(amount)
      lb = amount.match /(?<lbs>[0-9\.]+) lb/
      oz = amount.match /(?<oz>[0-9\.]+) oz/
      lbs = 0
      if lb
        lbs += lb[:lbs].to_f
      end
      if oz
        lbs += oz[:oz].to_f / 16.0
      end
      return lbs
    end

    def ingredient_weight_total(posts, grain_name)
      lbs = 0
      posts.each do |post|
        post['recipe']['fermentables'].each do |grain|
          if grain['name'] == grain_name
            lb = parse_weight(grain['amount'])
            if lb
              lbs += parse_weight(grain['amount'])
            end
          end
        end
      end
      lbs
    end

    def grain_weights(posts)
      grains = {}
      posts.each do |post|
        if post['recipe'].nil? then next end
        post['recipe']['fermentables'].each do |grain|
          if not grains.include?(grain['name'])
            grains[grain['name']] = 0
          end
          grains[grain['name']] += parse_weight(grain['amount'])
        end
      end
      return (grains.sort_by { |name, amount| amount }).reverse
    end

    def boil_ingr_weights(posts)
      hops = {}
      posts.each do |post|
        if post['recipe'].nil? then next end
        if not post['recipe']['hops'] then next end
        post['recipe']['hops'].each do |hop|
          if not hops.include?(hop['name'])
            hops[hop['name']] = 0
          end
          hops[hop['name']] += parse_weight(hop['amount'])
        end
      end
      return (hops.sort_by { |name, amount| amount }).reverse
    end
    
    def grain_list(posts)
      grains = []
      posts.each do |post|
        post['recipe']['fermentables'].each do |grain|
          if not grains.include?(grain['name'])
            grains.push(grain['name'])
          end
        end
      end
      return grains
    end
  end
end

Liquid::Template.register_filter(Jekyll::IngredientsFilters)
