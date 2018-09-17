#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 14:18:16 2018

@author: Mark
"""

str1 = "absdxsd"
list1 = list(str1)
print(list1)

str2 = "01010001010"
tape = list(map(int, str2))
print(tape)

a = -1 
b = 0 
c = 1 
d = 2 
e = -2 
if a :
    print ("-1 is true")
if b :
    print ("0 is true")
if c :
    print ("1 is true")
if d :
    print ("2 is true")
if e :
    print ("-2 is true")
    
c |= 1
print(str(c))

def loop (i) :
    step = 10
    step += 5 if not i else i // abs(i)
    print("test:" + str(step))

loop (c)