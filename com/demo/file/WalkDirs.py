#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/8/8 10:01
# @Author: yuzq
# @File  : WalkDirs
import shutil
import sys
from pathlib import Path


def searchExt(ext, source, target):
    # ext = r'jpg'
    # source = r'E:\RDJ-YUZHENQUAN\Desktop\linshi\python\searchext'
    # target = r'E:\RDJ-YUZHENQUAN\Desktop\linshi\python\searchexttarget'
    print('-----------method-----------')
    print(ext)
    print(source)
    print(target)
    print('-----------method-----------')

    all = []
    import os
    for dir, subdirs, files in os.walk(source):
        for file in files:
            print(file)
            if (file.endswith(ext)):
                all.append(file)
                shutil.copy(os.path.join(dir, file), target)

    print('Done.')
    return all


def searchBigFile(source):

    all = {}
    import os
    for dir, subdirs, files in os.walk(source):
        for file in files:
            path = os.path.join(dir, file)
            print(os.path.getsize(path))
            if (os.path.getsize(path) > 1024 * 1024):
                all[path] = str(os.path.getsize(path)/(1024*1024) // 1) + 'MB'
    print('Done.')
    return all


if __name__ == '__main__':
    print(sys.argv)
    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv[2])
    print(sys.argv[3])
    # all = searchExt(sys.argv[1], sys.argv[2], sys.argv[3])
    all = searchBigFile(sys.argv[2])
    print(all)
    print('-------start-----------')
    for i in all:
        print('--------' + i)
    print('-------end----------')
