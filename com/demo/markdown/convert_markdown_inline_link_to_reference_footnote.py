#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/7/23 19:21
# @Author: yuzq
# @File  : convert_markdown_inline_link_to_reference_footnote


if __name__ == '__main__':

    #将Markdown行内式链接转为文末参考式链接

    import sys
    import re
    import urllib
    import shutil
    from urllib import request
    from bs4 import BeautifulSoup


    md_file = sys.argv[1]   # 运行参数：md地址
    new_md = sys.argv[1][0:-3] + '_reference.md'
    shutil.copyfile(md_file, new_md)

    post = None  # 用来存放markdown文件内容
    index = 0
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    with open(md_file, 'r', encoding='utf-8') as f:  # 使用utf-8 编码打开
        post = f.read()
        matches = re.compile('[^!]\\[.*?\\](\(.*?\\))').findall(post)
        matches_no_repeat = list(set(matches))
        matches_no_repeat.sort(key=matches.index)
        matches = matches_no_repeat
        print('total url : {0}'.format(matches))
        post = post + '\n\n# 参考\n'
        for match in matches:
            index = index + 1
            print(index)
            url = match[1:-1]
            print(url)
            # footnote_mark = '[^footnote'+('{0}'.format(index))+ ']' #用这种替换格式会生成标准的markdown脚注
            footnote_mark = '[{0}]'.format(index)         #用这种替换格式，会生成markdown reference link
            footnote_mark2 = '[{0}]:'.format(index)         #用这种替换格式，会生成markdown reference link
            post = post.replace(match, footnote_mark) # 替换md文件中的地址，这里并不是标准的脚注
            # post = post.replace(match, footnote_mark)  # 替换md文件中的地址，用这种替换格式会生成标准的markdown脚注
            footnote_line = '\n'+footnote_mark2 + ''+ url
            url_title = ''
            if url[0:4] == 'http':  # 有title的url
                req = urllib.request.Request(url=url, headers=headers)
                try:
                    content = urllib.request.urlopen(req).read()
                except: # 获取不到标题
                    print('something is wrong with url {0}'.format(index))
                else: # 获取到标题才执行
                    soup = BeautifulSoup(content)
                    url_title = soup.title.string.replace("\n", "")
                    print(url_title)
                    footnote_line = footnote_line + '\n  网页标题: 《'+ url_title +'》'# 有标题就加上
            post = post + footnote_line

    open(new_md, 'w', encoding='utf-8').write(post)  # 如果有内容的话，就直接覆盖写入当前的markdown文件
            # 仍然注意用uft-8编码打开

