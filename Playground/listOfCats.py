#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 20:54:16 2018

@author: Mark
"""

numOfCat = int(input('How many cat do you have: '))
i = 0 
listOfCat = []
while i < numOfCat :
    i += 1
    catName = input('The name of the ' + str(i) + ' cat is: ')
    listOfCat = listOfCat + [str('The cat' + str(i)+ ' is named '  + catName)]
    if i == numOfCat:
        break 
for name in listOfCat :
    print('\n' + name)