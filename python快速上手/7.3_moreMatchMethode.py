# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 13:51:54 2021

@author: vincey
"""
import re

# More match mode about regex

# 在传给re.compile()原始字符串中，
# 需要匹配特殊字符时需要使用‘\’进行转义
# \. \^ \$ \* \+ \? \{ \} \[ \] \\ \| \( \)


# 1. use '()' to group the match

phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
pnb = phoneNumberRegex.search('My numbser is 415-555-5252')
print(pnb.group(1))

# Use channel to slip the group : '|'
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))


# Use '?' for selectable match

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman.')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman.')
print(mo2.group())

# Use '*' for match any times (0 time or more than 1 times)
batRege = re.compile(r'Bat(wo)*man')
mo1 = batRege.search('The Adventures of Batman.')
print(mo1.group())
mo2 = batRege.search('The Adventures of Batwoman.')
print(mo2.group())
mo3 = batRege.search('The Adventures of Batwowowowowoman.')
print(mo3.group())


# Use '+' for match  1 time or more times
batRege = re.compile(r'Bat(wo)+man')
mo1 = batRege.search('The Adventures of Batwoman.')
mo2 = batRege.search('The Adventures of Batwowowowoman')
mo3 = batRege.search('The Adventures of Batman')
print(mo1.group())
print(mo2.group())
print(mo3 == None)  # ‘+’只能匹配一次以上，对于0次的是不会匹配的

# Use '{}' for match given times
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo2 = haRegex.search('Ha'*3)
print(mo2.group())

# 贪心匹配方式 {a,b} （b>a）这种方式可以匹配a到b次的出现（a<=n<=b）
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHa')
mo2 = greedyHaRegex.search('HaHaHaHa')
mo3 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
print(mo2.group())
print(mo3.group())
