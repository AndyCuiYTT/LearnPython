#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# urls.py
# LearnPython
#
# Created by AndyCui on 2017/10/12
#

from django.conf.urls import url
from .views import index


urlpatterns = [
    url(r'^index/$', index),
]
