#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/7/29 16:22
# @Author: yuzq
# @File  : TestDic

def dic():
    birthdays = {'alice':18,'bob':22,'yuzq':24}
    while True:
        print('enter a name:(blank to quit)')
        name = input()
        if name == '':
            break;
        if name in birthdays:
            print(str(birthdays[name]) + ' is birthdays of ' + name)
        else:
            print('no birthday information')
            print('what is birthdays of you?')
            birthday = int(input())
            birthdays[name] = birthday
            print('birthday add sucess')


def dic2():
    birthdays = {'alice': 18, 'bob': 22, 'yuzq': 24}
    print(type(birthdays.items()))
    print(type(birthdays.keys()))
    print(type(birthdays.values()))

    for item in birthdays.items():
        print(type(item))
        print(item[0])
        print(item[1])

    print('-------------------------------------')
    for k,v in birthdays.items():
        print(type(k))
        print(type(v))
        print(str(k) + ' = ' + str(v),sep=',')
    print('-------------------------------------')
    for key in birthdays.keys():
        print(type(key))
        print(key)
    print('-------------------------------------')
    for value in birthdays.values():
        print(type(value))
        print(value)

def dic3():
    import pprint
    message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
    count = {}
    for character in message:
        count.setdefault(character,0)
        count[character] = count[character] + 1
    pprint.pprint(count)

if __name__ == '__main__':
    # dic()
    # dic2()
    dic3()
