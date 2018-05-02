#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# @Time    : 2017/12/6 14:58
# @Author  : HoxHou
# @File    : urls.py
# @Software: PyCharm Community Edition


from django.conf.urls import url, include

urlpatterns = [
    url(r'^pro_sys/pro_api/', include('app_api_test.pro_sys.pro_api.urls')),
    url(r'^pro_sys/pro_case/', include('app_api_test.pro_sys.pro_case.urls')),
    url(r'^pro_sys/pro_task/', include('app_api_test.pro_sys.pro_task.urls')),
    # ---------------------------------------------------------------------- #
    url(r'^pub_sys/pub_case/', include('app_api_test.pub_sys.pub_case.urls')),
]
