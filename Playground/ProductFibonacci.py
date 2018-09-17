#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 14:23:05 2018

@author: Mark
"""
from math import sqrt 

def Fib(n):
    a = 0 
    b = 1 
    c = 0
    FibList = [0,1]
    while c < n:
        c = a + b 
        a = b
        b = c
        if c > n:
            continue 
        else:
            FibList.append(c)
    return FibList
        
#print(Fib(573147844013817084101*927372692193078999176))

def Recursion_Fib(n):
    if n <= 0: 
        return 0 
    elif n == 1:
        return 1
    else:
        return Recursion_Fib(n-1)+Recursion_Fib(n-2)
        
    
#print(str(Recursion_Fib(10)))

def productFib(prod):
    top = (sqrt(prod))*2
    FibList = Fib(int(top)+1)
    result = [] 
    for index in range(len(FibList)-1):
        pro = FibList[index]*FibList[index+1]
        if pro == prod:
            result = [FibList[index], FibList[index+1], True]
        elif pro > prod:
            result = [FibList[index], FibList[index+1], False]
    print(str(top)) 
    print(str(573147844013817084101+927372692193078999176))


productFib(531521659127752446580404735205751701700776)
#print (str(573147844013817084101*927372692193078999176))

def testFib():
    a = 0
    b = 1
    c = 0
    d = 0 
    prod = 1
    while d < prod:
        c = a + b 
        d = a*b
        a = b
        b = c
        top = (sqrt(d))*2
        FibList = Fib(int(top))
        prod = FibList[-2]*FibList[-1]
        print(str(c))

#testFib()








