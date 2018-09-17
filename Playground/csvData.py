#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 18:21:29 2018

@author: Mark
"""
import csv 

emergent = open ('emergent.csv','r') 

lines = csv.reader(myFile)
for item in lines:
    print (item)
