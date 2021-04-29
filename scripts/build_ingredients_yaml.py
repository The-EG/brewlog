import os
import yaml
import re

def format_weight(weight, imperial=True, fmt='0.2f'):
    if weight is None: return ''
    if not imperial:
        if weight >= 1 or weight == 0: return f'{weight:{fmt}} kg'
        else: return f'{weight*1000:{fmt}} g'
    else:
        if weight == 0: return f'{weight:{fmt}} lbs'
        pounds = weight / 0.4535924
        oz = weight / 0.02834952
        if pounds >= 1 and oz % 16 > 0.0001: return f'{int(pounds):0.0f} lbs {oz % 16:{fmt}} oz'
        elif pounds >=1: return f'{pounds:{fmt}} lbs'
        else: return f'{oz:{fmt}} oz'

def parse_amount(amount_str, uoms, fullmatch=False):
    if isinstance(amount_str, float) or isinstance(amount_str, int): return amount_str
    amount_str = amount_str.lower().strip()

    try: return float(amount_str)
    except ValueError:
        val = 0
        matched = False
        for unit in uoms:
            if fullmatch: m = re.fullmatch(unit[0], amount_str)
            else: m = re.search(unit[0], amount_str)
            if m is not None:
                val += (float(m[1]) * unit[1])
                matched = True
        if matched: return val
    return None

def parse_volume(volume_str):
    return parse_amount(volume_str, [
        (r'(\d*\.?\d+) ?l( |$)', 1), # liters
        (r'(\d*\.?\d+) ?ml', 0.001), # mililiters
        (r'(\d*\.?\d+) ?(gallon|gal)', 3.785412), # gallons
        (r'(\d*\.?\d+) ?(quarts|qts|qt)', 0.946353), # quarts
        (r'(\d*\.?\d+) ?tsp', 0.00492892),
        (r'(\d*\.?\d+) ?(tbsp|tbs)', 0.0147868)
    ])

def parse_weight(weight_str):
    return parse_amount(weight_str, [
        (r'(\d*\.?\d+) ?kg', 1), # kilograms
        (r'(\d*\.?\d+) ?g', 0.001), # grams
        (r'(\d*\.?\d+) ?(lbs|lb)', 0.4535924), # pounds
        (r'(\d*\.?\d+) ?oz', 0.02834952) # ounces
    ])

def parse_volume_or_weight(amount_str):
    vol = parse_volume(amount_str)
    if vol is not None: return vol, True
    else: return parse_weight(amount_str), False

def get_post_ingredients(folder, data={'fermentables': {}, 'hops': {}}):
    with os.scandir(folder) as it:
        for ent in it:
            if ent.is_dir(): 
                get_post_ingredients(ent.path, data)
            else:
                with open(ent.path) as postfile:
                    post = next(yaml.load_all(postfile, Loader=yaml.FullLoader))
                    if ('brew_type' in post and post['brew_type']=='beer' and
                        'recipe' in post):
                        if 'fermentables' in post['recipe']:
                            for f in post['recipe']['fermentables']:
                                amt, is_vol = parse_volume_or_weight(f['amount'])
                                if f['name'] not in data['fermentables'] and not is_vol:
                                    data['fermentables'][f['name']] = 0
                                if not is_vol and amt is not None: data['fermentables'][f['name']] += amt
                        if 'hops' in post['recipe'] and post['recipe']['hops'] is not None:
                            for h in post['recipe']['hops']:
                                amt, is_vol = parse_volume_or_weight(h['amount'])
                                if h['name'] not in data['hops'] and not is_vol:
                                    data['hops'][h['name']] = 0
                                if not is_vol and amt is not None: data['hops'][h['name']] += amt
    return data
                        



if __name__=='__main__':
    data = get_post_ingredients('./_posts')
    yml_data =  {
        'fermentables': [{
            'name': f, 
            'amount': data['fermentables'][f],
            'amount_str': format_weight(data['fermentables'][f])
        } for f in data['fermentables']],
        'hops': [{
            'name': h,
            'amount': data['hops'][h],
            'amount_str': format_weight(data['hops'][h])
        } for h in data['hops']]
    }
    yml_data['fermentables'] = sorted(yml_data['fermentables'], key=lambda x:x['amount'], reverse=True)
    yml_data['hops'] = sorted(yml_data['hops'], key=lambda x:x['amount'], reverse=True)
    with open('./_data/ingredients.yaml','w') as out:
        yaml.dump(yml_data,out)
