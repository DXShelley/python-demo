#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/7/29 11:48
# @Author: yuzq
# @File  : TestList


def method(li=[]):
    ret = ''
    for i in range(len(li) - 2):
        ret += li[i];
        ret += ','
    ret += 'and '
    ret += li[len(li) - 1]
    return ret





if __name__ == '__main__':
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(method(spam))
