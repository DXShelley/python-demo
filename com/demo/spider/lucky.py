#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/8/18 19:48
# @Author: yuzq
# @File  : lucky.py
import sys
import webbrowser

import bs4
import requests

if __name__ == '__main__':
    print('Baiduing...')
    url = 'https://www.baidu.com/s?wd=' + ' '.join(sys.argv[1:])
    print(url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    # print(res.text)
    soup = bs4.BeautifulSoup(res.text, features='lxml')

    select = soup.select('#content_left > div > h3 > a')
    # print(select)

    #巧妙用法
    num_open = min(5, len(select))
    for i in range(num_open):
        webbrowser.open(select[i].get('href'))
