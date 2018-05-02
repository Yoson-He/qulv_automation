# -*- coding: utf-8 -*-
# @Time    : 2017/12/11 17:30
# @Author  : Yoson
# @File    : pub_case_views.py
# @Software: PyCharm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from common_utils.common import strClean
from common_utils import common
from common_utils.db_handler.mysql_engine import MySQLEngine

def pub_case_manage(request):
    return render(request, '../templates/pub_sys/pub_case/pub_case_manage.html')

def pub_case_form(request):
    return render(request, '../templates/pub_sys/pub_case/pub_case_form.html')

def pub_run_form(request):
    return render(request, '../templates/pub_sys/pub_case/pub_run_form.html')

def pub_result_form(request):
    return render(request, '../templates/pub_sys/pub_case/pub_result_form.html')

def pub_case_query(request):
    user_name = request.COOKIES.get('user_name')
    if user_name:
        if request.method == 'GET':
            page = request.GET.get('page')
            limit = request.GET.get('limit')
            level = request.GET.get('level')
            query_str = request.GET.get('query_str')
            sql = "select case_id,b.api_id,case_name,level,path,uri_params_value,req_body_value,req_params_value,expected_result, a.remark as remark " \
                  "from pub_case as a left join pub_api b on a.api_id = b.api_id " \
                  "where a.state=1 "

            if level is not None and level != '':
                sql += "AND level = '{level}'".format(level=level)
            if query_str is not None and strClean(query_str) != '':
                query_str = strClean(query_str)
                sql += " AND (case_id like'{query_str}' or case_name LIKE'%{query_str}%' or api_id like'{query_str}')".format(query_str=query_str)

            contact_list = MySQLEngine('pub_case').defined(type='query', sql=sql)
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
            return JsonResponse({'code': 0, 'msg': 'ok', 'count': data[1], 'data': data[0]})
    else:
        return HttpResponseRedirect('/')

@csrf_exempt
def pub_case_add(request):
    user_name = request.COOKIES.get('user_name')
    if user_name:
        if request.method == 'POST':
            data = {}
            for key in request.POST:
                if strClean(request.POST.get(key)) != '':
                    data[key] = strClean(request.POST.get(key))
                elif key in ['case_name', 'level', 'expected_result', 'api_id']:
                    return HttpResponse(key)
            data['created_by'] = user_name
            res = MySQLEngine('pub_case').insert_into(**data)
            return HttpResponse(res)
    else:
        return HttpResponseRedirect('/')

@csrf_exempt
def pub_case_update(request):
    user_name = request.COOKIES.get('user_name')
    if user_name:
        if request.method == 'POST':
            data = {}
            for key in request.POST:
                if strClean(request.POST.get(key)) != '':
                    data[key] = strClean(request.POST.get(key))
                elif key in ['case_name', 'level', 'api_id', 'expected_result']:
                    return HttpResponse(key)
            if 'path' in data:
                data.pop('path')
            data['updated_by'] = user_name
            res = MySQLEngine('pub_case').update_set(data, case_id=request.POST.get('case_id'))
            return HttpResponse(res)
    else:
        return HttpResponseRedirect('/')

def pub_case_delete(request):
    user_name = request.COOKIES.get('user_name')
    if user_name:
        if request.method == 'GET':
            data = {'updated_by': user_name, 'state': 0}
            res = MySQLEngine('pub_case').update_set(data, case_id=request.GET.get('case_id'))
            return HttpResponse(res)
    else:
        return HttpResponseRedirect('/')

def pub_api_query(request):
    user_name = request.COOKIES.get('user_name')
    if user_name:
        if request.method == 'GET':
            res = MySQLEngine('pub_api').where(api_id=request.GET.get('api_id'), state=1)
            if len(res) == 0:
                return HttpResponse('API不存在')
            return JsonResponse(res[0])
    else:
        return HttpResponseRedirect('/')

@csrf_exempt
def pub_case_run(request):
    user_name = request.COOKIES.get('user_name')
    if user_name:
        if request.method == 'POST':
            data = {}
            data['uri_params_value'] = None
            for key in request.POST:
                if strClean(request.POST.get(key)) != '':
                    data[key] = strClean(request.POST.get(key))
                elif key in ['host', 'path']:
                    return HttpResponse(key)

            url = common.urlHandle(host=data['host'], path=data['path'], uri_params_value=data['uri_params_value'])
            if url == 'uri参数个数不匹配':
                return HttpResponse('uri参数个数不匹配')
            data['url'] = url
            case_list = []
            case_list.append(data)
            res=common.runTest(case_list)
            if type(res) is str:
                return HttpResponse(res)
            else:
                return JsonResponse(res[0][0])
    else:
        return HttpResponseRedirect('/')

def get_host():
    pass