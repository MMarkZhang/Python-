#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 10:17:16 2018

@author: Mark
"""

dict1 = {'first':{'shit':1, 'dick':2, 'bitch':3}, \
         'second':{'shit':3, 'dick':2, 'bitch':4}}
# print(dict1['first']['shit'])

dict2 = {}

for item in dict1:
    for word in dict1[item]:
        print(dict1[item][word])
        dict2.setdefault(word,{})
        dict2[word][item] = dict1[item][word]
 
print(dict2)
        
