#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/8/4 18:45
# @Author: yuzq
# @File  : multiclipboard


if __name__ == '__main__':
    import shelve,pyperclip,sys
    mcbshelf = shelve.open('mcb')
    # TODO: Save clipboard content.
    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        mcbshelf[sys.argv[2]] = pyperclip.paste()
    if len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
        mcbshelf[sys.argv[2]] = pyperclip.paste()
        mcbshelf.pop(sys.argv[2])

    # TODO: List keywords and load content.
    elif len(sys.argv) == 2:
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcbshelf.keys())))
        elif sys.argv[1].lower() == 'delete':
            mcbshelf.clear()
        elif sys.argv[1] in mcbshelf:
            pyperclip.copy(mcbshelf[sys.argv[1]])
    mcbshelf.close()


