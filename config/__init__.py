# -*- coding: utf-8 -*-
from __future__ import absolute_import

__all__ = ['celery_app', 'RUN_VER', 'APP_CODE', 'SECRET_KEY', 'BK_URL', 'BASE_DIR']

import os

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from blueapps.core.celery import celery_app

# app 基本信息

# SaaS运行版本，如非必要请勿修改
RUN_VER = 'open'
# SaaS应用ID
APP_CODE = 'ykf'
# SaaS安全密钥，注意请勿泄露该密钥
SECRET_KEY = '7a5b01e2-91fa-4a37-8a36-e0630d8a43c6'
# 蓝鲸SaaS平台URL, 如 https://paas.blueking.com/
BK_URL = 'http://paas.class.o.qcloud.com:80/t/ykf/'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(
    __file__)))
