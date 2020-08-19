#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/8/4 20:49
# @Author: yuzq
# @File  : renameDates
import os
import sys
import zipfile
from pathlib import Path


def rename_dates():
    import re, shutil, os

    datePattern = re.compile(r"""^(.*?)  # all text before the date
     ((0|1)?\d)-     # one or two digits for the month
     ((0|1|2|3)?\d)-   # one or two digits for the day
     ((19|20)\d\d)    # four digits for the year
     (.*?)$      # all text after the date
     """, re.VERBOSE)

    # datePattern = re.compile(r"""^(.* ?)  # all text before the date
    # ((0|1)?\d)-  # one or two digits for the month
    # ((0|1|2|3)?\d)-  # one or two digits for the day
    # ((19|20) \d\d)  # four digits for the year
    # (.*?)$  # all text after the date
    # """, re.VERBOSE)
    # TODO: Loop over the files in the working directory.
    for dirs, subdirs, filenames in os.walk('./'):
        path = ''
        for dir in dirs:
            pass
        for subdir in subdirs:
            pass
        for filename in filenames:
            amerFilename = os.path.join(dirs, filename)

            # TODO: Skip files without a date.
            mo = datePattern.search(amerFilename)
            if (mo == None):
                continue

            # TODO: Get the different parts of the filename.
            beforePart = mo.group(1)
            monthPart = mo.group(2)
            dayPart = mo.group(4)
            yearPart = mo.group(6)
            afterPart = mo.group(8)

            euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

            print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
            shutil.move(amerFilename, euroFilename)


def backupToZip(folder, target):
    # 创建zip文件
    folder = os.path.abspath(folder)  # make sure folder is absolute
    number = 1
    while True:
        zip_file_name = os.path.join(target, os.path.basename(folder) + '_' + str(number) + '.zip')
        if not os.path.exists(zip_file_name):
            break
        number += 1
    print('Creating %s...' % zip_file_name)
    backup_zip = zipfile.ZipFile(zip_file_name, 'w')
    print('done.')

    # 遍历目录，并压缩到zip文件中
    for dirs, subdirs, filenames in os.walk(folder):
        print('Adding files in %s...' % (dirs))
        for subdir in subdirs:
            print('Adding files in %s...' % (os.path.join(dirs, subdir)))
        for filename in filenames:
            # 不重复归档归档文件
            newbase = os.path.basename(folder) + '_'
            if str(filename).startswith(newbase) and str(filename).endswith('.zip'):
                continue
            backup_zip.write(os.path.join(dirs, filename))
    backup_zip.close()
    print('Backup Done.')


if __name__ == '__main__':
    # rename_dates()
    backupToZip(sys.argv[1], sys.argv[2])
