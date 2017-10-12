from django.contrib import admin
from .models import BookInfo, HeroInfo

# Register your models here.

# 创建超级管理员: python3 manage.py createsuperuser
# username: Andy  password: asd123456
#

admin.site.register(BookInfo)
admin.site.register(HeroInfo)
