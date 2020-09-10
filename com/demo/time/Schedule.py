#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/9/9 16:33
# @Author: yuzq
# @File  : MonitorSystem


# logfile：监测信息写入文件
import datetime
import time
from threading import Timer

import psutil as psutil
import schedule as schedule
from apscheduler.schedulers.blocking import BlockingScheduler

'''
1：循环+sleep方式适合简答测试，
2：timer可以实现定时任务，但是对定点任务来说，需要检查当前时间点；
3：schedule可以定点定时执行，但是需要在循环中检测任务，而且存在阻塞；
4：APScheduler框架更加强大，可以直接在里面添加定点与定时任务；
综合考虑，决定使用APScheduler框架，实现简单，只需要直接创建任务，并将添加到调度器中即可'''


def MonitorSystem(logfile=None):
    # 获取cpu使用情况
    cpuper = psutil.cpu_percent()
    # 获取内存使用情况：系统内存大小，使用内存，有效内存，内存使用率
    mem = psutil.virtual_memory()
    # 内存使用率
    memper = mem.percent
    # 获取当前时间
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    line = f'{ts} cpu:{cpuper}%, mem:{memper}%'
    print(line)
    if logfile:
        logfile.write(line)
    Timer(3, MonitorSystem).start()


def MonitorNetWork(logfile=None):
    # 获取网络收信息
    netinfo = psutil.net_io_counters()
    # 获取当前时间
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    line = f'{ts} bytessent={netinfo.bytes_sent}, bytesrecv={netinfo.bytes_recv}'
    print(line)
    if logfile:
        logfile.write(line)
    Timer(3, MonitorNetWork).start()


# 这种方式最简单，直接使用while+sleep就可以实现
def loopMonitor():
    while True:
        MonitorSystem()
        MonitorNetWork()
        # 2s检查一次
        time.sleep(3)


# timer最基本理解就是定时器，我们可以启动多个定时任务，这些定时器任务是异步执行，所以不存在等待顺序执行问题。
def timer():
    # 记录当前时间
    print(datetime.datetime.now())
    # 3S执行一次
    sTimer = Timer(3, MonitorSystem)
    # 1S执行一次
    nTimer = Timer(1, MonitorNetWork)
    # 使用线程方式执行
    sTimer.start()
    nTimer.start()
    # 等待结束
    sTimer.join()
    nTimer.join()
    # 记录结束时间
    print(datetime.datetime.now())


def func():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func  time :', ts)


def func2():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func2 time：', ts)
    time.sleep(2)


def tasklist():
    # 清空任务
    schedule.clear()
    # 创建一个按秒间隔执行任务
    schedule.every(1).seconds.do(func)
    # 创建一个按2秒间隔执行任务
    schedule.every(2).seconds.do(func2)
    # 执行10S
    for i in range(10):
        schedule.run_pending()
        time.sleep(1)


def dojob():
    # 创建调度器：BlockingScheduler
    scheduler = BlockingScheduler()
    # 添加任务,时间间隔2S
    scheduler.add_job(func, 'interval', seconds=2, id='test_job1')
    # 添加任务,时间间隔5S
    scheduler.add_job(func2, 'interval', seconds=3, id='test_job2')
    scheduler.start()


if __name__ == '__main__':
    # loopMonitor()
    # timer()
    # MonitorSystem()
    # MonitorNetWork()
    # tasklist()
    dojob()
