#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/9/2 11:17
# @Author: yuzq
# @File  : Excel2Txt
import openpyxl


def write2txt(li, path):
    with open(path, 'w') as f:
        for item in li:
            f.writelines(str(item) + '\n')


if __name__ == '__main__':
    wb = openpyxl.load_workbook('produceSales.xlsx', data_only=True)
    sheet = wb.active

    for colobj in sheet.iter_cols():
        write2txt([col.value for col in list(colobj)], colobj[0].value + '.txt')

    wb.close()
