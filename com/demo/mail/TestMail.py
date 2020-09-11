#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/9/10 19:59
# @Author: yuzq
# @File  : TestMail
import imghdr
import logging
import smtplib
from email import message
from email.mime.text import MIMEText
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)


def test1():
    smtpObj = smtplib.SMTP('smtp.163.com', 25)
    logging.debug(type(smtpObj))
    logging.debug(smtpObj.ehlo('Hello!'))
    smtpObj.starttls()

    # smtp_ssl = smtplib.SMTP_SSL('smtp.163.com', 994)
    # logging.debug(type(smtp_ssl))
    # logging.debug(smtp_ssl.ehlo('Hello!'))

    logging.debug(smtpObj.login('yu_zhenquan@163.com', 'Dx2011512'))

    test = """
        这是一封来自于振泉测试python的email库的邮件
        """
    SUBJECT = u" 于振泉python邮件测试 "  # 定义邮件主题
    FROM = "yu_zhenquan@163.com"  # 定义邮件发件人
    TO = "2543352661@qq.com"  # 定义邮件收件人

    msg = MIMEText(test, "plain", "utf-8")  # 定义主体内容
    msg['Subject'] = SUBJECT  # 邮件主题
    msg['From'] = FROM  # 邮件发件人 , 邮件头部可见
    msg['To'] = TO  # 邮件收件人 , 邮件头部可见
    logging.debug(smtpObj.sendmail(FROM, TO, msg.as_string()), )
    logging.debug(smtpObj.quit())
    # message = 'Subject:hahaha. \nhello world'
    # logging.debug(smtpObj.sendmail(FROM, TO, message) )


def test2():
    smtp = smtplib.SMTP('smtp.163.com', 25)
    smtp.starttls()
    smtp.login('yu_zhenquan@163.com', 'Dx2011512')
    msg = message.EmailMessage()
    msg.set_content('你好，中国')

    SUBJECT = u" 于振泉python邮件测试 "  # 定义邮件主题
    FROM = "yu_zhenquan@163.com"  # 定义邮件发件人
    TO = "2543352661@qq.com"  # 定义邮件收件人
    msg['Subject'] = SUBJECT
    msg['From'] = FROM
    msg['To'] = TO
    msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'
    # msg.preamble = u'我是前言'

    for file in Path('.').iterdir():
        if file.is_file() and file.name.endswith('.jpg'):
            with open(file, 'rb') as f:
                read = f.read()
                msg.add_attachment(read, maintype='image', subtype=imghdr.what(None, read))

    smtp.send_message(msg)
    smtp.quit()


if __name__ == '__main__':
    # test1()
    test2()
