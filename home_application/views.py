# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
def home(request):
    """
    首页
    """
    return render(request, 'home_application/home.html')

def test(request):
    print(request.method)
    word = 'Congratuations!'
    return HttpResponse(word)

def hello(request):
    return render(request, 'home_application/helloworld.html')
