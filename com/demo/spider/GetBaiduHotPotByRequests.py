#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/8/18 17:11
# @Author: yuzq
# @File  : GetBaiduHotPotByRequests
import logging

import requests

logging.basicConfig(level=logging.DEBUG)


def get_html(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    content = ''
    try:
        response.raise_for_status()
        if response.status_code == requests.codes.ok:
            content = response.text


    except Exception as ex:
        logging.debug('请求出错了' + str(ex))
    finally:
        pass
    logging.debug('Get Html done.')
    return content.encode(encoding='utf-8')


def get_html_ele(text):
    result = []
    import bs4
    soup = bs4.BeautifulSoup(text,features='lxml')
    tags = soup.select('#hotsearch-content-wrapper .title-content-title')
    # tags = soup.select('#node-2413 .cc-cd-cb-l .t')
    for tag in tags:
        result.append(tag.getText())
    logging.debug('get element from html done.')
    return result


def write_to_file(list):
    with open('hotpot.txt', 'w', encoding='utf-8') as f:
        for ele in list:
            f.writelines(ele + '\n')

    logging.debug('Write done.')
    pass


if __name__ == '__main__':
    url = 'https://www.baidu.com/'
    # url = 'https://tophub.today/c/finance'
    html = get_html(url)
    # logging.debug(html)
    elements = get_html_ele(html)
    # logging.debug(str(elements))
    write_to_file(elements)
    logging.debug("Done.")
