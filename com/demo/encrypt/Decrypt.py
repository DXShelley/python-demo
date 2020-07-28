#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/7/24 9:11
# @Author: yuzq
# @File  : Decrypt
import os
import sys
import zipfile
from pathlib import Path

import rarfile as rar_file


def decrypt_rar_or_zip_file(file_name, dest_path):
    # 根据文件扩展名，使用不同的库
    if file_name.endswith('.zip'):
        fp = zipfile.ZipFile(file_name)
    elif file_name.endswith('.rar'):
        fp = rar_file.RarFile(file_name)

    print(fp.infolist())

    try:
        fp.extractall(dest_path)
        fp.close()
        print("解压成功！")
    except:
        try:
            # 读取密码本文件
            path = Path(os.getcwd())
            fpPwd = path.joinpath('passwd.txt').open('r')
            # fpPwd = open('password.txt')
        except:
            print('No dict file pwd.txt in current directory.')
            return
        for pwd in fpPwd:
            pwd = pwd.rstrip()
            try:
                fp.extractall(path=dest_path, pwd=pwd.encode())
                print('Success! ====>' + pwd)
                print("解压成功！")
                fp.close()
                break
            except:
                print("解压失败！")
        fpPwd.close()


if __name__ == '__main__':
    filename = sys.argv[1]
    destPath = sys.argv[2]
    if os.path.isfile(filename) and filename.endswith(('.zip', '.rar')):
        decrypt_rar_or_zip_file(filename, destPath)
    else:
        print('Must be Rar or Zip file')
