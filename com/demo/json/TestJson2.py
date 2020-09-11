#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/9/8 20:57
# @Author: yuzq
# @File  : TestJson2
import json
from collections import OrderedDict

'''
JSON编码支持的基本数据类型为 None ， bool ， int ， float 和 str ， 以及包含这些类型数据的lists，tuples和dictionaries。 
对于dictionaries，keys需要是字符串类型(字典中任何非字符串类型的key在编码时会先转换为字符串)。 为了遵循JSON规范，你应该只编码Python的lists和dictionaries。 
而且，在web应用程序中，顶层对象被编码为一个字典是一个标准做法。

'''


def parse_json_str():
    data = {
        'name': 'ACME',
        'shares': 100,
        'price': 542.23
    }
    # obj转json字符串
    json_str = json.dumps(data, indent=2)
    print(json_str)


def write_or_read_json_file():
    data = {
        'name': 'ACME',
        'shares': 100,
        'price': 542.23
    }
    # Writing JSON data
    with open('data.json', 'w') as f:
        json.dump(data, f)

    # Reading data back
    with open('data.json', 'r') as f:
        data2 = json.load(f)
        print(data)


# json字符串转特定对象
def json_str_to_obj():
    s = '{"name": "ACME", "shares": 50, "price": 490.1}'
    data = json.loads(s, object_pairs_hook=OrderedDict)
    print(data)

    data2 = json.loads(s, object_hook=JSONObject)
    print(data2.name)


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

'''
对象实例通常并不是JSON可序列化的.
如果你想序列化对象实例，你可以提供一个函数，它的输入是一个实例，返回一个可序列化的字典
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def serialize_instance(obj):
    d = { '__classname__' : type(obj).__name__ }
    d.update(vars(obj))
    return d
def unserialize_object(d):
    # Dictionary mapping names to known classes
    classes = {
        'Point': Point
    }
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls) # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d

def test_serialize():
    p = Point(2, 3)
    s = json.dumps(p, default=serialize_instance)
    print(s)
    a = json.loads(s, object_hook=unserialize_object)
    print(a)
    print(a.x)
    print(a.y)

if __name__ == '__main__':
    # parse_json_str()
    # write_or_read_json_file()
    # json_str_to_obj()
    test_serialize()
