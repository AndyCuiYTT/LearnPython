from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# HttpRequest
def index(request):
    # HttpResponse
    return HttpResponse('hello world ll')
