# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 08:38:49 2021

@author: vincey
"""

# practice re regex

import re

numRegex = re.compile(r'^\d{1,3}(,\d{3})*$')
s = numRegex.search('25,866,134')
print(s.group())


nameRegex = re.compile('^[A-Z]\w+\sNakamoto')
s = nameRegex.search('Aatoshi Nakamoto')
print(s.group())


myRegex = re.compile(
    r'^(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.$', re.I)
myStr = ['Alice eats apples.',
         'Bob pets cats.',
         'Carol throws baseballs.',
         'Alice throws Apples.',
         'BOB EATS CATS.',
         'RoboCop eats apples.',
         'ALICE THROWS FOOTBALLS.',
         'Carol eats 7 cats.']


for i in range(len(myStr)):
    s = myRegex.search(myStr[i])
    if s is not None:
        print('匹配成功：', s.group())
    else:
        print('不匹配：', myStr[i])
