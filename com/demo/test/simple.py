#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/7/28 11:17
# @Author: yuzq
# @File  : simple

class Spam(object):

    def __init__(self):
        self.eggs = 1

    def hello(self, name):
        print('Hello ' + name)

    def spam(self):
        eggs = 99
        self.bacon()
        print(eggs)
        print(self.eggs)

    def bacon(self):
        ham = 101
        self.eggs = 0


if __name__ == '__main__':
    spam = Spam()
    spam.spam()

    # vars = input('请键盘输入')
    # print(vars)
    # print(int(vars))

    # while True:
    #     name = input("who are you ?")
    #     if name != 'yuzq':
    #         continue
    #
    #     password = input("Hello,yuzq.What is the password ?")
    #     if password == "yuzq":
    #         break
    # print("Access granted")

    # for i,j in range(5):
    #     print("执行次数：" + str(i))

    for i in range(5):
        print(type(i))

    # print(range(5))
    # print(range(5).index(1))
    # print(range(10).start)
    # print(range(2,8,3).start)
    # print(range(2,8,3).stop)
    # print(range(2,8,3).step)
    # print(range(2,9,3).count())
    # print(list(range(2,9,3)))

    # print(random.randrange(0,10,2))
    # for i in range(5):
    #     print(random.randint(1,10))

    # while True:
    #     print('Type exit to exit')
    #     response = input()
    #     if(response == 'exit'):
    #         sys.exit()
    #     print("You typed " + response + '.')

    # spam = 333
    # if spam == 1:
    #     print('Hello')
    # elif spam == 2:
    #     print('Howdy')
    # else:
    #     print('Greetings')

    # for i in range(1,11):
    #     print(i)
    #
    # j = 1
    # while j < 11:
    #     print(j)
    #     j = j + 1

    # print(round(12.1111))
    # print(abs(-1212.1212))

    # Hello('Alice')
    # Hello('Bob')
    # print('hello','haha',sep=',',end='dddddd')


