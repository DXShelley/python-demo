#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/8/19 14:22
# @Author: yuzq
# @File  : TestSelenium
import logging

from selenium import webdriver

logging.basicConfig(level=logging.DEBUG)
if __name__ == '__main__':
    firefox = webdriver.Firefox()
    logging.debug('--驱动类型---' + str(type(firefox)))
    # firefox.get('http://localhost:9090')
    firefox.get('http://inventwithpython.com')
    try:
        elem = firefox.find_element_by_class_name('display-3')
        print('Found <%s> element with that class name!' % (elem.tag_name))
    except:
        print('Was not able to find an element with that name.')
