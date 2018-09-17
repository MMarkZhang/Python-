#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 14:55:09 2018

@author: Mark
"""

def zero(fun=None):
    if fun is None:
        return 0 
    else: 
        if fun[0] == 'p':
            return fun[1] + 0 
        if fun[0] == 'm':
            return 0-(fun[1] - 0)
        if fun[0] == 't':
            return fun[1] * 0
        if fun[0] == 'd':
            return 0
        
def one(fun=None):
    if fun is None:
        return 1 
    else: 
        if fun[0] == 'p':
            return fun[1] + 1
        if fun[0] == 'm':
            return 0-(fun[1] - 1)
        if fun[0] == 't':
            return fun[1] * 1
        if fun[0] == 'd':
            return int(1/(fun[1]/1))
        
def two(fun=None):
    if fun is None:
        return 2 
    else: 
        if fun[0] == 'p':
            return fun[1] + 2 
        if fun[0] == 'm':
            return 0-(fun[1] - 2)
        if fun[0] == 't':
            return fun[1] * 2
        if fun[0] == 'd':
            return int(1/(fun[1]/2))
        
def three(fun=None):
    n = 3
    if fun is None:
        return n 
    else: 
        if fun[0] == 'p':
            return fun[1] + n 
        if fun[0] == 'm':
            return 0-(fun[1] - n)
        if fun[0] == 't':
            return fun[1] * n
        if fun[0] == 'd':
            return int(1/(fun[1]/n))
        
def four(fun=None):
    n = 4
    if fun is None:
        return n 
    else: 
        if fun[0] == 'p':
            return fun[1] + n 
        if fun[0] == 'm':
            return 0-(fun[1] - n)
        if fun[0] == 't':
            return fun[1] * n
        if fun[0] == 'd':
            return int(1/(fun[1]/n))
        
def five(fun=None):
    n = 5
    if fun is None:
        return n 
    else: 
        if fun[0] == 'p':
            return fun[1] + n 
        if fun[0] == 'm':
            return 0-(fun[1] - n)
        if fun[0] == 't':
            return fun[1] * n
        if fun[0] == 'd':
            return int(1/(fun[1]/n))
        
def six(fun=None):
    n = 6
    if fun is None:
        return n 
    else: 
        if fun[0] == 'p':
            return fun[1] + n 
        if fun[0] == 'm':
            return 0-(fun[1] - n)
        if fun[0] == 't':
            return fun[1] * n
        if fun[0] == 'd':
            return int(1/(fun[1]/n))

def seven(fun=None):
    n = 7
    if fun is None:
        return n 
    else: 
        if fun[0] == 'p':
            return fun[1] + n 
        if fun[0] == 'm':
            return 0-(fun[1] - n)
        if fun[0] == 't':
            return fun[1] * n
        if fun[0] == 'd':
            return int(1/(fun[1]/n))
        
def eight(fun=None):
    n = 8
    if fun is None:
        return n 
    else: 
        if fun[0] == 'p':
            return fun[1] + n 
        if fun[0] == 'm':
            return 0-(fun[1] - n)
        if fun[0] == 't':
            return fun[1] * n
        if fun[0] == 'd':
            return int(1/(fun[1]/n))

def nine(fun=None): 
    if fun is None :
        return 9 
    else:
        if fun[0] == 'p':
            return fun[1] + 9 
        if fun[0] == 'm':
            return 0-(fun[1] - 9)
        if fun[0] == 't':
            return fun[1] * 9
        if fun[0] == 'd':
            return int(1/(fun[1]/9))

def plus(num): 
    return ['p',num]
def minus(num): 
    return ['m',num]
def times(num): 
    return ['t',num]
def divided_by(num): 
    return ['d',num]

