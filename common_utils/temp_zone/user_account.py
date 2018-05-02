#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# @Time    : 2017/9/19 15:03
# @Author  : HoxHou
# @File    : user_account_views.py
# @Software: PyCharm Community Edition
import hashlib

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from app_sys_management.sys_user.user_account import UserAccount


@csrf_exempt
def sys_user_account(request):
    user_name = request.COOKIES.get('user_name')  # 从cookie中取值
    if user_name:
        List = UserAccount().sys_user_list()
        return render(request, '../templates/sys_menu/user_account-bakup.html', {'List': List})
    else:
        return redirect('/')


@csrf_exempt
def user_from(request):
    return render(request, '../templates/sys_menu/user_from.html')


@csrf_exempt
def user_add(request):
    global rslt
    if request.method == 'POST':
        user_name = request.POST.get('user_name', '')
        password = request.POST.get('repass', '')
        user_role = request.POST.get('user_role', '')
        phone = request.POST.get('phone', '')
        create_by = request.COOKIES.get('user_name')  # 从cookie中取值
        rslt = UserAccount().add(user_name=user_name, password=password, create_by=create_by, user_role=user_role,
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
