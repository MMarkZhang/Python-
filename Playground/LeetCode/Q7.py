#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 13:55:46 2018

@author: Mark
"""

str1 = '00123'
int1 = int(str1)
print(int1)

int2 = 2**31
print(int2)

a = -321
b = -a 
c = list(str(b))
print(c)

a //= 10 #两个/才是整除
print(a)

b /= 10 
if a == (int(-b)-1):
    print('fuck this')
print(b)

def checkPerfectNumber(num):
    from math import sqrt 
    factor = []
    up = int(sqrt(num))+1
    s = num-1 
    for n in range(2,up):
        if num/n == int(num/n) and (n not in factor) :
            factor.append((num/n))
            factor.append(n)
            s -= ((num/n)+n)
            if s == 0 :
                return True 
            elif s < 0 :
                return False 
            else:
                continue 
        else:
            continue 
    return False 

checkPerfectNumber(28)



