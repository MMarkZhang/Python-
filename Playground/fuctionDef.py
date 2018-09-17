#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:47:20 2018

@author: Mark
"""

import random 
def costuRate (num) :
    if num == 1 :
        return "extremely dislike"
    elif num == 2 :
        return "dislike"
    elif num == 3 :
        return "netrual"
    elif num == 4 :
        return "favor"
    elif num == 5 :
        return "really love it!!!"

print (costuRate(random.randint(1,5)))
