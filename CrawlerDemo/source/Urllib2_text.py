#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Urllib2_text.py
# CrawlerDemo
#
# Created by AndyCui on 2017/10/9
#

import urllib
import urllib2

if __name__ == '__main__':
    # 设置url信息和头部信息
    url = "https://www.oschina.net/action/user/hash_login"
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    formData = {'email': 'eee@163.com', 'pwd': '55'}
    data = urllib.urlencode(formData)
    request = urllib2.Request(url=url, data=data, headers=header)
    # 发送请求和接收响应
    try:
        response = urllib2.urlopen(request)
        print response.read()
    except urllib2.HTTPError, e:
        print e.code
        print e.reason



