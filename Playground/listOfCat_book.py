#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 21:00:08 2018

@author: Mark
"""

catNames = [] 
while True:
    nameOfCat = input('Enter the name of cat' + str(len(catNames)+1) + ': (or enter nothing to stop.)')
    if nameOfCat == '':
        break 
    catNames += [nameOfCat]
print('The cat names are:')
for name in catNames:
    print('\n' + name)
    