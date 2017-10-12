#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Spider.py
# LearnPython
#
# Created by AndyCui on 2017/10/10
#

import urllib2
import re
import os


if __name__ == '__main__':

    # 抓取过程
    # 1.访问一个页面地址,获取网页源代码
    url = 'https://www.qiushibaike.com/text/page/1'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    header = {'User-Agent': user_agent}
    try:
        request = urllib2.Request(url=url, headers=header)
        reponse = urllib2.urlopen(request)
        content = reponse.read()
    except urllib2.HTTPError as e:
        print(e)
        exit()
    except urllib2.URLError as e:
        print(e)
        exit()
    # print content
    # 2.根据抓取到内容提取想要的数据
    regex = re.compile('<h2>\s*(.*?)\s*</h2>.*?<div class="content">.*?<span>\s*(.*?)\s*</span>.*?</div>', re.S)
    items = regex.findall(content)
    # 3.保存抓取的数据
    for item in items:
        path = 'qiubai'
        try:
            if not os.path.exists(path):
                os.makedirs(path)
            filePath = path + '/' + item[0] +'.txt'
            with open(filePath, 'w') as file:
                file.write(item[1].replace('\n', '').replace('<br/>', '\n'))
        except IOError as e:
            print(e)

    # 4.抓取其他剩下页面数据
    # 循环上边过程,修改页码
    pass
