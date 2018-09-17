#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 14:08:39 2018

@author: Mark
"""
num = 0 
while num <= 10 :
    name = input('what is your name: ')
    if name == 'none':
        print ('there are ' + str(num) + ' of students.')
        break
    elif num == 10:
        print ('there are more than 10 students.')
    num = num + 1 
    
    