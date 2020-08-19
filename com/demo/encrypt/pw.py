#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/7/29 19:12
# @Author: yuzq
# @File  : pw
import shelve

if __name__ == '__main__':
    pw_shelf = shelve.open('pw')
    import sys
    if len(sys.argv) < 2:
        print('Usage: python pw.py [account] - copy account password')
        sys.exit()

    account = sys.argv[1]
    if account in pw_shelf:
        import pyperclip
        pyperclip.copy(pw_shelf[account])
        print('Password for ' + account + ' copied to clipboard')

    else:
        print('There is no accmount named ' + account)
        print('If you want to add?')
        yesorno = input()
        if 'YES' == yesorno.upper() or 'Y' == yesorno.upper():
            print('Please enter password for this accmount')
            pwd = input()
            pw_shelf[account] = pwd
            print('Password updated for ' + account)
