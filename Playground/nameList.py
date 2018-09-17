#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 11:23:02 2018

@author: Mark
"""

def namelist(names):
    nameList = ''
    n = len(names)
    if n == 0:
        return ''
    elif n ==1 :
        return names[0]['name']
    for index in range(n-2):
        nameList += (names[index]['name'] + ', ')
    nameList += (names[n-2]['name'] + ' & ' + names[n-1]['name'])
    return nameList
        
print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))

#使用.join 太妙了 ; join相当于在每两个字符之间加上指定string
def namelist2(names):
    if len(names)==0: return ''
    elif len(names)==1: return names[0]['name']
    return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + \
            names[-1]['name']

str1 = '12345678'
print(str1[:-1])