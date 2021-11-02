# -*- coding: utf-8 -*-
"""
5.6.2编程任务 --好玩的物品清单

Created on Sat Sep 18 20:48:12 2021

@author: vincey
"""

dic_things = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayInventory(things: dict):
    print('---------------------------------------------')
    print('Inventory:')
    tot_num = 0
    for k, v in things.items():
        print(str(v)+' '+k)
        tot_num += v
    print('Totle number of items:'+str(tot_num))
    print('---------------------------------------------')


def addToInventory(inventory: dict, items=[]):
    if items == []:
        pass
    else:
        for item in items:
            inventory[item] = inventory.get(item, 0) + 1
    return inventory


displayInventory(dic_things)

addToInventory(dic_things, dragonLoot)

displayInventory(dic_things)
