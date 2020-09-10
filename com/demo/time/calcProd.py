#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/9/9 19:22
# @Author: yuzq
# @File  : calcProd
import time


def calcProd(size=1):
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, size):
        product = product * i
    return product


if __name__ == '__main__':
    start_time = time.time()
    prod = calcProd(10000)
    end_time = time.time()
    print('The result is %s digits long.' % (str(prod)))
    print('Took %s seconds to calculate.' % round(end_time - start_time,4))
