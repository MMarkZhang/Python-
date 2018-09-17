#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  5 19:30:46 2018

@author: Mark
"""

#方法一while loop
def feibo(upbound):
    a = 0 
    b = 1
    print (str(a))
    print (str(b))
    while a+b < upbound:
        c = a + b 
        a = b 
        b = c 
        print (str(c))
#方法二递归recursion
def recur(n):
    if n <= 1 :
         return (n)
    else:
        return (recur(n-1)+recur(n-2))
        
feibo(1000)
