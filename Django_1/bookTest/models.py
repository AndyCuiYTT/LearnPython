from django.db import models


# 数据模型
# Create your models here.
class BookInfo(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField()


class HeroInfo(models.Model):
    name = models.CharField(max_length=10)
    content = models.CharField(max_length=100)
    gender = models.BooleanField(default=True)
    book = models.ForeignKey(BookInfo)  # 指定外键

    # 创建项目: django-admin.py startproject HelloWorld
    # 创建应用: python3 manage.py startapp bookTest
    # 定义模型类
    # 生成迁移文件: python3 manage.py makemigrations
    # 迁移: python3 manage.py migrate

    # 数据操作命令
    # 创建 book = BookInfo()
    # 保存 book.save()
    # 修改 book = BookInfo.objects.get(id='1')
    # book.save()
    # 删除 book.delete()
    # 查询 BookInfo.objects.all()

    # 关系
    # 根据图书找英雄对象 book.heroinfo_set.all()
    # 根据英雄找图书对象 hero.book
