# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 11:36:40 2021

@author: vincey
"""

import re
import pyperclip

phoneRegex = re.compile(r'''\d{11}|           # 手机号
                        \d{3}-\d{8}|          # 区号为三位的电话号码
                        \d{4}-\d{7}           # 区号为四位的电话号码
                        ''')

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                # 邮箱头
    @                                # @
    [a-zA-Z0-9.-]+                   # 域名头
    \.[a-zA-Z]{2,4}                  # 域名尾 
    )''', re.VERBOSE)

text = pyperclip.paste()
phoneList = phoneRegex.findall(text)
emailList = emailRegex.findall(text)
myPhoneList = ''
myEmailList = ''

for i in range(len(phoneList)):
    myPhoneList += 'PhoneNo '+str(i)+': '+phoneList[i]+'\n'
print(myPhoneList)

for i in range(len(emailList)):
    myEmailList += 'Email '+str(i)+': '+emailList[i]+'\n'
print(myEmailList)
