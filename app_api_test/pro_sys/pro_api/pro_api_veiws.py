#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# @Time    : 2017/12/6 9:47
# @Author  : HoxHou
# @File    : pro_api_veiws.py
# @Software: PyCharm Community Edition


from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from app_api_test.pro_sys.pro_api.pro_api_handler import ProApiHandler



@csrf_exempt
def pro_api_page(request):
    return render(request, '../templates/pro_sys/pro_api/pro_api.html')


@csrf_exempt
def add_from(request):
    return render(request, '../templates/pro_sys/pro_api/add_from.html')


@csrf_exempt
def edit_from(request):
    return render(request, '../templates/pro_sys/pro_api/edit_from.html')


@csrf_exempt
def import_from(request):
    return render(request, '../templates/pro_sys/pro_api/import_from.html')

def pro_api_list(request):
    if request.method == 'GET':
        user_name = request.COOKIES.get('user_name')
        page = request.GET.get('page')
        limit = request.GET.get('limit')
        if user_name:
            data = ProApiHandler().api_list(page, limit)
            return JsonResponse({'code': 0, 'msg': 'ok', 'count': data[1], 'data': data[0]})
        else:
            return redirect('/')

def params_list(request):
    if request.method == 'GET':
        user_name = request.COOKIES.get('user_name')
        api_id = request.GET.get('api_id')
        if user_name:
            rslt = ProApiHandler().params_list(api_id)
            return JsonResponse(rslt)
        else:
            return redirect('/')


@csrf_exempt
def api_add(request):
    rslt = None
    if request.method == 'POST':
        QueryDict = request.POST
        create_by = request.COOKIES.get('user_name')  # 从cookie中取值
        rslt = ProApiHandler().api_add(QueryDict, create_by)
        if rslt is not 1: rslt = 0
    return HttpResponse(rslt)


@csrf_exempt
def api_edit(request):
    rslt = None
    if request.method == 'POST':
        QueryDict = request.POST
        update_by = request.COOKIES.get('user_name')  # 从cookie中取值
        rslt = ProApiHandler().api_edit(QueryDict, update_by)
        if rslt is not 1: rslt = 0
    return HttpResponse(rslt)


@csrf_exempt
def api_delete(request):
    rslt = None
    if request.method == 'POST':
        api_id = request.POST['api_id']
        update_by = request.COOKIES.get('user_name')  # 从cookie中取值
        rslt = ProApiHandler().api_delete(api_id, update_by)
        if rslt is not 1: rslt = 0
    return HttpResponse(rslt)



@csrf_exempt
def module_list(request):
    api_id = request.GET.get('api_id', None)
    main_module = request.GET.get('main_module', None)
    rslt = ProApiHandler().module_list(api_id,main_module)
    return JsonResponse(rslt)




@csrf_exempt
def sub_module_list(request):
    api_id = request.GET.get('api_id', None)
    module = request.GET.get('module', None)
    main_module = request.GET.get('main_module', None)
    rslt = ProApiHandler().sub_module_list(api_id,module,main_module)
    return JsonResponse(rslt)


@csrf_exempt
def api_add(request):
    rslt = None
    if request.method == 'POST':
        QueryDict = request.POST
        create_by = request.COOKIES.get('user_name')  # 从cookie中取值
        rslt = ProApiHandler().api_add(QueryDict, create_by)
        if rslt is not 1: rslt = 0

    return HttpResponse(rslt)

@csrf_exempt
def api_edit(request):
    rslt = None
    if request.method == 'POST':
        QueryDict = request.POST
        update_by = request.COOKIES.get('user_name')  # 从cookie中取值
        rslt = ProApiHandler().api_edit(QueryDict, update_by)
        if rslt is not 1: rslt = 0
    return HttpResponse(rslt)


@csrf_exempt
def api_delete(request):
    rslt = None
    if request.method == 'POST':
        api_id = request.POST['api_id']
        update_by = request.COOKIES.get('user_name')  # 从cookie中取值
        rslt = ProApiHandler().api_delete(api_id, update_by)
        if rslt is not 1: rslt = 0
    return HttpResponse(rslt)



@csrf_exempt
def api_import(request):
    rslt = None
    if request.method == 'POST':
        api_info_channel = request.POST['api_info_channel']
        print(api_info_channel)
        import_by = request.COOKIES.get('user_name')
        rslt = ProApiHandler().import_api(api_info_channel)
        rslt=0
    return HttpResponse(rslt)