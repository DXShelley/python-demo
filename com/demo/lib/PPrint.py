#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/8/4 14:26
# @Author: yuzq
# @File  : PPrint
import pprint

if __name__ == '__main__':
    cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
    pprint.pformat(cats)
    file = open('myCats.txt','w')
    file.write('cats = ' + pprint.pformat(cats) + '\n')
    file.close()