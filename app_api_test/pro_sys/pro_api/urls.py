#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# @Time    : 2017/12/6 9:50
# @Author  : HoxHou
# @File    : urls.py
# @Software: PyCharm Community Edition


from django.conf.urls import url

from app_api_test.pro_sys.pro_api import pro_api_veiws

urlpatterns = [
    # 这里 r'^$' 里面得加上 ^$ 。如果里面还要配置 URL 结尾记的加上反斜杠，如 r'^index/$'
    # 全路径地址:/app_api_test/pro_sys/pro_api/.....
    url(r'^$', pro_api_veiws.pro_api_page, name='pro_api_page'),
    url(r'^add_from/$', pro_api_veiws.add_from,name='add_from'),
    url(r'^edit_from/$', pro_api_veiws.edit_from, name='edit_from'),
    url(r'^import_from/$', pro_api_veiws.import_from, name='import_from'),
    url(r'^import/$', pro_api_veiws.api_import, name='import'),
    url(r'^list/$', pro_api_veiws.pro_api_list, name='list'),
    url(r'^params_list/$', pro_api_veiws.params_list, name='params_list'),
    url(r'^module_list/$', pro_api_veiws.module_list, name='module_list'),
    url(r'^sub_module_list/$', pro_api_veiws.sub_module_list, name='sub_module_list'),
    url(r'^add/$', pro_api_veiws.api_add, name='api_add'),
    url(r'^edit/$', pro_api_veiws.api_edit, name='api_edit'),
    url(r'^delete/$', pro_api_veiws.api_delete, name='api_delete'),

]
