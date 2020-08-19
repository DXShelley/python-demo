#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/8/19 11:28
# @Author: yuzq
# @File  : getHeadersOrCookies

def get_headers(header_raw):
    """
    通过原生请求头获取请求头字典
    :param header_raw: {str} 浏览器请求头
    :return: {dict} headers
    """
    return dict(line.split(": ", 1) for line in header_raw.split("\n") if line != '')


def get_cookies(cookie_raw):
    """
    通过原生cookie获取cookie字段
    :param cookie_raw: {str} 浏览器原始cookie
    :return: {dict} cookies
    """
    return dict(line.split("=", 1) for line in cookie_raw.split("; "))


if __name__ == '__main__':
    header_raw = """Host: bing.ioliu.cn
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cookie: Hm_lvt_667639aad0d4654c92786a241a486361=1597800805; _ga=GA1.2.2067265767.1597800806; _gid=GA1.2.1367673174.1597800806; likes=; Hm_lpvt_667639aad0d4654c92786a241a486361=1597803960"""
    header_json = get_headers(header_raw)
    print(header_json)