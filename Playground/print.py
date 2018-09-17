#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 14:15:27 2018

@author: Mark
"""

print ("Hello")
print ("World!")
"""输出的是两行，因为末尾自带换行符"""
print ("Hello," , end = " ")
print ("world")
"""输出的为一行，并且中间有end内的连接"""
print ("cat", "dog", "cow")
print ("cat", "dog", "cow", sep = "|")
print ("cat", "dog", "cow", sep = "")
