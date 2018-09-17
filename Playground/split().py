#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 21:40:35 2018

@author: Mark
"""

stringList = input("输入数值，每个数值用空格隔开")
listString = stringList.split(" ")
list1 = []
listA = []
listB = []
listD = []
a1 = 0 
b1 = 0 
d1 = 0
for i in listString:
    list1.append(int(i))
    
while a1 < len(list1): 
    a2 = a1 + 1
    while a2 < len(list1):
        listA.append(list1[a1]+list1[a2])
        a2 = a2 + 1
    a1 = a1 + 1

while b1 < len(list1): 
    b2 = b1 + 1
    while b2 < len(list1):
        listB.append(abs(list1[b1]+list1[b2]))
        b2 = b2 + 1
    b1 = b1 + 1

while d1 < len(listA): 
    d2 = d1 + 1
    while d2 < len(listB):
        listD.append(abs(listA[d1]+listB[d2]))
        d2 = d2 + 1
    d1 = d1 + 1
    
print(str(max(listD) + min(listD) + len(listD)))


