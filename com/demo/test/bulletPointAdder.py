#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/7/30 8:54
# @Author: yuzq
# @File  : bulletPointAdder


def bullet_point_adder():
    import pyperclip
    content = pyperclip.paste()
    lines = content.split('\n')
    for i in range(len(lines) - 1):
        lines[i] = '* ' + lines[i]

    content = '\n'.join(lines)
    pyperclip.copy(content)


if __name__ == '__main__':
    bullet_point_adder()
