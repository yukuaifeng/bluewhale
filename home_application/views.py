# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import HostModel


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

def host(request):
    return render(request, 'home_application/hostmanage.html')

def host_data(request):
    if request.method == 'POST':
        host_name = request.POST.get("host_name", None)
        host_ip = request.POST.get("host_ip", None)
        host_os = request.POST.get("host_os", None)
        host_partition = request.POST.get("host_partition", None)

        if "" in [host_name, host_ip, host_os, host_partition]:
            return render_json({'code' : -1, 'message':'lost someone'})
        
        try:
            HostModel.objects.create(
                host_name = host_name, host_ip = host_ip, host_os = host_os, host_partition = host_partition)
        except Exception as e:
            return render_json({'code':-1, 'message':'something wrong'})
        
        return render_json({'code':0, 'message':'insert success'})
    else:
        return render_json({'code':0, 'items' : HostModel.objects.to_dict(),
                            'catalogues':{
                                'hostname':'主机名',
                                'hostip' : '主机ip',
                                'hostos' : '主机操作系统',
                                'hostpartition' : '磁盘分区',
                                'createtime' : '创建时间'
                            }})

