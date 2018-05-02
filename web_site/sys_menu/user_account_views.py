#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# @Time    : 2017/9/19 15:03
# @Author  : HoxHou
# @File    : user_account_views.py
# @Software: PyCharm Community Edition


from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from app_sys_main.sys_user.user_account import UserAccount



def user_account_page(request):
    user_name = request.COOKIES.get('user_name')  # 从cookie中取值
    if user_name:
        return render(request, '../templates/sys_main/user_account.html')
    else:
        return redirect('/')


def user_list(request):
    if request.method == 'GET':
        user_name = request.COOKIES.get('user_name')
        page = request.GET.get('page')
        limit = request.GET.get('limit')
        if user_name:
            data = UserAccount().sys_user_list(page,limit)
            return JsonResponse({'code': 0, 'msg': 'ok', 'count': data[1], 'data': data[0]})
        else:
            return redirect('/')





@csrf_exempt
def user_from(request):
    return render(request, '../templates/sys_main/user_from.html')


@csrf_exempt
def user_add(request):
    global rslt
    if request.method == 'POST':
        user_name = request.POST.get('user_name', '')
        realName = request.POST.get('realName', '')
        password = request.POST.get('repass', '')
        user_role = request.POST.get('user_role', '')
        phone = request.POST.get('phone', '')
        create_by = request.COOKIES.get('user_name')  # 从cookie中取值
        rslt = UserAccount().add(user_name=user_name,realName = realName, password=password, create_by=create_by, user_role=user_role,
                                 phone=phone)
    return HttpResponse(rslt)


@csrf_exempt
def user_delete(request):
    global rslt
    if request.method == 'POST':
        id = request.POST.get('id', '')
        delete_by = request.COOKIES.get('user_name')  # 从cookie中取值
        rslt = UserAccount().delete(id=id,delete_by=delete_by)
    return HttpResponse(rslt)
