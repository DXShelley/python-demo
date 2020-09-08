#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/9/2 19:19
# @Author: yuzq
# @File  : TestPdf
import PyPDF3


def simple():
    # pdf_file = open('encrypted.pdf','rb')
    pdf_file = open('meetingminutes.pdf', 'rb')
    pdf_reader = PyPDF3.PdfFileReader(pdf_file)

    print(pdf_reader.isEncrypted)
    # pdf_reader.decrypt('rosebud')
    print(pdf_reader.numPages)

    page = pdf_reader.getPage(1)
    print(page.extractText())


def simple2():
    pdf_file = open('meetingminutes.pdf', 'rb')
    pdf_reader = PyPDF3.PdfFileReader(pdf_file)

    pdf_file2 = open('meetingminutes2.pdf', 'rb')
    pdf_reader2 = PyPDF3.PdfFileReader(pdf_file)

    pdf_writer = PyPDF3.PdfFileWriter()

    for page_num in range(pdf_reader.numPages):
        pdf_obj = pdf_reader.getPage(page_num)
        pdf_writer.addPage(pdf_obj)

    for page_num in range(pdf_reader2.numPages):
        pdf_obj = pdf_reader2.getPage(page_num)
        pdf_writer.addPage(pdf_obj)

    pdf_file3 = open('combinedminutes.pdf', 'wb')
    pdf_writer.write(pdf_file3)

    pdf_file3.close()
    pdf_file.close()
    pdf_file2.close()


def simple3():
    pass


if __name__ == '__main__':
    # simple()
    simple2()
