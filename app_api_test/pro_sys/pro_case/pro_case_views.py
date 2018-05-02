# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 16:15
# @Author  : Yoson
# @File    : pro_case_views.py
# @Software: PyCharm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from common_utils.common import strClean
from common_utils import common
from common_utils.db_handler.mysql_engine import MySQLEngine

def case_manage(request):
    return render(request, '../templates/pro_sys/pro_case/case_manage.html')

def case_form(request):
    return render(request, '../templates/pro_sys/pro_case/case_form.html')

def run_form(request):
    return render(request, '../templates/pro_sys/pro_case/run_form.html')

def result_form(request):
    return render(request, '../templates/pro_sys/pro_case/result_form.html')

def case_query(request):
    user_name = request.COOKIES.get('user_name')
    if user_name:
        if request.method == 'GET':
            page = request.GET.get('page')
            limit = request.GET.get('limit')
            main_module = request.GET.get('main_module')
            module = request.GET.get('module')
            sub_module = request.GET.get('sub_module')
            level = request.GET.get('level')
            query_str = request.GET.get('query_str')
            sql = "SELECT * FROM pro_case WHERE state=1 "

            if level is not None and level != '':
                sql += "AND level = '{level}'".format(level=level)
            if query_str is not None and strClean(query_str) != '':
                query_str = strClean(query_str)
                sql += " AND (case_id like'{query_str}' or case_name LIKE'%{query_str}%' or api_id like'{query_str}')".format(query_str=query_str)

            if sub_module is not None and sub_module != '':
                sql += "AND menu_id in (select menu_id from q_boss_menu where state=1 and sys_name='产品系统' and main_module='{main_module}' and module = '{module}' and sub_module ='{sub_module}')".format(main_module=main_module, module=module,sub_module=sub_module)
            elif module is not None and module != '':
                sql += "AND menu_id in (select menu_id from q_boss_menu where state=1 and sys_name='产品系统' and main_module='{main_module}' and module = '{module}')".format(main_module=main_module, module=module)
            elif main_module is not None and main_module != '':
                sql += "AND menu_id in (select menu_id from q_boss_menu where state=1 and sys_name='产品系统' and main_module='{main_module}')".format(main_module=main_module)

            contact_list = MySQLEngine('pro_case').defined(type='query', sql=sql)
            paginator = Paginator(contact_list, limit)  # Show 25 contacts per page
            try:
                contacts = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                contacts = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                contacts = paginator.page(paginator.num_pages)
            for each in contacts.object_list:
                r = MySQLEngine('q_boss_menu').where(menu_id=each['menu_id'])
                each['main_module'] = r[0]['main_module']
                each['module'] = r[0]['module']
                each['sub_module'] = r[0]['sub_module']
            data = contacts.object_list, len(contact_list)
            return JsonResponse({'code': 0, 'msg': 'ok', 'count': data[1], 'data': data[0]})
    else:
        return HttpResponseRedirect('/')

@csrf_exempt
def case_add(request):
    user_name = request.COOKIES.get('user_name')
    if user_name:
        if request.method == 'POST':
            data = {}
            for key in request.POST:
                if strClean(request.POST.get(key)) != '':
                    data[key] = strClean(request.POST.get(key))
                elif key in ['case_name', 'main_module', 'module', 'sub_module', 'level', 'expected_result']:
                    return HttpResponse(key)
            data['menu_id'] = data.pop('sub_module')
            data.pop('module'), data.pop('main_module')
            data['created_by'] = user_name
            res = MySQLEngine('pro_case').insert_into(**data)
            return HttpResponse(res)
    else:
        return HttpResponseRedirect('/')

@csrf_exempt
def case_update(request):
    user_name = request.COOKIES.get('user_name')
    if user_name:
        if request.method == 'POST':
            data = {}
            for key in request.POST:
                if strClean(request.POST.get(key)) != '':
                    data[key] = strClean(request.POST.get(key))
                elif key in ['case_name', 'module', 'sub_module', 'level', 'expected_result']:
                    return HttpResponse(key)
            data['updated_by'] = user_name
            res = MySQLEngine('pro_case').update_set(data, id=request.POST.get('id'))
            return HttpResponse(res)
    else:
        return HttpResponseRedirect('/')

def case_delete(request):
    user_name = request.COOKIES.get('user_name')
    if user_name:
        if request.method == 'GET':
            data = {'updated_by': user_name, 'state': 0}
            res = MySQLEngine('pro_case').update_set(data, case_id=request.GET.get('case_id'))
            return HttpResponse(res)
    else:
        return HttpResponseRedirect('/')

def api_query(request):
    user_name = request.COOKIES.get('user_name')
    if user_name:
        if request.method == 'GET':
            res = MySQLEngine('pro_api').where(api_id=request.GET.get('api_id'))
            return JsonResponse(res[0])
    else:
        return HttpResponseRedirect('/')

@csrf_exempt
def case_run(request):
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

def get_module(request):
    user_name = request.COOKIES.get('user_name')
    if user_name:
        if request.method == 'GET':
            data = {}
            if request.GET.get('type') == '1':
                sql = "select distinct main_module from q_boss_menu where state=1 and sys_name='产品系统'"
                res = MySQLEngine('q_boss_menu').defined('query', sql)
                for each in res:
                    data[each['main_module']] = each['main_module']
            elif request.GET.get('type') == '2':
                sql = "select distinct module from q_boss_menu where state=1 and sys_name='产品系统' and main_module='" + request.GET.get('main_module')+"'"
                res = MySQLEngine('q_boss_menu').defined('query', sql)
                for each in res:
                    data[each['module']] = each['module']
            elif request.GET.get('type') == '3':
                sql = "select menu_id, sub_module from q_boss_menu where state=1 and sys_name='产品系统' and module='" + request.GET.get('module')+"'"
                res = MySQLEngine('q_boss_menu').defined('query', sql)
                for each in res:
                    data[each['menu_id']] = each['sub_module']
            return JsonResponse(data)
    else:
        return HttpResponseRedirect('/')
