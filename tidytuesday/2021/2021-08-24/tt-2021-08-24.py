#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 19:52:32 2021

@author: YouCanCallMeAll
"""
# %% import pandas module
import pandas as pd
from graphviz import Digraph

# %% import lemur data
lemur_data_url = r'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-08-24/lemur_data.csv'
lemur_data = pd.read_csv(lemur_data_url,index_col=0,parse_dates=[0], encoding = 'unicode_escape')

# %% import taxonomy
tax_url = r'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-08-24/taxonomy.csv'
taxonomy = pd.read_csv(tax_url,index_col=0,parse_dates=[0], encoding = 'unicode_escape')

# %% profile datasets
print(lemur_data.head(5))
for col in lemur_data:
    print(col)

print(taxonomy.head(5))
for col in taxonomy:
    print(col)

# %% join datasets on taxonomy
lemur_data = lemur_data.join(taxonomy)

print(lemur_data.head(5))
for col in lemur_data:
    print(col)
    
# %% print lemur's name, and the name of its dam and sire
lemur_name = lemur_data[['dlc_id','name', 'dam_id', 'dam_name', 'sire_id', 'sire_name']]
lemur_name = lemur_name.drop_duplicates()
print(lemur_name)
