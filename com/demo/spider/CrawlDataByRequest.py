#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/7/22 9:44
# @Author: yuzq
# @File  : CrawlDataByRequest


# if __name__ == '__main__':
#
#
#     import requests        #导入requests包
#     url = 'http://www.cntour.cn/'
#     strhtml = requests.get(url)        #Get方式获取网页数据
#     print(strhtml.text)
#
#     import requests  # 导入requests包
#     import json
import json
from urllib import request

import pymysql
import requests
from lxml import etree


def get_translate_date(word=None):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    From_data = {'i': word, 'from': 'zh-CHS', 'to': 'en', 'smartresult': 'dict', 'client': 'fanyideskweb',
                 'salt': '15477056211258', 'sign': 'b3589f32c38bc9e3876a570b8a992604', 'ts': '1547705621125',
                 'bv': 'b33a2f3f9d09bde064c9275bcb33d94e', 'doctype': 'json', 'version': '2.1',
                 'keyfrom': 'fanyi.web', 'action': 'FY_BY_REALTIME', 'typoResult': 'false'}
    # 请求表单数据
    response = requests.post(url, data=From_data)
    # 将Json格式字符串转字典
    content = json.loads(response.text)
    print(content)
    # 打印翻译后的数据
    # print(content['translateResult'][0][0]['tgt'])


def get_by_soup():
    import requests  # 导入requests包
    from bs4 import BeautifulSoup
    url = 'http://www.cntour.cn/'
    strhtml = requests.get(url)
    soup = BeautifulSoup(strhtml.text, 'lxml')
    data = soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')
    print(data)
    import re
    for item in data:
        result = {
            "title": item.get_text(),
            "link": item.get('href'),
            'ID': re.findall('\d+', item.get('href'))
        }
    print(result)


def get_data():
    req_csdn = request.Request('https://blog.csdn.net/meteor_93')
    req_csdn.add_header('User-Agent',
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')
    html_csdn = request.urlopen(req_csdn).read().decode('utf-8')
    # print(html_csdn)
    #

    read_num_csdn = etree.HTML(html_csdn).xpath('//*[@id="asideProfile"]/div[2]/dl[1]/dt/a/span/text()')[0]

    # print(read_num_csdn)
    fans_num_csdn = etree.HTML(html_csdn).xpath('//*[@id="fan"]/text()')[0]
    rank_num_csdn = etree.HTML(html_csdn).xpath('//*[@id="asideProfile"]/div[4]/dl[5]/@title')[0]
    like_num_csdn = etree.HTML(html_csdn).xpath('//*[@id="asideProfile"]/div[2]/dl[3]/dt/span/text()')[0]
    print(read_num_csdn, fans_num_csdn, rank_num_csdn, like_num_csdn)
    connection = connect()

    conn, cursor = connection['conn'], connection['cursor']
    csdn_data = {
        "plantform": 'csdn',
        "read_num": read_num_csdn,
        "fans_num": fans_num_csdn,
        "rank_num": rank_num_csdn,
        "like_num": like_num_csdn
    }
    sql_insert = "insert into spider_data(id, plantform, read_num, fans_num, rank_num, like_num, create_date) values (UUID(), %(plantform)s, %(read_num)s, %(fans_num)s, %(rank_num)s, %(like_num)s, now())"
    # cursor.execute('SET NAMES utf8;')  #使用游标设置
    cursor.execute(sql_insert, csdn_data)
    conn.commit()
    conn.close()


def connect():
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='lims_emc_dev',
                           password='lims_emc_$dev',
                           database='emc_dev',
                           charset='utf8mb4')
    # conn.set_charset('utf8')
    # 获取操作游标
    cursor = conn.cursor()
    return {"conn": conn, "cursor": cursor}


if __name__ == '__main__':
    # get_translate_date('我爱中国')
    # get_by_soup()
    get_data()
