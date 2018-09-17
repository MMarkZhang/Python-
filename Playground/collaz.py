#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 11:08:43 2018

@author: Mark
"""

# Give a number to process
while True:
    try:
        print('Enter an integer number:')
        n = int(input())
        break
    except:
        print('You gave a noninteger string.')

# set function to process n
def collatz(number):
    r = number % 2
    if r == 0:
        return number // 2
    else:
        return 3 * number + 1

# while-loop to display the results
while n !=1:
    print(collatz(n))
    n = collatz(n)