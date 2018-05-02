#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# @Time    : 2017/12/6 9:50
# @Author  : HoxHou
# @File    : urls.py
# @Software: PyCharm Community Edition



from django.conf.urls import url



urlpatterns = [
    # 这里 r'^$' 里面得加上 ^$ 。如果里面还要配置 URL 结尾记的加上反斜杠，如 r'^index/$'
    url(r'^inv_center_api/$', inv_center_api_views.inventory_center_api_page),
    url(r'^inv_center_api/list/$', inv_center_api_views.api_list),
    url(r'^inv_center_api/add_from/$', inv_center_api_views.add_from),
    url(r'^inv_center_api/edit_from/$', inv_center_api_views.edit_from),
    url(r'^inv_center_api/sub_module_list/$', inv_center_api_views.sub_module_list),
    url(r'^inv_center_api/add/$', inv_center_api_views.api_add),
    url(r'^inv_center_api/edit/$', inv_center_api_views.api_edit),
    url(r'^inv_center_api/delete/$', inv_center_api_views.api_delete),
]
