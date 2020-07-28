#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/7/28 16:30
# @Author: yuzq
# @File  : Collata

def collatz(number):
    mod = number % 2
    if mod == 0:
        print(str(number // 2))
        return number // 2
    else:
        print(str(3 * number + 1))
        return 3 * number + 1


if __name__ == '__main__':
    print('Please enter a int number')
    try:
        num = int(input())
        while num != 1:
            num = collatz(num)
    except ValueError:
        print('must enter a int number')
