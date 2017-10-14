from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo, HeroInfo


# Create your views here.

# view: 必须接收参数: request(HttpRequest),
# view: 响应返回 HttpResponse
# HttpRequest
def index(request):
    # HttpResponse
    # return HttpResponse('hello Django')
    context = {'title': '首页', 'list': range(10)}
    return render(request, 'bookTest/index.html', context)


def bookList(request):
    list = BookInfo.objects.all()
    context = {'bookList': list}
    return render(request, 'bookTest/bookList.html', context)


def detail(request, id):
    list = BookInfo.objects.get(id=id).heroinfo_set.all()
    context = {'herolist': list}
    return render(request, 'bookTest/detail.html', context)
