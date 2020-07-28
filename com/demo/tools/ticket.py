#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/7/24 17:06
# @Author: yuzq
# @File  : ticket

from splinter.browser import Browser
from time import sleep

class ticket(object):
    """docstring for 12306抢票"""
    driver_name = ''
    executable_path = ''
    # 用户名，密码
    username = u"153****1009"
    passwd = u"*******"
    # 车次，选择第几趟，0则从上之下依次点击
    order = 1
    ###乘客名
    users = [u"XXX"]
    ##席位
    xb = u"硬座"
    pz = u"成人票"

    """网址"""
    ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
    login_url = "https://kyfw.12306.cn/otn/login/init"
    initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"
    buy = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"


    # 需要下载chromedriver
    def __init__(self):
        self.driver_name = 'chrome'
        self.executable_path = 'D:\Chrome Driver\chromedriver'


    def login(self):
        self.driver.visit(self.login_url)
        # 填充密码
        self.driver.fill("loginUserDTO.user_name", self.username)
        # sleep(1)
        self.driver.fill("userDTO.password", self.passwd)
        print(u"等待验证码，自行输入...")
        while True:
            if self.driver.url != self.initmy_url:
                sleep(1)
            else:
                break


    def start(self):
        self.driver = Browser(driver_name=self.driver_name, executable_path=self.executable_path)
        self.driver.driver.set_window_size(1900, 1000)
        self.login()
        # sleep(1)
        self.driver.visit(self.ticket_url)
        try:
            print(u"购票页面开始...")
            # sleep(1)
            # 加载查询信息
            self.driver.cookies.add({"_jc_save_fromStation": self.starts})
            self.driver.cookies.add({"_jc_save_toStation": self.ends})
            self.driver.cookies.add({"_jc_save_fromDate": self.dtime})

            self.driver.reload()

            count = 0
            if self.order != 0:
                while self.driver.url == self.ticket_url:
                    try:
                        self.driver.find_by_text(u"查询").click()
                    except Exception as e:
                        continue
                    count += 1
                    # 根据td的id获取节点以判断是否有票 id需要手工获取
                    isTicketElement = self.driver.find_by_id("YW_490000502609")
                    if len(isTicketElement) == 0:
                        print("网络错误")
                        continue
                    print(u"循环查询... 第 %s 次，还是木有票" % count)
                    isTicket = self.driver.find_by_id("YW_490000502609")._element.text
                    sleep(30)
                    # isTicket = "--" or isTicket = "无" 均是指无相应席位的余票
                    if isTicket == "无":
                        continue
                    # sleep(1)
                    try:
                        self.driver.find_by_text(u"预订")[self.order - 1].click()
                        continue
                    except Exception as e:
                        print(e)
                        print(u"还没开始预订")
                        continue
            else:
                while self.driver.url == self.ticket_url:
                    self.driver.find_by_text(u"查询").click()
                    count += 1
                    isTicket = self.driver.find_by_id("YW_490000502609")
                    print(isTicket)
                    sleep(0.8)
                    try:
                        for i in self.driver.find_by_text(u"预订"):
                            i.click()
                            sleep(1)
                    except Exception as e:
                        print(e)
                        print(u"还没开始预订 %s" % count)
                        continue

            print(u"开始预订...")
            # sleep(3)
            # self.driver.reload()
            sleep(1)
            print(u'开始选择用户...')
            for user in self.users:
                self.driver.find_by_text(user).last.click()
            # seatType_1 选择席位 略
            print(u"提交订单...")
            sleep(1)
            # 选择席别、票种示例
            # self.driver.find_by_xpath('//select[@id="seatType_1"]/option[@value="0"]')._element.click()
            # self.driver.find_by_text(self.pz).click()
            # self.driver.find_by_id('').select(self.pz)
            # # sleep(1)
            # self.driver.find_by_text(self.xb).click()
            # sleep(1)
            self.driver.find_by_id('submitOrder_id').click()
            # print u"开始选座..."
            # self.driver.find_by_id('1D').last.click()
            # self.driver.find_by_id('1F').last.click()

            sleep(1.5)
            print(u"确认选座...")
            self.driver.find_by_id('qr_submit_id').click()

        except Exception as e:
            print(e)


# 需要获取相应站点的cookies
cities = {'青岛': '%u9752%u5C9B%2CQDK',
          '临沂': '%u4E34%u6C82%2CLVK'}

if __name__ == '__main__':
    ticket = ticket()
    ticket.starts = cities['青岛']
    ticket.ends = cities['临沂']
    ticket.dtime = "2018-02-13"
    ticket.start()
