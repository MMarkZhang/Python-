#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 10:59:43 2018

@author: Mark
"""

def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1.reverse()
        l2.reverse()
        s1 = ''.join([str(i) for i in l1])
        s2 = ''.join([str(i) for i in l2])
        total = int(s1) + int(s2)
        st = str(total)
        tl = []
        for i in st:
            tl.append(int(i))
        tl.reverse()
        return tl 

l1 = [2,4,3]
l2 = [5,6,4]
print(addTwoNumbers(l1, l2))

l3 = [5,6,4]

for i in range(2, -1, -1):
    print (l3[i])