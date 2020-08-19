#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/8/4 21:12
# @Author: yuzq
# @File  : TestWalk
import os
if __name__ == '__main__':
    for folderName, subfolders, filenames in os.walk('E:\\RDJ-YUZHENQUAN\\Desktop\\linshi\\8样式'):
        print('The current folder is ' + folderName)
        for subfolder in subfolders:
            print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        for filename in filenames:
            path = os.path.join(folderName,filename)
            print('FILE INSIDE ' + folderName + ': ' + filename)
            print('------path -----------' + path)
    print('')
    print('-- --------------------'  + path)