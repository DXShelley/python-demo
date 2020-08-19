#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/8/19 9:55
# @Author: yuzq
# @File  : DownImageByRequests
import logging
import os
import traceback
import uuid
from pathlib import Path

import bs4
import requests

logging.basicConfig(level=logging.DEBUG)


def get_html_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36A'
    }
    response = requests.get(url, headers=headers)

    content = ''
    try:
        response.raise_for_status()
        if response.status_code == requests.codes.ok:
            content = response.text
    except Exception as ex:
        logging.debug('下载页面失败\n' + traceback.format_exc())
    return content


def get_html_elements(text, selectors):
    try:
        soup = bs4.BeautifulSoup(text, features='lxml')
        tags = soup.select(selectors)
    except Exception as ex:
        logging.debug('获取页面指定元素失败\n' + traceback.format_exc())
    return tags


def download_image(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        }
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        if res.status_code == requests.codes.ok:
            target_dir = Path(os.path.curdir).joinpath('bingImage1')
            target_file = target_dir.joinpath(os.path.basename(url))
            logging.debug('-- 文件路径 -- ' + str(target_file.resolve()))
            with open(target_file, 'wb') as image:
                for chunk in res.iter_content(100000):
                    image.write(chunk)
        else:
            logging.debug('请求失败，http响应码为： ' + res.status_code)
    except Exception as ex:
        logging.debug('下载图片失败\n' + traceback.format_exc())


def get_images():
    root_url = 'https://bing.ioliu.cn'
    url = 'https://bing.ioliu.cn/?p=136'
    logging.debug('正在下载图片。。。')
    try:
        while url != 'https://bing.ioliu.cn/':
            html = get_html_content(url)
            elements = get_html_elements(html, 'div.container .item .download')
            elements.reverse()
            for ele in elements:
                download_image(root_url + (ele.get('href')))
            pre = get_html_elements(html, 'body > div.page > a:nth-child(1)')
            if len(pre) > 0:
                url = root_url + pre[0].get('href')
            else:
                url = 'https://bing.ioliu.cn/'

    except:
        logging.debug('图片下载失败\n' + traceback.format_exc())
    logging.debug('所有页面图片下载完成!')


if __name__ == '__main__':
    get_images()
    url = 'https://bing.ioliu.cn/?p=136'
    html = get_html_content(url)
    # logging.debug(html)
    # elements = get_html_elements(html, 'div.container .item .download')
    # logging.debug(elements)
    # logging.debug(len(elements))
