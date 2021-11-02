# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 13:18:48 2021

@author: vincey
"""
import time
import random
import re


def getAnswer():

    return


counter = 0
flag = True

while True:
    if flag:
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
    print('Tell me the answer: '+str(num1)+' * '+str(num2))
    time1 = time.time()
    answer = input()
    time2 = time.time()-time1
    print(int(time2 % 60))
    if counter > 2:
        print('Time limited !!!')
        break
    elif int(time2 % 60) > 8:
        print('Timeout or wrong answer!!')
        break
    elif re.search('\D', answer):
        print('Please input an integer!!')
        flag = False
        counter += 1
    elif num1*num2 != int(answer):
        print('Wrong answer!!')
        flag = False
        counter += 1
    else:
        print('Correct!!!')
        flag = True
