#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 16:29:16 2018

@author: Mark
"""
n = 2**10
k = 0 
while n >= 1 :
    for j in range(1, int(n)+1):
        k += 1 
    n = n/2 
print(k)
