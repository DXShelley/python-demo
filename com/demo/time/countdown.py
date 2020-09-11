#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/9/10 19:35
# @Author: yuzq
# @File  : countdown.py
import logging
import subprocess
import time

logging.basicConfig(level=logging.DEBUG)
if __name__ == '__main__':
    i = 60
    while i != 0:
        logging.debug(i)
        # print(i,end='')
        time.sleep(1)
        i = i -1
    subprocess.Popen(['start','alarm.wav'],shell=True)
