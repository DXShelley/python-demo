#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/9/9 21:08
# @Author: yuzq
# @File  : threadDemo
import threading
import time


def threadDemo():
    time.sleep(5)
    print('Wake up!')


if __name__ == '__main__':
    print('Start of program.')
    thread = threading.Thread(target=threadDemo)
    thread.start()
    print('End of program.')
