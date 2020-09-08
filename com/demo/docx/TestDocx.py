#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/9/2 19:49
# @Author: yuzq
# @File  : TestDocx
from docx import Document
from docx.shared import Inches, Cm


def simple():
    document = Document('demo.docx')  # type:docx.document.Document
    print(type(document))
    paragraphs = document.paragraphs  # type:docx.text.paragraph.Paragraph
    # print(paragraphs)
    print('-----------paragraphs-------------')
    print(paragraphs[0].text)
    print(paragraphs[0].style.name)
    paragraphs[0].style = 'Normal'
    print(paragraphs[0].style.name)
    print(paragraphs[0].text)
    print(paragraphs[1].text)
    print(paragraphs[2].text)
    runs = paragraphs[1].runs
    # print(runs)
    print('-----------runs-------------')
    print(runs[0].text)
    print(runs[1].text)
    runs[1].underline = True
    print(runs[2].text)
    print(runs[3].text)

    document.save('restyle.docx')


def simple2():
    document = Document()

    document.add_paragraph('Hello,world', 'Title')
    parag1 = document.add_paragraph('This is another paragraph', '')
    parag2 = document.add_paragraph('This is yet another paragraph')

    parag1.add_run(' This text is being added to the second paragraph')

    print(type(document))
    document.save('helloworld.docx')


def create_docx():
    document = Document()
    document.add_heading('Document Title', 0)
    p = document.add_paragraph('A plain paragraph having some ')
    p.add_run('bold').bold = True
    p.add_run(' and some ')
    p.add_run('italic.').italic = True

    document.add_heading('Heading, level 1', level=1)
    document.add_paragraph('Intense quote', style='Intense Quote')
    document.add_paragraph(
        'first item in unordered list', style='List Bullet'
    )

    document.add_paragraph(
        'first item in ordered list', style='List Number'
    )

    document.add_page_break()

    paragraph = document.add_paragraph()
    paragraph.add_run().add_picture(r'图片.jpg',width=Cm(15), height=Cm(10))
    # document.add_picture('图片.jpg',width=Cm(15), height=Cm(10))
    # document.add_picture('无标题的表单.png')
    document.add_page_break()

    table = document.add_table(rows=1, cols=3)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Qty'
    hdr_cells[1].text = 'Id'
    hdr_cells[2].text = 'Desc'

    records = (
        (3, '101', 'Spam'),
        (7, '422', 'Eggs'),
        (4, '631', 'Spam, spam, eggs, and spam')
    )

    for qty, id, desc in records:
        row_cells = table.add_row().cells
        row_cells[0].text = str(qty)
        row_cells[1].text = id
        row_cells[2].text = desc

    document.add_page_break()
    document.save('demo2.docx')


def getText(filename):
    doc = Document(filename)

    fullText = []

    for para in doc.paragraphs:
        fullText.append(para.text)

    return '\n'.join(fullText)


if __name__ == '__main__':
    create_docx()
    # simple()
    # simple2()
    # print(getText('demo.docx'))
