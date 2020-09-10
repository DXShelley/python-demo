#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/9/9 19:48
# @Author: yuzq
# @File  : TestDateTime
import datetime
import time

if __name__ == '__main__':
    now = datetime.datetime.now()
    print(now)
    print(datetime.time.second)
    print(datetime.datetime.time(now))
    print(now.time())
    print(now.year)
    print(now.month)
    print(now.day)

    print(f'{now.hour}:{now.minute}:{now.second}')
    print(time.time())
    print(datetime.datetime.fromtimestamp(time.time()))

    timedelta = datetime.timedelta(days=11,seconds=120,microseconds=360)
    print(timedelta.days)
    print(timedelta.seconds)
    print(timedelta.microseconds)
    print(timedelta.total_seconds())
    print(now + timedelta)
    print(now.strftime('%Y-%m-%d %H:%M:%S'))
    print(datetime.datetime.strptime('2015/10/21 16:29:00','%Y/%m/%d %H:%M:%S'))

