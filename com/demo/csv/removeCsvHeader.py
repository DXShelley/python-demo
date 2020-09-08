#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/9/7 21:52
# @Author: yuzq
# @File  : removeCsvHeader.py
import csv
import os

if __name__ == '__main__':
    print('Removing start.')
    os.makedirs('headerRemoved', exist_ok=True)
    present_dir = os.getcwd()

    for csv_filename in os.listdir('.'):
        if not csv_filename.endswith('.csv'):
            continue

        print('Removing header from ' + csv_filename + '...')
        li = []
        with open(os.path.join(present_dir, csv_filename), 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if reader.line_num == 1:
                    continue
                li.append(row)

        target_file = os.path.join(present_dir, 'headerRemoved', csv_filename)
        with open(target_file, 'w', newline='') as f:
            writer = csv.writer(f, delimiter='#')
            writer.writerows(li)
        print('Removed header from ' + csv_filename + ' Done.')
    print('Removing end.')
