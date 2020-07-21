#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/7/20 16:32
# @Author: yuzq
# @File  : dirCompare
from filecmp import dircmp


def print_diff_files(dcmp):
    for name in dcmp.diff_files:
        print("diff_file %s found in %s and %s" % (name, dcmp.left,
                                                   dcmp.right))
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files(sub_dcmp)



if __name__ == '__main__':
    dcmp = dircmp("E:\\RDJ-YUZHENQUAN\\Desktop\\linshi\\201\\16\\settlement\\service",
                  "E:\\RDJ-YUZHENQUAN\\Desktop\\linshi\\201\\16\\settlement")
    print_diff_files(dcmp)
