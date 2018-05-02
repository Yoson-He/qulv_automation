# -*- coding: utf-8 -*-
# @Time    : 2017/12/11 17:30
# @Author  : Yoson
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from app_api_test.pub_sys.pub_case import pub_case_views
urlpatterns = [
    url(r'^$', pub_case_views.pub_case_manage, name='pub_case_manage'),
    url(r'^query/$', pub_case_views.pub_case_query, name='pub_case_query'),
    url(r'^add/$', pub_case_views.pub_case_add, name='pub_case_add'),
    url(r'^update/$', pub_case_views.pub_case_update, name='pub_case_update'),
    url(r'^delete/$', pub_case_views.pub_case_delete, name='pub_case_delete'),
    url(r'^api_query/$', pub_case_views.pub_api_query, name='pub_api_query'),
    url(r'^case_run/$', pub_case_views.pub_case_run, name='pub_case_run'),
    url(r'^case_form/$', pub_case_views.pub_case_form, name='pub_case_form'),
    url(r'^run_form/$', pub_case_views.pub_run_form, name='pub_run_form'),
    url(r'^result_form/$', pub_case_views.pub_result_form, name='pub_result_form'),
    url(r'^get_host/$', pub_case_views.get_host, name='get_host'),

]