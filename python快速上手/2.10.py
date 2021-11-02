# -*- coding: utf-8 -*-
"""
猜数字游戏，猜一个0到100的数字

Vincey gale edit 

2021-09-15
"""

import random

my_number=random.randint(1, 100)
print('Guess  the integer  bettwen 1 to 100 and tell me:\n')
while True:
    num=int(input())
    if num>my_number:
        print('Too large:')
    elif num<my_number:
        print('Too small:')
    else:
        print("Congratulations!")
        break
