# -*- coding: utf-8 -*-
"""
conway's game of life

Created on Thu Sep 16 11:11:39 2021

@author: vincey gale
"""

import random,time,copy

WIDTH=10
HEIGHT=10
nextCells=[]

# function of print the list
def prt(lst): 
    for x in range(WIDTH):
        print(lst[x])

# create the list
for x in range(WIDTH):
    column=[]
    for y in range(HEIGHT):
        if random.randint(0,1)==0:
            column.append('*')
        else:
            column.append(' ')
    nextCells.append(column)

# count the char in the list 
def cnt(lst,tp):
    s=0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if lst[x][y]==tp:
                s+=1
    return s

# main loop
while True:
    print('\n\n\n')
    currentCells=copy.deepcopy(nextCells)
    prt(currentCells)
    print(cnt(currentCells, '*'))
    for x in range(WIDTH):
        for y in range(HEIGHT):
            flag_alive=0 
            leftCell=(x-1)%WIDTH
            rightCell=(x+1)%WIDTH
            upperCell=(y+1)%HEIGHT
            downCell=(y-1)%HEIGHT
            #判断四周的字符是不是‘*’以改变标志符
            if currentCells[leftCell][upperCell]=='*':
                flag_alive+=1
            if currentCells[leftCell][y]=='*':
                flag_alive+=1
            if currentCells[leftCell][downCell]=='*':
                flag_alive+=1  
            if currentCells[rightCell][upperCell]=='*':
                flag_alive+=1  
            if currentCells[x][upperCell]=='*':
                flag_alive+=1  
            if currentCells[x][rightCell]=='*':
                flag_alive+=1  
            if currentCells[rightCell][downCell]=='*':
                flag_alive+=1  
            if currentCells[x][downCell]=='*':
                flag_alive+=1  
            #通过生成新的列表
            if currentCells[x][y]=='*' and (flag_alive in (2,3)):
                nextCells[x][y]='*'
            elif currentCells[x][y]==' ' and flag_alive==3:
                nextCells[x][y]='*'
            else:
                nextCells[x][y]=' '
                
    time.sleep(2)


    
