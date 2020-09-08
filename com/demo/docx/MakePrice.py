#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/9/3 20:00
# @Author: yuzq
# @File  : MakePrice
from docx import Document
from docx.shared import Pt


def get_student():
    dict = {}
    with open('Student.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            if line.endswith('\n'):
                key, value = line.strip('\n').split(' ')
            else:
                key, value = line.split(' ')
            dict.setdefault(key, value)
    return dict

def get_docx():
    document = Document('学生奖状模板.docx')
    paragraphs = document.paragraphs
    return paragraphs

def make_price2(dict,paragraphs):


    for key ,value in dict.items():
        document = Document()
        paragraphs[0].text = key + ' : '
        paragraphs[4].text = value + ' '
        runs_ = paragraphs[0].runs[0]
        font = runs_.font
        font.size = Pt(20)
        runs_.font.name = u'楷体'
        runs_.bold = True

        font = paragraphs[4].runs[0].font
        font.size = Pt(20)
        paragraphs[4].runs[0].font.name = u'楷体'



def make_price(dict={}):
    document = Document('学生奖状模板.docx')
    paragraphs = document.paragraphs
    print([paragraph.text for paragraph in paragraphs])


    for key, value in dict.items():
        paragraphs[0].text = key + ' : '
        paragraphs[4].text = value + ' '
        runs_ = paragraphs[0].runs[0]
        font = runs_.font
        font.size = Pt(20)
        runs_.font.name = u'楷体'
        runs_.bold = True

        font = paragraphs[4].runs[0].font
        font.size = Pt(20)
        paragraphs[4].runs[0].font.name = u'楷体'

        document.save('学生奖状-' + key + '.docx')



if __name__ == '__main__':
    dict = get_student()
    make_price(dict)
