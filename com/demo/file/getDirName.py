#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/9/4 13:39
# @Author: yuzq
# @File  : getDirName
from pathlib import Path

if __name__ == '__main__':
    path = Path(r'E:\RDJ-YUZHENQUAN\Downloads\EGDownloads\2020090400009')
    dirs = path.iterdir()

    list = []
    for dir in dirs:
        if(dir.is_dir()):
            list.append(dir.name)
    # print('\n'.join(list))


    error_list = []

    with open(r'D:\develop\Notepad++\aaa\tmp\errorData.txt','r',encoding='utf-8') as f:
        for line in f.readlines():
            error_list.append(line.strip('\n').strip(','))

    for line in list:
        if line in error_list:
            print(line)

    print(len(list) + len(error_list))
