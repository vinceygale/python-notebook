# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 13:40:02 2021

@author: vincey
"""

birthdays = {'Bob': 'Apr 1', 'Alice': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    my_name = input('Please input UR name:')
    if my_name == '':
        break
    elif my_name in birthdays:
        print(my_name+"'s birthday is "+birthdays[my_name])
    else:
        print('Can not find the '+my_name+"'s birthday data.")
        birthdays[my_name] = input('Input UR birthday please:')
        print('Data of birthdays hass updated !')
