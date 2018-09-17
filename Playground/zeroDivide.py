#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 16:04:04 2018

@author: Mark
"""

def wrong(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: u can\'t divide a number by zero")

print(wrong(2))
print(wrong(3))
print(wrong(0))
print(wrong(10), "\n")

# 第二种情况

def wrong(divideBy):
        return 42 / divideBy
try:
    print(wrong(2))
    print(wrong(3))
    print(wrong(0))
    print(wrong(10))    
except ZeroDivisionError:
    print("Error: u can\'t divide a number by zero")
    
print ("this is a line, " + "\n" )
print ("jieshu")
