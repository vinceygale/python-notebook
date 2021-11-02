# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 09:54:19 2021

@author: vincey
"""
#!python 3
 #一个更新的多重剪贴板
 #usage:py.exe mcb.pyw save<keyword>    -  saves clipboard to keyword
 #      py.exe mcb.pyw <keyword>        -  loads keyword to clipboard
 #      py.exe mcb.pyw list             -  loads all keywords to clipboard
 #      py.exe mcb.pyw delete<keyword>  -  delete kdyword from clipboard
 #      py.exe mcb.pyw delete           -  delete all keywords from clipboard

import sys,shelve,pyperclip

mcbShelf=shelve.open('mcb')
if len(sys.argv)==3 and sys.argv[1].lower()=='save':
    mcbShelf[sys.argv[2]]=pyperclip.paste()
elif len(sys.argv)==3 and sys.argv[1].lower()=='delete':
    mcbShelf.pop(sys.argv[2])
elif len(sys.argv)==2 and sys.argv[1].lower()=='list':
    pyperclip.copy(str(list(mcbShelf.keys())))
elif len(sys.argv)==2 and sys.argv[1].lower()=='delete':
    mcbShelf.clear()
else:
    pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()
