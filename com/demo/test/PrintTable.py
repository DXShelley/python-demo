#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/7/30 9:08
# @Author: yuzq
# @File  : PrintTable


if __name__ == '__main__':
    tableData = [['apples', 'oranges', 'peach'], ['Alice', 'Bob', 'Carol', 'David', 'Tom'],
                 ['dogs', 'cats', 'moose']]

    '''
        记录每列字符串最大长度
        记录最大行数
    '''
    col_widths = [0] * len(tableData)
    row_max_size = 0
    for i in range(len(tableData)):
        width = 0
        size = 0
        for ins in tableData[i]:
            if len(ins) > width:
                width = len(ins)
            size += 1
        col_widths[i] = width
        if size > row_max_size:
            row_max_size = size

    for i in range(row_max_size):
        str = ''
        for j in range(len(tableData)):

            try:
                cell = tableData[j][i]
            except:
                cell = '-'
            finally:
                str += cell.rjust(col_widths[j])
                # str += cell.ljust(col_widths[j])
                str += ' ' * col_widths[j]
        print(str, end='\n')

    # for i in range(len(tableData)):
    #     # str = tableData[0][1]
    #     # str = tableData[1][1]
    #     # str = tableData[2][1]
    #     strs = ''
    #     for j in range(len(tableData[i])):
    #         strs += tableData[i][j]
    #     print(strs,end='\n')
    #
    # print(list(range(3)))
    # print(len(tableData))
