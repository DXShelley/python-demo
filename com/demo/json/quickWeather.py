#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/9/7 22:40
# @Author: yuzq
# @File  : quickWeather
import json
import pprint
import sys

import requests

if __name__ == '__main__':
    # 1.从命令行读取请求的位置，命令行参数以空格分隔
    if len(sys.argv) < 2:
        print('Usage : quickWeather.py location')
        sys.exit()
    location = ' '.join(sys.argv[1:])  # 命令行参数存在列表里是没有空格的，此处用空格来拼接它们
    print(location)

    # 2.下载JSON数据
    url = 'http://wthrcdn.etouch.cn/weather_mini?city=%s' % (location)
    response = requests.get(url)
    response.raise_for_status()
    pprint.pprint(response.text)

    weatherData = json.loads(response.text)  # 观察json数据格式后发现温度存在在data的wendu中
    pprint.pprint(weatherData)
    w = weatherData['data']
    pprint.pprint(w)
    pprint.pprint(w['wendu'])