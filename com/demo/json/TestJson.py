#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/9/7 22:26
# @Author: yuzq
# @File  : TestJson
import json

if __name__ == '__main__':
    stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
    print(stringOfJsonData)
    jsondata_as_pythonvalue = json.loads(stringOfJsonData)
    print(jsondata_as_pythonvalue)

    json_data = json.dumps(jsondata_as_pythonvalue)
    print(json_data)

