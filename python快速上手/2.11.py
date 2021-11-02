# -*- coding: utf-8 -*-

"""
石头、剪刀、布游戏

Created on Wed Sep 15 11:10:58 2021

@author: vincey
"""

import random

lst=['s','j','b'] #s:石头,j:剪刀,b:布
dic={'赢':0,'输':0,'平':0}
print('这是一个石头、剪刀、布的游戏。请输入你想出的图形：')#\n石头（s），剪刀（j），布（b），退出（q）:')
while True:
    my_tag=lst[random.randint(0,2)]
    ur_tag=input('石头（s）?剪刀（j）?布（b）?退出（q）? :')
    if ur_tag=='q':
        break
    elif ur_tag==my_tag:
        dic['平']=dic['平']+1
    elif my_tag=='s' and ur_tag=='j':
        dic['输']=dic['输']+1
    elif my_tag=='s' and ur_tag=='b':
        dic['赢']=dic['赢']+1
    elif my_tag=='j' and ur_tag=='s':
        dic['赢']=dic['赢']+1
    elif my_tag=='j' and ur_tag=='b':
        dic['输']=dic['输']+1
    elif my_tag=='b' and ur_tag=='s':
        dic['输']=dic['输']+1
    elif my_tag=='b' and ur_tag=='j':
        dic['赢']=dic['赢']+1
    else:
        print(ur_tag+'是个错误的输入！')
    print(dic)


