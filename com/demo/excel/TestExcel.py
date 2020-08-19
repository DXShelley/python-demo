#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/8/14 10:41
# @Author: yuzq
# @File  : TestExcel
import os
import sys

if __name__ == '__main__':
    print(os.getcwd())
    print( os.path.abspath('.'))
    print(sys.path[0])
    print(os.path.abspath('/'))

    book_dir = r'E:\lang\python\demo\com\books\Automate_the_Boring_Stuff_onlinematerials-master'
    file_path = os.path.join(book_dir,'example.xlsx')
    print(os.listdir(book_dir))
    print(os.path.join(book_dir,'example.xlsx'))

    import openpyxl as excel

    workbook = excel.load_workbook(file_path)
    print(type(workbook.get_sheet_names))
    print(workbook.get_sheet_names())
    print(workbook.active)
    print(type(workbook.active))
    print(workbook.active.active_cell)
    print(workbook['Sheet2'])
    sheet1 = workbook.get_sheet_by_name('Sheet1')  # type:excel.workbook.workbook.Worksheet
    print(sheet1)
    cell = sheet1['A2']

    print(type(cell))
    print(cell.value)
    print(cell.row)
    print(cell.column)
    print(cell.coordinate)


    cell1 = sheet1['A1']

    sheet2 = workbook['Sheet2']
    print(sheet2)
