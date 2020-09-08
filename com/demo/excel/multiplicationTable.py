#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/8/29 15:30
# @Author: yuzq
# @File  : multiplicationTable
from openpyxl.workbook import workbook

if __name__ == '__main__':

    # 创建工作簿和工作表
    wb = workbook.Workbook()
    sheet = wb.create_sheet('multiplicationTable', 0)

    # 生成数据结构
    multiplicationTable = []

    for row_index in range(1, 10):
        rows = []
        rows.append(row_index)
        for col_index in range(1, 10):
            rows.append(row_index * col_index)

        multiplicationTable.append(rows)

    # 充填表格
    l = list(range(1, 10))
    l.insert(0, '')
    print(l)
    sheet.append(l)
    for row_obj in multiplicationTable:
        sheet.append(row_obj)
    # 保存到文件
    wb.save('multiplicationTable.xlsx')
