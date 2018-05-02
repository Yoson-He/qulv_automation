# -*- coding: utf-8 -*-
# @Time    : 2017/12/6 14:30
# @Author  : Yoson
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from app_api_test.pro_sys.pro_task import pro_task_views

urlpatterns = [
    url(r'^$', pro_task_views.task_page, name='task_page'),
    url(r'^task_query$', pro_task_views.task_query, name='task_query'),
    url(r'^task_form', pro_task_views.task_form, name='task_form'),


]