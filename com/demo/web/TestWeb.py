#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/8/13 20:57
# @Author: yuzq
# @File  : TestWeb

import logging

import bs4

logging.basicConfig(level=logging.INFO)


def test_webbrowser():
    import webbrowser
    webbrowser.open('http://localhost:9090')


def test_requests():
    import requests
    response = requests.get('http://localhost:10101/123')
    logging.info(type(response))
    logging.info(response.headers)
    logging.info(response.request.headers)

    try:
        response.raise_for_status()
        # 使用二进制模式，可以防止文件乱码
        fi = open('index.html','wb')
        for chunk in response.iter_content(100000):
            fi.write(chunk)
        fi.close()
        # 不使用二进制模式，会导致文件乱码
        fi2 = open('index2.html','w')
        fi2.write(response.text)
        fi2.close()

    except Exception as exc:
        logging.info('出大事了: %s' % (exc))

    if response.status_code == requests.codes.ok:
        logging.info('Request successed')
    logging.info(response.content)
    # logging.info(response.text)


def test_soup():
    import bs4
    example_file = open(' example.html')
    example_soup = bs4.BeautifulSoup(example_file.read())
    elems = example_soup.select('#author')
    logging.info(type(elems))
    logging.info(len(elems))
    logging.info(elems)
    logging.info(type(elems[0]))
    logging.info(elems[0])
    logging.info(str(elems[0]))
    logging.info(elems[0].attrs)
    logging.info(elems[0].get('id'))


if __name__ == '__main__':
    # test_webbrowser()
    test_requests()
    # test_soup()