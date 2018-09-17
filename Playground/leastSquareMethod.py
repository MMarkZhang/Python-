#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 15:42:52 2018

@author: Mark
"""
# 这是least square method -> linear regression (best-fit line)

list1 = [1,2,3,4,5]
list2 = [2,4,5,4,5]

sum1 = sum(list1)
sum2 = sum(list2)

avgList1 = sum1/5
avgList2 = sum2/5 

nutor = 0 #分子 numerator 
detor = 0 #分母 denominator
for i in range(5):
    nutor += (list1[i] - avgList1) * (list2[i] - avgList2)
    detor += pow((list1[i] - avgList1),2)

print(str(nutor/detor))