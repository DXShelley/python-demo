#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/8/13 20:35
# @Author: yuzq
# @File  : Debugg

def error_file():
    import traceback
    import logging
    logging.basicConfig(filename='myProgramLog.txt', level=logging.INFO, format=' %(asctime)s - %(levelname)s -   %(message)s')
    try:
        raise Exception('This is the error message.')
    except:
        error_file = open('errorInfo.txt', 'w')
        error_file.write(traceback.format_exc())
        error_file.close()

        print('The traceback info was written to errorInfo.txt.')
        logging.info('The traceback info was written to errorInfo.txt. by logging')
        logging.critical('Critical error!')
        logging.critical('Critical error2!')
        logging.error('error1')
        logging.disable(logging.CRITICAL)
        logging.critical('Critical error3!')
        logging.error('error2')
        logging.info('info')


if __name__ == '__main__':
    error_file()
