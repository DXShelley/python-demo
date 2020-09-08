#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/9/7 19:25
# @Author: yuzq
# @File  : TestCsv
import csv
from _csv import Dialect


def read_csv(filepath):
    file = open(filepath)
    # Reader 对象只能循环遍历一次。要再次读取 CSV 文件，必须调用 csv.reader，创 建一个对象
    reader = csv.reader(file)

    print(reader)
    # list方法已经遍历过一遍了，所以后续遍历没有值了。
    # example_data = list(reader)
    # print(example_data)
    # print(example_data[1][1])
    # 要注意的是，reader只能被遍历一次。由于reader是可迭代对象，可以使用next方法一次获取一行。
    for row in reader:
        print('Row #:' + str(reader.line_num) + '  ' + str(row))
    file.close()


def print_dialects():
    names = csv.list_dialects()
    print(names)
    for name in names:
        print(type(name))
        print(name)
        dialect = csv.get_dialect(name)
        print(type(dialect))
        print(repr(dialect.delimiter), end=" ")
        print(dialect.doublequote, end=" ")
        print(dialect.escapechar, end=" ")
        print(repr(dialect.lineterminator), end=" ")
        print(dialect.quotechar, end=" ")
        print(dialect.quoting, end=" ")
        print(dialect.skipinitialspace, end=" ")
        print(dialect.strict)


def write_csv(li, file):
    # 在 Windows 上，需要为 open()函数的 newline 关键字参数传入一个空字符串。如果忘记设置 newline 关键字参数，output.csv 中的行距将有两倍
    # file = open(file, 'a', newline='')
    file = open(file, 'w', newline='')

    csv.register_dialect('mydialect', delimiter='#', lineterminator='\n\n\n')

    # writer = csv.writer(file,delimiter='@')
    # writer = csv.writer(file, dialect='mydialect')
    writer = csv.writer(file, dialect='excel-tab')
    writer.writerows(li)
    file.close()


if __name__ == '__main__':
    file_path = 'example.csv'
    list = [[1, 2, 3, 4], [5, 6, 7, 'hello,world']]

    # print_dialects()

    write_csv(list, 'example3.csv')

    read_csv('example3.csv')
