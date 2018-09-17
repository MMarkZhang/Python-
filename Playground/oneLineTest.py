#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 09:04:59 2018

@author: Mark
"""

ls = [[1,2,3], [4,5,6], [7,8,9]]
newLs = [[l[1], l[2]] for l in ls]
print(newLs)

l1 = [2,3,4]
l1.reverse()
s1 = ''.join([str(i) for i in l1])
print(s1)

