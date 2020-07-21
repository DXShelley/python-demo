#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/7/20 16:59
# @Author: yuzq
# @File  : CopyFile
import os
import shutil
from shutil import copy2, Error, copystat


def copytree(src, dst, symlinks=False):
    names = os.listdir(src)
    os.makedirs(dst)
    errors = []
    for name in names:
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if symlinks and os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)
            elif os.path.isdir(srcname):
                copytree(srcname, dstname, symlinks)
            else:
                copy2(srcname, dstname)
            # XXX What about devices, sockets etc.?
        except OSError as why:
            errors.append((srcname, dstname, str(why)))
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except Error as err:
            errors.extend(err.args[0])
    try:
        copystat(src, dst)
    except OSError as why:
        # can't copy file access times on Windows
        if why.winerror is None:
            errors.extend((src, dst, str(why)))
    if errors:
        raise Error(errors)

if __name__ == '__main__':
    copytree("E:\\RDJ-YUZHENQUAN\\Desktop\\linshi\\201\\16\\settlement","E:\\RDJ-YUZHENQUAN\\Desktop\\linshi\\201\\16\\settlement2")
