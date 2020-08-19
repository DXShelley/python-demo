#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/8/4 20:33
# @Author: yuzq
# @File  : ZipFile


if __name__ == '__main__':
    import zipfile ,os
    example_file = zipfile.ZipFile("E:\\sunway\\temp\\补丁发版\\288补.zip")
    print(example_file.namelist())
    spam_info = example_file.getinfo('CasicDestroyContractActivitiProcessService.class')
    print((spam_info.file_size))
    print((spam_info.compress_size))

    # example_file.extract('CasicDestroyContractActivitiProcessService.class')
    # example_file.extractall()
    example_file.extract('CasicDestroyContractActivitiProcessService.class','./extractdir')
    example_file.close()

    example_file2 = zipfile.ZipFile('new.zip','w')
    example_file2.write('./capitalsquiz1.txt',compress_type=zipfile.ZIP_DEFLATED)
    example_file2.write('./capitalsquiz2.txt',compress_type=zipfile.ZIP_DEFLATED)
    example_file2.close()