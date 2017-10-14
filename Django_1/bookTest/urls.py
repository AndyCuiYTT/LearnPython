#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# urls.py
# LearnPython
#
# Created by AndyCui on 2017/10/12
#

from django.conf.urls import url
from .views import index, bookList, detail

# 配置 URL 路由
# 设置项目路径下 urls.py 文件,在 urlpatterns 下添加 url(r'^路径/', include('映射 app urls.py')),
# 在 app 跟路径添加 urls.py 文件,设置映射路由.
# index 的访问完整路径: http://127.0.0.1:8000/bookTest/index/
urlpatterns = [
    url(r'^$', index),
    url(r'^booklist/', bookList),
    url(r'^(\d+)/$', detail),
]
