#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 14:43:31 2018

@author: Mark
"""

inputList = input()
intList = inputList.split(" ")
column = int(intList[0])
row = int(intList[1])
numIndex = int(intList[2])
numList = [] 
c = 1
r = 1
i = 0
while c <= column:
    while r <= row: 
        numList.append(c*r)
        r = r + 1 
    r = 1
    c = c + 1
guessList = sorted(numList)
print (str(guessList[numIndex-1]))

# 输出是对了，但是内存超限了，还不够优化，需要学习