# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 17:16:34 2021

@author: vincey
"""

import pyperclip
my_str = ''
lst = pyperclip.paste().split('\n')
for i in range(len(lst)):
    lst[i] = '*'+(lst[i])
    my_str = my_str+lst[i]+'\n'
print(my_str)
pyperclip.copy(my_str)


