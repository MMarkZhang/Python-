#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 17:12:10 2018

@author: Mark
"""

def food():
    global eggs
    eggs = 'small'
    
eggs = 'big' 
print(eggs)
food()
print(eggs)


def wrongFood():
    global shit #若少了这个，则会报错
    print(shit)
    shit = "awful"
shit = "weird"
wrongFood()
print(shit)
