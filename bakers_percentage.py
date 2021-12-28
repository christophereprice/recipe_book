import pandas as pd

def calc(df):
  

  df['bakers percentage'] = ''
    
  water_bp = df.loc['water', 'grams'] / df.loc['flour', 'grams'] * 100
  df.loc['water', 'bakers percentage'] = water_bp
    
  oil_bp = df.loc['oil', 'grams'] / df.loc['flour', 'grams'] * 100
  df.loc['oil', 'bakers percentage'] = oil_bp
    
  salt_bp = df.loc['salt', 'grams'] / df.loc['flour', 'grams'] * 100
  df.loc['salt', 'bakers percentage'] = salt_bp
    
  yeast_bp = df.loc['yeast', 'grams'] / df.loc['flour', 'grams'] * 100
  df.loc['yeast', 'bakers percentage'] = yeast_bp
    
  return df