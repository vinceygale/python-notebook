# -*- coding: utf-8 -*-
"""
a program for cheese check

Created on Sat Sep 18 17:56:00 2021

@author: vincey
"""

my_cheese = {'1h': 'bking', '6c': 'wqueen', '2c': 'bpawn',
             '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
pieces = ['king', 'queen', 'knight', 'rook', 'bishop', 'pawn']
W_lst = []
B_lst = []
#
for i in range(len(pieces)):
    W_lst.append('w'+pieces[i])
    B_lst.append('b'+pieces[i])


def count(lst: list, s=' '):  # for count how many time does s in list
    counter = 0
    for data in lst:
        if data == s:
            counter += 1
    return counter


def check_k(diction):  # for checking the coordinate of pieces
    flag = True
    keys = list(diction.keys())
    for i in range(len(keys)):
        if len(keys[i]) > 2:
            flag = False
            print(keys[i]+' 棋子坐标出现错误！')
        elif (keys[i][0] not in ['1', '2', '3', '4', '5', '6', '7', '8']) or (keys[i][-1] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
            flag = False
            print(keys[i]+' 棋子坐标出现错误！')
        elif int(keys[i][0]) > 8:
            flag = False
            print(keys[i]+' 棋子坐标出现错误！')
    return flag


def check_v(diction):  # for ckecking the name and numbers of pieces
    flag = True
    w_num = 0
    b_num = 0
    values = list(diction.values())
    for i in range(len(values)):
        if (values[i] not in W_lst) and (values[i] not in B_lst):
            flag = False
            print(values[i] + ' is a wrong pieces')
        if values[i][0] == 'b':
            b_num += 1
        if values[i][0] == 'w':
            w_num += 1
    if count(values, 'bking') > 1:  # 检查黑王数量
        flag = False
        print('There is more than one bking in this cheese!!')
    if count(values, 'wking') > 1:  # 检查白王数量
        flag = False
        print('There is more than one wking in this cheese!!')
    if count(values, 'bpawn') > 8:  # 检查黑卒数量
        flag = False
        print('U can have 8 bpawns as most!!')
    if count(values, 'wpawn') > 8:  # 检查白卒数量
        flag = False
        print('U can have 8 wpawns as most!!')
    if b_num > 16 or w_num > 16:   #检查双方棋子数量
        flag = False
        print('U can have 16 pieces as most!!')
    return flag


# 打印原始数据
for k, v in my_cheese.items():
    print(k+':  '+v)
# 开始进行检查
if check_k(my_cheese) and check_v(my_cheese):
    print('棋子检查成功！')
else:
    print('棋子检查失败！')
