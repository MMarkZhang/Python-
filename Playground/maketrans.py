#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 22:00:58 2018

@author: Mark
"""

inputTable = '12345'
outputTable = 'abcde'
testStr = '139352012'
welcome= 'hello world!'

#第一种用法：转换文字
transtab = str.maketrans(inputTable, outputTable)
print(testStr.translate(transtab))
#缩为一句语句，将字capitalize
print(welcome.translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')))

print('\n')
# 第二种用法：制作翻译表
bytes_tabtrans = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz', b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# 转换为大写，并删除字母o
print(b'runoob'.translate(bytes_tabtrans, b'o'))
