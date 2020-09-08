#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/9/8 18:07
# @Author: yuzq
# @File  : TestStocks
import csv
import pprint
from collections import namedtuple


def traverse1():
    print('------------我是方法分界线起始---------------')
    with open('stocks.csv') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            # Process row
            pprint.pprint(row)
            print(row[2])

    print('------------我是方法分界线终止---------------')


def traverse2():
    print('------------我是方法分界线起始---------------')
    with open('stocks.csv') as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        Row = namedtuple('Row', headings)
        for r in f_csv:
            row = Row(*r)
            # Process row
            pprint.pprint(row)
            print(row.Price)
    print('------------我是方法分界线终止---------------')


def traverse3():
    print('------------我是方法分界线起始---------------')
    with open('stocks.csv') as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            # process row
            pprint.pprint(row)
            print(row['Symbol'])
    print('------------我是方法分界线终止---------------')


def write1():
    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
            ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
            ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
            ]

    with open('stocks2.csv', 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)


def write2():
    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    rows = [{'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007',
             'Time': '9:36am', 'Change': -0.18, 'Volume': 181800},
            {'Symbol': 'AIG', 'Price': 71.38, 'Date': '6/11/2007',
             'Time': '9:36am', 'Change': -0.15, 'Volume': 195500},
            {'Symbol': 'AXP', 'Price': 62.58, 'Date': '6/11/2007',
             'Time': '9:36am', 'Change': -0.46, 'Volume': 935000},
            ]

    with open('stocks.csv', 'w') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(rows)


if __name__ == '__main__':
    # write1()
    write2()
    # traverse1()
    # traverse2()
    traverse3()
