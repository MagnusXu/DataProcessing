#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 11:59:57 2019

@author: lordxuzhiyu
"""

import pandas as pd
import numpy as np

data = pd.read_csv('/Users/lordxuzhiyu/Desktop/res_2019-04-01T13_12_34.712246.csv')
copy = pd.read_csv('/Users/lordxuzhiyu/Desktop/query_result copy.csv')

#df = data[['house_number', 'street']]
#print(df.dtypes)
#df1 = df['house_number'].str.cat(df['street'])
#df1 = df1.str.replace('\\s+', ' ')

#copy['full_address'] = copy['street_number'].str.cat(copy['street_name'], sep=' ')
#print(copy['full_address'])

data['add'] = data['unit_number'].str.cat(data['full_address'], sep = ' ')
data['add'] = data['add'].str.replace('\\s+', ' ')
data = data.drop_duplicates(subset = 'add', keep = "last")

copy['add'] = copy['unit_number'].str.cat(copy[['street_number', 'street_name']], sep=' ')
copy['add'] = copy['add'].str.replace('\\s+', ' ')
#print(copy['full_address'])

#data.set_index('add')
#data.transpose()
#dict_data = data[['add','bedroom', 'bathroom', 'sizeft', 'amenities']].set_index('add').to_dict(orient = 'index')


#print(dict_data)
#print(data[['bedroom', 'bathroom', 'sizeft', 'amenities']])

#copy['bedroom'] = copy['full_address'].map(bed).values()


test = pd.merge(copy, data, on = 'add', how = 'left')
test['sizeft'] = test['sizeft'].str.extract('(\d+)', expand = False)
test = test.sort_values(['sizeft', 'amenities', 'bedroom', 'bathroom'], na_position = 'last')


test.bedroom = pd.to_numeric(test.bedroom, errors = 'coerce')
test.bathroom = pd.to_numeric(test.bathroom, errors = 'coerce')

na1 = pd.isna(test['bedrooms'])
na2 = pd.isna(test['bathrooms'])
na3 = pd.notna(test['bedroom'])
na4 = pd.notna(test['bathroom'])
na5 = pd.notna(test['sizeft'])


test['need_update'] = np.where(
        (na1&na2&na3&na4&na5) |
        (test['bedrooms']==test['bedroom'])&(test['bathrooms']==test['bathroom']),0,1)

test = test.sort_values(['need_update'], ascending = True)

#print(test['need_update'])
test.to_csv('/Users/lordxuzhiyu/Desktop/test2.csv')
#result = test['equal']
#count = pd.value_counts(copy['add'].values, sort = True)
#print(count)
