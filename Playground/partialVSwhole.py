#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 14:53:36 2018

@author: Mark
"""

def spam():
    egg = 101010
    bacon()
    print(egg) 

def bacon() :
    egg = 0
    bacon = 1 

spam() #101010

def food() :
    print (shit)
shit = 12
food() #自动调用了全局变量中的shit变量 #12
print(shit) #12

def first() :
    a = "1"
    print(a)
def second() :
    a = "2"
    first()
    print(a)
first()
second()
#print(a)若在此处使用这个语句，会出现错误，因为a还未赋值
a = "3"
print(a)