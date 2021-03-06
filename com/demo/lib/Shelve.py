#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/8/4 8:36
# @Author: yuzq
# @File  : Shelve

import shelve


def test_shelve():
    # open 返回一个Shelf类的实例
    #
    # 参数flag的取值范围：
    #  'r'：只读打开
    #  'w'：读写访问
    #  'c'：读写访问，如果不存在则创建
    #  'n'：读写访问，总是创建新的、空的数据库文件
    #
    # protocol：与pickle库一致
    # writeback：为True时，当数据发生变化会回写，不过会导致内存开销比较大
    d = shelve.open('shelve.db', flag='c', protocol=2, writeback=False)
    assert isinstance(d, shelve.Shelf)
    print(str( isinstance(d, shelve.Shelf)))

    # 在数据库中插入一条记录
    d['abc'] = {'name': ['a', 'b']}
    d.sync()

    print(d['abc'])

    # writeback是False，因此对value进行修改是不起作用的
    d['abc']['x'] = 'x'
    print(d['abc'])  # 还是打印 {'name': ['a', 'b']}

    # 当然，直接替换key的value还是起作用的
    d['abc'] = 'xxx'
    print(d['abc'])

    # 还原abc的内容，为下面的测试代码做准备
    d['abc'] = {'name': ['a', 'b']}
    d.close()

    # writeback 为 True 时，对字段内容的修改会writeback到数据库中。
    d = shelve.open('shelve.db', writeback=True)

    # 上面我们已经保存了abc的内容为{'name': ['a', 'b']}，打印一下看看对不对
    print(d['abc'])

    # 修改abc的value的部分内容
    d['abc']['xx'] = 'xxx'
    print(d['abc'])
    d.close()

    # 重新打开数据库，看看abc的内容是否正确writeback
    d = shelve.open('shelve.db')
    print(d['abc'])
    d.close()


if __name__ == '__main__':
    test_shelve()
