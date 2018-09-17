#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 11:06:18 2018

@author: Mark
"""

import random 
secretNumber = random.randint(1,20)
print ("I am thinking of a number between 1 and 20.")

for guessTaken in range (1,7):
    print ('Take a guess.')
    guess = int(input())
    
    if guess < secretNumber:
        print ('Your guess is too low.')
    elif guess > secretNumber: 
        print ('Your guess is too high.')
    else :
        break # This condition is the correct guess! 

if guess == secretNumber :
    print ('God Job! You guessed my number in ' + str(guessTaken) + 'guesses!')
else :
    print ('Nope. The number I was thinking of was ' + str(secretNumber))
    