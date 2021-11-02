# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 13:18:58 2021

@author: vincey
"""
import re


def isPhoneNumber(text: str):
    if len(text) != 12:
        return False
    if not text[0: 3].isdecimal():
        return False
    if not text[4: 7].isdecimal():
        return False
    if not text[8: 12].isdecimal():
        return False
    return True


print('415-555-4244 is a phone number:')
print(isPhoneNumber('415-555-4244'))
print('Vincey Gale is not a phone number:')
print(isPhoneNumber('Vincey Gale'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9099 is my office'
for i in range(len(message)):
    chk = message[i:i+12]
    if isPhoneNumber(chk):
        print('Phone Number Found: '+chk)
print('Done!!!')


# seach()返回一个Match对象
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
pnb = phoneNumberRegex.search(message)
print('Phone Number Found: '+pnb.group())

phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
pnh = phoneNumberRegex.search('My phone number is 415-555-4242')

# findall()
pnb = phoneNumberRegex.findall(message)
print(pnb)

# 相比之下，findall()实用性更强
# search()匹配失败会返回一个None值，而且只返回第一个匹配的值
# findall返回时不会出现None,最多会返回一个空列表，
# 而且会返回全部匹配值，可以根据自己需要取值
