#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/7/28 16:06
# @Author: yuzq
# @File  : GuessNumber
import random


def guess_number():
    print('I am Thinking of a number between 1 and 20')
    target_number = random.randint(1, 20)
    count = 0
    while count < 6:
        print('Take a guess')
        number = int(input())
        if number < target_number:
            print('Your guess is too low')
        elif number > target_number:
            print("Your guess is too high")
        else:
            print("Good job! You guessed my number in " + str(count) + 'guesses!')
            break
        count = count + 1
    if count == 6:
        print('Nope. The number I was thinking of was' + str(target_number))



if __name__ == '__main__':
    guess_number()
