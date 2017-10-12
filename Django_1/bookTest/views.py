from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# view: 必须接收参数: request(HttpRequest),
# view: 响应返回 HttpResponse
# HttpRequest
def index(request):
    # HttpResponse
    return HttpResponse('hello Django')
