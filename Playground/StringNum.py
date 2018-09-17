#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 11:31:14 2018

@author: Mark
"""
def order_weight(string):
    listofNum = string.split()
    #print (listofNum)
    dictofNum = {}
    space = " "
    str1 = ""
    for index in range(len(listofNum)) :
        count = 0
        for num in listofNum[index]:
            count += int(num)
        if count in dictofNum:
            dictofNum[count].append(listofNum[index])
            dictofNum[count].sort
        else:
            dictofNum[count] = [listofNum[index]]
    list1 = [dictofNum[k] for k in sorted(dictofNum.keys())]
    print(list1)
    for k in range(len(list1)):
        for index in range(len(list1[k])):
            str1 += (list1[k][index] + ' ')
    str1.rstrip(' ')
    print(str1)

order_weight("103 123 4444 99 2000")

print (" ----------------------------------------- ")

str1 = "180"
str2 = "90"
str3 = "56"
str4 = "65"
if str1 < str2 :
    print("180 is ahead of 90")

if str3 < str4 :
    print ("56 is ahead of 65")
   
dictofNum = {1 : ["100"] , 2 : ["11"], 4 : ["14"], 3 : ["123"]}
dictofNum[1].append("1")
print(dictofNum)

num1 = 1 
str1 = str(num1)
num1 += 1 
print(str1 + " " + str(num1))

list1 = ["180",  "90", "56", "65"]
list1.sort()
print(list1)

sorted(dictofNum.keys())
print(dictofNum)

seq = ()
for i in dictofNum:
    for item in dictofNum[i]:
        seq += tuple(item)
print(seq)

count = 0
for item in str3:
    count += int(item)
print(str(count))