import pandas as pd

# Flour
def flour(val,unit_type):
  if(unit_type == "grams"):
    grams = val
    tbsp = grams / 8
    cup = grams / 128
  if(unit_type == "tbsp"):
    tbsp = val
    grams = tbsp * 8
    cup = tbsp / 16
  if(unit_type == "cups"):
    cup = val
    grams = cup * 128
    tbsp = cup * 16
  
  unit_cost = 1.29
  unit_size_grams = 2260
  cost = unit_cost / unit_size_grams * grams
  unit_quantity = cost / unit_cost
  calories = 4 * grams
      
  flour = [grams, tbsp, cup, cost, unit_cost, unit_quantity, calories]
  df = pd.DataFrame([flour], columns = ['grams','tbsp','cup','cost','unit_cost','unit_quantity','calories'])
  df.index = ['flour']

  return df

# Sugar 
def sugar(val,unit_type):
  if(unit_type == "grams"):
    grams = val
    tbsp = grams / 12
    cup = grams / 192
  if(unit_type == "tbsp"):
    tbsp = val
    grams = tbsp * 12
    cup = tbsp / 16
  if(unit_type == "cups"):
    cup = val
    grams = cup * 192
    tbsp = cup * 16

  unit_cost = 2.19
  unit_size_grams = 1810
  cost = unit_cost / unit_size_grams * grams
  unit_quantity = cost / unit_cost
  calories = 3.75 * grams

  sugar = [grams, tbsp, cup, cost, unit_cost, unit_quantity, calories]
  df = pd.DataFrame([sugar], columns = ['grams','tbsp','cup','cost','unit_cost','unit_quantity','calories'])
  df.index = ['sugar']

  return df

# Salt 
def salt(val,unit_type):
  if(unit_type == "grams"):
    grams = val
    tbsp = grams / 18
    cup = grams / 288
  if(unit_type == "tbsp"):
    tbsp = val
    grams = tbsp * 18
    cup = tbsp / 16
  if(unit_type == "cups"):
    cup = val
    grams = cup * 288
    tbsp = cup * 16
  
  unit_cost = .45
  unit_size_grams = 737
  cost = unit_cost / unit_size_grams * grams
  unit_quantity = cost / unit_cost
  calories = 0 * grams

  salt = [grams, tbsp, cup, cost, unit_cost, unit_quantity, calories]
  df = pd.DataFrame([salt], columns = ['grams','tbsp','cup','cost','unit_cost','unit_quantity','calories'])
  df.index = ['salt']

  return df

# Oil 
def oil(val,unit_type):
  if(unit_type == "grams"):
    grams = val
    tbsp = grams / 14.2
    cup = grams / 227.2
  if(unit_type == "tbsp"):
    tbsp = val
    grams = tbsp * 14.2
    cup = tbsp / 16
  if(unit_type == "cups"):
    cup = val
    grams = cup * 227.2
    tbsp = cup * 16

  unit_cost = 13.28 
  unit_size_grams = 1995
  cost = unit_cost / unit_size_grams * grams
  unit_quantity = cost / unit_cost
  calories = 9 * grams

  oil = [grams, tbsp, cup, cost, unit_cost, unit_quantity, calories]
  df = pd.DataFrame([oil], columns = ['grams','tbsp','cup','cost','unit_cost','unit_quantity','calories'])
  df.index = ['oil']

  return df

# Yeast 
def yeast(val,unit_type):
  if(unit_type == "grams"):
    grams = val
    tbsp = grams / 9
    cup = grams / 288
  if(unit_type == "tbsp"):
    tbsp = val
    grams = tbsp * 9
    cup = tbsp / 16
  if(unit_type == "cups"):
    cup = val
    grams = cup * 288
    tbsp = cup * 16
  
  unit_cost = 7.92 
  unit_size_grams = 908
  cost = unit_cost / unit_size_grams * grams
  unit_quantity = cost / unit_cost
  calories = 0 * grams

  yeast = [grams, tbsp, cup, cost, unit_cost, unit_quantity, calories]
  df = pd.DataFrame([yeast], columns = ['grams','tbsp','cup','cost','unit_cost','unit_quantity','calories'])
  df.index = ['yeast']

  return df


# Milk (Powdered) 
def milk(val,unit_type):
  if(unit_type == "grams"):
    grams = val
    tbsp = grams / 7
    cup = grams / 112
  if(unit_type == "tbsp"):
    tbsp = val
    grams = tbsp * 7
    cup = tbsp / 16
  if(unit_type == "cups"):
    cup = val
    grams = cup * 112
    tbsp = cup * 16
  
  unit_cost = 19.99
  unit_size_grams = 908
  cost = unit_cost / unit_size_grams * grams
  unit_quantity = cost / unit_cost
  calories = 5 * grams

  milk = [grams, tbsp, cup, cost, unit_cost,unit_quantity, calories]
  df = pd.DataFrame([milk], columns = ['grams','tbsp','cup','cost','unit_cost','unit_quantity','calories'])
  df.index = ['milk']

  return df

# Water 
def water(val,unit_type):
  if(unit_type == "grams"):
    grams = val
    tbsp = grams / 14.786
    cup = grams / 236.576
  if(unit_type == "tbsp"):
    tbsp = val
    grams = tbsp * 14.786
    cup = tbsp / 16
  if(unit_type == "cups"):
    cup = val
    grams = cup * 236.576
    tbsp = cup * 16
  
  unit_cost = 0
  unit_size_grams = 0
  unit_quantity = 0
  cost = 0
  calories = 0 * grams

  water = [grams, tbsp, cup, cost, unit_cost, unit_quantity, calories]
  df = pd.DataFrame([water], columns = ['grams','tbsp','cup','cost','unit_cost','unit_quantity','calories'])
  df.index = ['water']

  return df

# Baking Powder 
def baking_powder(val,unit_type):
  if(unit_type == "grams"):
    grams = val
    tbsp = grams / 14.4
    cup = grams / 230.4
  if(unit_type == "tbsp"):
    tbsp = val
    grams = tbsp * 14.4
    cup = tbsp / 16
  if(unit_type == "cups"):
    cup = val
    grams = cup * 230.4
    tbsp = cup * 16
  
  unit_cost = 7.87
  unit_size_grams = 340
  cost = unit_cost / unit_size_grams * grams
  unit_quantity = cost / unit_cost
  calories = 0 * grams

  baking_powder = [grams, tbsp, cup, cost, unit_cost, unit_quantity, calories]
  df = pd.DataFrame([baking_powder], columns = ['grams','tbsp','cup','cost','unit_cost','unit_quantity','calories'])
  df.index = ['baking powder']

  return df

# Experimental 
def ingredient(name,grams,grams_in_tbsp,unit_cost=1,unit_size_grams=1,calories=0):
  
  tbsp = grams / grams_in_tbsp
  cup = tbsp / 16
  
  cost = unit_cost / unit_size_grams * grams
  unit_quantity = cost / unit_cost
  calories = calories * grams

  df = [grams, tbsp, cup, cost, unit_cost, unit_quantity, calories]
  df = pd.DataFrame([df], columns = ['grams','tbsp','cup','cost','unit_cost','unit_quantity','calories'])
  df.index = [name]

  return df