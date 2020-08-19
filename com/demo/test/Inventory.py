#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/7/29 17:47
# @Author: yuzq
# @File  : Inventory

def display_inventory(dic={}):
    print('Inventory:')
    count = 0
    for item in dic.items():
        print(str(item[1]) + ' ' + item[0])
        count += item[1]

    print('Total number of items: ' + str(count))


def add_to_inventory(inventory={}, added_items=[]):
    for item in added_items:
        if item not in inventory:
            inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


if __name__ == '__main__':
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = add_to_inventory(inv, dragonLoot)
    display_inventory(inv)
