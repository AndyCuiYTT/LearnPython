from django.contrib import admin
from .models import BookInfo, HeroInfo


# Register your models here.

# 创建超级管理员: python3 manage.py createsuperuser
# username: Andy  password: asd123456
#


# 后台管理系统显示效果
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date']


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender', 'content', 'book']


# 注册模型
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
