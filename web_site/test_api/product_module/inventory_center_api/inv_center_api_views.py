#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 19:31
# @Author  : HoxHou
# @File    : inv_center_api_views.py
# @Software: PyCharm Community Edition
import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from app_api_test.test_api.product_module.inventory_center_api.inv_center_api import inv_center_api


def inventory_center_api_page(request):
    """

    :param request:
    :return:
    """
    user_name = request.COOKIES.get('user_name')  # 从cookie中取值
    if user_name:
        return render(request, '../templates/test_api/product_module/inventory_center_api/inv_center_api.html')
    else:
        return redirect('/')


def add_from(request):
    """

    :param request:
    :return:
    """
    return render(request, '../templates/test_api/product_module/inventory_center_api/add_from.html')


@csrf_exempt
def edit_from(request):
    """

    :param request:
    :return:
    """
    return render(request, '../templates/test_api/product_module/inventory_center_api/edit_from.html')


def api_list(request):
    """

    :param request:
    :return:
    """
    if request.method == 'GET':
        user_name = request.COOKIES.get('user_name')
        page = request.GET.get('page')
        limit = request.GET.get('limit')
        if user_name:
            data = inv_center_api().api_list(page, limit)
            return JsonResponse({'code': 0, 'msg': 'ok', 'count': data[1], 'data': data[0]})
        else:
            return redirect('/')


@csrf_exempt
def api_add(request):
    rslt = None
    if request.method == 'POST':
        QueryDict = request.POST
        create_by = request.COOKIES.get('user_name')  # 从cookie中取值
        rslt = inv_center_api().add(QueryDict, create_by)
        if rslt is not 1: rslt = 0
    return HttpResponse(rslt)


@csrf_exempt
def api_edit(request):
    rslt = None
    if request.method == 'POST':
        QueryDict = request.POST
        update_by = request.COOKIES.get('user_name')  # 从cookie中取值
        rslt = inv_center_api().edit(QueryDict, update_by)
        if rslt is not 1: rslt = 0
    return HttpResponse(rslt)


@csrf_exempt
def api_delete(request):
    rslt = None
    if request.method == 'POST':
        id = request.POST['id']
        update_by = request.COOKIES.get('user_name')  # 从cookie中取值
        rslt = inv_center_api().delete(id, update_by)
        if rslt is not 1: rslt = 0
    return HttpResponse(rslt)


@csrf_exempt
def sub_module_list(request):
    rslt = None
    module = request.GET.get('module', None)
    api_id = request.GET.get('api_id', None)
    if len(module) is 0:
        pass
    else:
        list=inv_center_api().sub_module_list(module)
        sub_module=inv_center_api().edit_sub_module(api_id)
        rslt = {
            "status": 200,
            "message": "seccuss!",
            "sub_module":sub_module,
            "data": list,
        }
    return HttpResponse(json.dumps(rslt))
