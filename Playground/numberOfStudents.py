#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 16:22:50 2018

@author: Mark
"""

for i in range (10):
    name = input('what is your name: ')
    if name == 'none':
        print ('there are ' + str(i) + ' of students.')
        break
    elif i == 9:
        print ('there are more than 10 students.')