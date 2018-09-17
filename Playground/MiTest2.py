#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 09:34:12 2018

@author: Mark
"""
import numpy as np 
import time as t 

def MiTest2(n):
    #start = t.time()
    result = []
    for i in range(n):
        #相当于把一行的牌，还原成一垒的牌，然后在一行中的位置，对应到一叠中 
        result = result[-1:] + result[:-1]
        result = [(n-i)] + result
    #end = t.time()
    #print(end-start)
    return result 
    
    
MiTest2(5)

l = [1,2,3,4,5]
#print(l[-1:])
#print(l[:-1])
print('--------------------')

def change(n):
    #start = t.time()
    result = [-99999999999999] 
    ls = []
    for i in range(1, n+1):
        ls.append(i)
    for index in range(n):
            result.append(ls[0])
            ls.pop(0)
            if len(ls) != 0:
                ls.append(ls[0])
                ls.pop(0)
            else:
                break 
    npresult = np.array(result)
    lsresult = list(np.argsort(npresult))
    lsresult.pop(0)
    #end = t.time()
    #print(end-start)
    return lsresult 

change(5)
        
        
  
  