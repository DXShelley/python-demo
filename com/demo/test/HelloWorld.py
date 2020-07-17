#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/7/17 17:16
#@Author: yuzq
#@File  : HelloWorld.py

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


if __name__ == '__main__':
    d = Dog("小狗")
    d.add_trick("hhhhh")
    print(d.tricks)