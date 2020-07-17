#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/7/17 17:22
#@Author: yuzq
#@File  : Dog.py

class Dog:
    def __init__(self,name):
        self.list = []
        self.name = name

    def get_list(self):
        return self.list

    def add_list(self,item):
        self.list.append(item)


if __name__ == '__main__':
    dog = Dog("二哈")
    dog.add_list("拆家")
    dog.add_list("能吃")
    print(dog.name)
    print(dog.get_list())

    jinmao = Dog("金毛")
    jinmao.add_list("憨厚")
    jinmao.add_list("老实")
    print(jinmao.name)
    print(jinmao.get_list())

