# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 13:18:48 2021

@author: vincey
"""
import pyinputplus as pyip

# sandwichSeller
LINE = '-'*30
sandwich = {}
totCost = 0.0
price = {'wheat': 2,
         'white': 1.5,
         'sourdough': 2.3,
         'chicken': 3,
         'turkey': 3.5,
         'ham': 3.3,
         'tofu': 2.6,
         'cheddar': 3.2,
         'swiss': 4,
         'mozzarella': 2.5,
         'mayo': 3,
         'mustard': 2.2,
         'lettuce': 1.9,
         'tomato': 1.3,
         ' ': 0}


def askMenu(thing: str, lst=[]):
    global totCost  # , sandwich, price
    want = pyip.inputMenu(lst, default=' ')
    sandwich[thing] = want
    totCost += price[want]
    print(want + ' : '+str(price[want])+'\nTotcost : '+str(totCost)+'\n\n')


print(LINE)
print('This\' a sandwich seller,please answer my questions:\n\n')
print('Which type bread do U want : ')
askMenu('bread', ['wheat', 'white', 'sourdough'])
print('Which type protein do U want :')
askMenu('protein', ['chicken', 'turkey', 'ham', 'tofu'])
if pyip.inputYesNo('Do you want cheese?') in ['y', 'Y', 'YES', 'yes']:
    print('Which type cheese do you want :')
    askMenu('cheese', ['cheddar', 'swiss', 'mozzarella'])
if pyip.inputYesNo('Do you want mayo/mustard/lettuce/tomato', default='No') in ['y', 'Y', 'YES', 'yes']:
    print('So,witch one do you want :')
    askMenu('other', ['mayo', 'mustard', 'lettuce', 'tomato'])
num = pyip.inputInt('How many sandwichs do U want : ', default=1, min=1)
totCost = totCost*num
print('Things'.center(10, ' ')+'Type'.center(10, ' ') + 'Unitprice'.center(6))
for k, v in sandwich.items():
    print(k.center(10, ' ')+v.center(10, ' ') + str(price[v]).center(6))
print('You want '+str(num)+' sandwich(es)\nTotcost: '+str(totCost))
