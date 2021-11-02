# -*- coding: utf-8 -*-
"""
第四章课后练习

Created on Thu Sep 16 17:20:27 2021

@author: vincey
"""

import random


# 4.11.1 逗号代码：

def prt(lst):
    for i in range(len(lst)-1):
        print(lst[i], end=', ')
    print('and '+str(lst[-1]))


spam = ['apples', '', 'bananas', 'tofu', 'cats', 5]
prt(spam)


# 4.11.2 统计连续


def rdm(number):
    streaks = []
    for i in range(number):
        if random.randint(0, 1) == 1:
            streaks.append('H')
        else:
            streaks.append('T')
    return streaks


def cnt(lst):
    sum = 1
    counter = 0
    for i in range(1, len(lst)-1):
        if lst[i] == lst[i+1]:
            sum += 1
            if sum == 6:
                counter += 1
        else:
            sum = 1
    return counter


print(cnt(rdm(10000)))


# 4.11.3 字符图网格反转

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'o', 'o', '.', '.', '.'],
        ['o', 'o', 'o', 'o', '.', '.'],
        ['o', 'o', 'o', 'o', 'o', '.'],
        ['.', 'o', 'o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'o', 'o', '.'],
        ['o', 'o', 'o', 'o', '.', '.'],
        ['.', 'o', 'o', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def chg(lst, x=1, y=1):  # 进行反转图形
    my_list = []
    for i in range(0, y):
        tmp_list = []
        for t in range(0, x):
            tmp_list.append(lst[t][i])
        my_list.append(tmp_list)
    return my_list


def pnt(lst, x=1, y=1):  # 打印图形
    for i in range(x):
        for t in range(y):
            print(lst[i][t], end=' ')
        print('')


new_list = chg(grid, 9, 6)
print('\n\n原图形：')
pnt(grid, 9, 6)
print('\n\n处理完成后：')
pnt(new_list, 6, 9)

print('\n\n另外一种方式进行反转')

for i in range(6):
    for t in range(9):
        print(grid[t][i], end=' ')
    print('')
