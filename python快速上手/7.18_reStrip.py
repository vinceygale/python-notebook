# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 17:06:56 2021

@author: vincey
"""

# 用正则表达式完成strip()功能

import re

myStr = '43OOasd    '
mychars = 'OO'


def re_strip(myString: str, stripChars=''):
    reStr = ''
    if stripChars != '':
        reStr = re.sub(re.compile(stripChars), '', myString)
    else:
        reStr = re.sub(re.compile(r'\s*$'), '', myString)
    return reStr


print(re_strip(myStr, mychars))
