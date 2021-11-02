# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 16:24:42 2021

@author: vincey
"""

# Check password

import re

password = '12A1234dfc'
lenghRegex = re.compile(r'.{8,}')
charRegex = re.compile(r'[a-z]*[A-Z]*')
numRegex = re.compile(r'\d+')


def checkLength(pwd: str):
    if lenghRegex.search(pwd) is not None:
        return True
    else:
        return False


def checkChars(pwd: str):
    if charRegex.search(pwd) is not None:
        return True
    else:
        return False


def checkNums(pwd: str):
    if numRegex.search(pwd) is not None:
        return True
    else:
        return False


if not checkLength(password):
    print('密码长度不符合要求！')
elif not checkChars(password):
    print('密码中应包含大写和小写字母！')
elif not checkNums(password):
    print('密码中应包含数字！')
else:
    print('密码强度合格！')
