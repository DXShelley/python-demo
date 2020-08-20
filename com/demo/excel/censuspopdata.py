#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/8/20 19:28
# @Author: yuzq
# @File  : censuspopdata
import logging
import os

import openpyxl, pprint

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    logging.info('Opening workbook...')
    book_dir = r'E:\lang\python\demo\com\books\Automate_the_Boring_Stuff_onlinematerials-master'
    file_path = os.path.join(book_dir, 'censuspopdata.xlsx')
    wb = openpyxl.load_workbook(file_path)
    # sheet = wb.get_sheet_by_name('Population by Census Tract')  # type: openpyxl.worksheet.worksheet.Worksheet
    sheet = wb.active  # type: openpyxl.worksheet.worksheet.Worksheet
    countyData = {}

    logging.info('Reading rows...')

    for row in range(2, sheet.max_row + 1):
        state = sheet['B' + str(row)].value
        county = sheet['C' + str(row)].value
        pop = sheet['D' + str(row)].value
        countyData.setdefault(state, {})
        countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
        countyData[state][county]['tracts'] += 1
        countyData[state][county]['pop'] += int(pop)

    logging.info('Writing results...')
    resultFile = open('census2010.py', 'w')
    resultFile.write('allData = ' + pprint.pformat(countyData))
    resultFile.close()
    logging.info('Done.')

