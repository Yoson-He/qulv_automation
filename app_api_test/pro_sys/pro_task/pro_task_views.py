# -*- coding: utf-8 -*-
# @Time    : 2017/12/6 14:30
# @Author  : Yoson
# @File    : pro_task_views.py
# @Software: PyCharm

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from common_utils.common import strClean
from common_utils import common
from common_utils.db_handler.mysql_engine import MySQLEngine

def task_page(request):
    return render(request, "../templates/pro_sys/pro_task/task_page.html")

def task_form(request):
    return render(request, "../templates/pro_sys/pro_task/task_form.html")


def task_query(request):
    user_name = request.COOKIES.get('user_name')
    if user_name:
        if request.method == 'GET':
            page = request.GET.get('page')
            limit = request.GET.get('limit')
            query_str = request.GET.get('query_str')
            sql = "SELECT * FROM pro_task WHERE state=1 "

            if query_str is not None and strClean(query_str) != '':
                query_str = strClean(query_str)
                sql += " AND (task_id like'{query_str}' or task_name LIKE'%{query_str}%')".format(
                    query_str=query_str)
            contact_list = MySQLEngine('pro_task').defined(type='query', sql=sql)
            paginator = Paginator(contact_list, limit)  # Show 25 contacts per page
            try:
                contacts = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                contacts = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                contacts = paginator.page(paginator.num_pages)
            data = contacts.object_list, len(contact_list)
            print(data[0])
            return JsonResponse({'code': 0, 'msg': 'ok', 'count': data[1], 'data': data[0]})
    else:
        return HttpResponseRedirect('/')