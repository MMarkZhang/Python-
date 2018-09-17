#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 16:28:51 2018

@author: Mark
"""

#n = int(input())

#a = list(map(int, input().rstrip().split()))

#print(a)

c = [1,2,4,3,5]
b = []
sortedC = sorted(c)
for index in range(len(c)):
    for num in range(len(c)):
        b = c
        swapNum = b[index]
        b[index] = b[num]
        b[num] = swapNum
        print(b)
        print(c)