# -*- coding: utf-8 -*-
from django.db import models
import datetime

# Create your models here.

class HostModelManager(models.Manager):
    def get_record(self, data):
        try:
            qs = super().get_queryset()
            res_dict = [{
                'host_name' = item.host_name,
                'host_ip' = item.host_ip,
                'host_os' = item.host_os,
                'host_partition' = item.host_partition,
                'create_time' = item.create_time
            }]
        except Exception,e:
            print("获取失败", e)
        return res_dict



class HostModel(models.Model):
    os_choices = (
        ('windows','windows'),
        ('linux', 'linux'),
        ('mac','mac'),
    )
    host_name = models.CharField("主机名", max_length=64)
    host_ip = models.GenericIPAddressField("主机ip", max_length=64)
    host_os = models.CharField("操作系统", choices = os_choices, max_length=64)
    host_partition = models.CharField("磁盘分区", max_length=64)
    create_time = models.DateTimeField("创建时间", auto_now=True)

    objects = HostModelManager()
    