#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/8/19 9:55
# @Author: yuzq
# @File  : DownImageByRequests
import logging
import os
import random
import re
import shelve
import traceback
import uuid
from pathlib import Path

import bs4
import requests

logging.basicConfig(level=logging.DEBUG)


def get_html_content(url):
    proxy_list = {
        'http': '114.103.104.113:4216',
        'http': '114.239.171.181:4216',
        'http': '89.223.20.202:5836',

    }
    # 收集到的常用Header
    my_headers = [
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
        'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "]

    response = requests.get(url, headers={'User-Agent' : random.choice(my_headers)}, proxies=proxy_list,timeout=5)
    # response = requests.get(url, headers={'User-Agent' : random.choice(my_headers)},timeout=5)

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


def download_image(url, fname=None):
    try:
        proxy_list = {
            'http': '114.103.104.113:4216',
            'http': '114.239.171.181:4216',
            'http': '89.223.20.202:5836',

        }

        # 收集到的常用Header
        my_headers = [
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
            "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
            'Opera/9.25 (Windows NT 5.1; U; en)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
            'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
            'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
            "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
            "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "]

        res = requests.get(url, headers={'User-Agent' : random.choice(my_headers)},proxies=proxy_list,timeout=5)
        # res = requests.get(url, headers={'User-Agent' : random.choice(my_headers)},timeout=5)

        # ip_and_port = res.raw._connection.sock.getpeername()
        # logging.debug('代理ip： ' + str(ip_and_port))
        res.raise_for_status()
        if res.status_code == requests.codes.ok:
            target_dir = Path(os.path.curdir).joinpath('bingImage1')
            target_fname = str(uuid.uuid1())
            if fname != None:
                target_fname = validateTitle(fname)
            target_file = target_dir.joinpath(target_fname)
            logging.debug('-- 文件路径 -- ' + str(target_file.resolve()))
            with open(target_file, 'wb') as image:
                for chunk in res.iter_content(100000):
                    image.write(chunk)
        else:
            logging.debug('请求失败，http响应码为： ' + res.status_code)
    except Exception as ex:
        logging.debug('下载图片失败\n' + traceback.format_exc())


def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title


def get_images():
    root_url = 'https://bing.ioliu.cn'
    url = 'https://bing.ioliu.cn/?p=136'
    logging.debug('正在下载图片。。。')
    try:

        # 持久化文件记录，防止重复下载
        db = shelve.open('shelve.db', flag='c', protocol=2, writeback=False)

        while url != 'https://bing.ioliu.cn/':
            html = get_html_content(url)
            elements = get_html_elements(html, 'div.container .item')

            elements.reverse()
            for ele in elements:
                href = ele.contents[0].contents[3].contents[2].get('href')
                fname = ele.contents[0].contents[2].h3.string
                if fname not in db.keys():
                    download_image(root_url + href, fname + '.jpg')
                    db[fname] = '1'
            pre = get_html_elements(html, 'body > div.page > a:nth-child(1)')
            if len(pre) > 0:
                url = root_url + pre[0].get('href')
            else:
                url = 'https://bing.ioliu.cn/'
        logging.debug('所有页面图片下载完成!')
    except:
        logging.debug('图片下载失败\n' + traceback.format_exc())
    finally:
        db.close()

if __name__ == '__main__':
    get_images()
    url = 'https://bing.ioliu.cn/?p=136'
    html = get_html_content(url)
    # logging.debug(html)
    # elements = get_html_elements(html, 'div.container .item .download')
    # logging.debug(elements)
    # logging.debug(len(elements))
