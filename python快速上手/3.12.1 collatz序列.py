# -*- coding: utf-8 -*-
"""
Collatz序列

Created on Wed Sep 15 12:06:50 2021

@author: vincey
"""

def collatz(n):
    if n%2==0:
        return n//2
    else: 
        return 3*n+1

print('Enter number:')
for i in range(5):
    try:
        s=int(input())
        res=collatz(s)
        print(res)
    except ValueError:
        print('input integer please!')

