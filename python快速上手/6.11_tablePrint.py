# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 19:01:56 2021

@author: vincey
"""

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'DAvid'],
             ['dogs', 'cats', 'moose', 'goose']]


def getMostLength(lst: list):
    length = 0
    for i in range(len(lst)):
        if length < len(lst[i]):
            length = len(lst[i])
    return length


def printTable1(myLst: list):
    weight = getMostLength(myLst[0])+3
    for i in range(len(myLst)):
        #tmpStr = ''
        for t in range(len(myLst[i])):
            if i == 0:
                print(myLst[t][i].rjust(weight), end='')
            else:
                print(myLst[t][i].ljust(weight), end='')

        print('\n')
    return


def printTable(myLst: list):
    weight = getMostLength(myLst[0])+3
    for r in range(len(myLst)):
        for l in range(len(myLst[r])):
            if r == 0:
                print(myLst[r][l].rjust(weight), end='')
            else:
                print(myLst[r][l].ljust(weight), end='')
        print('\n')
    return


printTable(tableData)
