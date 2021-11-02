# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 08:15:46 2021

@author: vincey
"""

import re

# use sub() for replace the string we searched

namesRegex = re.compile(r'Agent \w+')
newStr = namesRegex.sub(
    'CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(newStr)


agentNamesRegex = re.compile(r'Agent (\w)\w*')
newStr = agentNamesRegex.sub(
    r'\1****', 'Agent Alice told Agent Carol the Agent Eve knew Agent Bob was a double agent.')
print(newStr)


# 可以使用三重引号(''')创建多行字符串，然后进行注释
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                 #地区编码
    (\s|-|\.)?                         #分隔符
    \d{3}                              #前三个字符
    (\s|-|\.)                          #分隔符
    \d{4}                              #后四个字符
    (\s*(ext|x|ext.)\s*\d{2,5})?       #扩展
    )''', re.VERBOSE)
