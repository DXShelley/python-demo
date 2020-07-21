#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/7/20 16:40
# @Author: yuzq
# @File  : TemplateFile
import logging
import os
import pathlib

import libpath as libpath

if __name__ == '__main__':
    import tempfile

    fp = tempfile.TemporaryFile()
    fp.write(b'Hello world!')

    logging.warning(fp.seek(0))
    logging.warning(fp.read())

    fp.close()

    with tempfile.TemporaryFile() as fp:
        fp.write(b'Hello world!')
        logging.warning(fp.seek(0))
        logging.warning(fp.read())



    with tempfile.TemporaryDirectory() as tmpdirname:
        print('created temporary directory', tmpdirname)

    import linecache

    logging.warning(linecache.getline(linecache.__file__, 8))