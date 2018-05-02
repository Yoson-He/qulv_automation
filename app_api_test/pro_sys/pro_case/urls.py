# -*- coding: utf-8 -*-
# @Time    : 2017/11/23 10:02
# @Author  : Yoson
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from app_api_test.pro_sys.pro_case import pro_case_views

urlpatterns = [
    url(r'^$', pro_case_views.case_manage, name='case_manage'),
    url(r'^query/$', pro_case_views.case_query, name='case_query'),
    url(r'^add/$', pro_case_views.case_add, name='case_add'),
    url(r'^update/$', pro_case_views.case_update, name='case_update'),
    url(r'^delete/$', pro_case_views.case_delete, name='case_delete'),
    url(r'^api_query/$', pro_case_views.api_query, name='api_query'),
    url(r'^case_run/$', pro_case_views.case_run, name='case_run'),
    url(r'^case_form/$', pro_case_views.case_form, name='case_form'),
    url(r'^run_form/$', pro_case_views.run_form, name='run_form'),
    url(r'^get_module/$', pro_case_views.get_module, name='get_module'),
    url(r'^result_form/$', pro_case_views.result_form, name='result_form'),

]