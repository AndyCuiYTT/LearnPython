#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# RE_test.py
# CrawlerDemo
#
# Created by AndyCui on 2017/10/10
#

import re

if __name__ == '__main__':
    ''
    # 判断字符串是否全部是小写字母 [a-z]+$
    # result = re.match('[a-z]+', 'aaaaaa')
    # if result:
    #     print '全是小写'
    # else:
    #     print '不全是小写'

    # result = re.search('^[a-z]+$', 'aaaaaa')
    # if result:
    #     print '全是小写'
    #     print result.group()
    # else:
    #     print '不全是小写'

    # regex = re.compile('^[a-z]+$')
    # result = regex.search('ddddddd')
    # if result:
    #     print '全是小写'
    #     print result.group()
    # else:
    #     print '不全是小写'

    # 提取分组字符串,字母[a-z]+ 数字[0-9]+: ([0-9]+)([a-z]+)([0-9]+)([a-z]+)
    # str = 'ssdsdf232334dgfsdf323fdgd'
    # result = re.search('([0-9]+)([a-z]+)([0-9]+)([a-z]+)', str)
    # print result.group(4)

    # 在字符串中提取邮箱手机号
    str = 'sdsfsfdsdsfwe18315915937sf15277883465s-=-=---'
    # 0?(13|14|15|18)[0-9]{9}
    regex_phone = re.compile('(0?(?:13|14|15|18)[0-9]{9})')
    print regex_phone.findall(str)

