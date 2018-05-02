#!/var/python3/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/9/10 21:14
# @Author  : HoxHou
# @File    : index.py
# @Software: PyCharm Community Edition

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponseRedirect, HttpResponse
from app_sys_main.sys_user.user_account import UserAccount
from common_utils.cryptographic_algorithm.make_password import Encryption


# Create your views here.
# @csrf_protect
@csrf_exempt
def login(request):
    user_name = request.COOKIES.get('user_name')  # 从cookie中取值
    if user_name:
        return render(request, '../templates/sys_main/index.html', {'user_name': user_name})
    else:
        if request.method == 'POST':
            user_name = request.POST.get('user_name', '')
            password = request.POST.get('password', '')
            # Django自带的账号认证
            # user = authenticate(username=user_name, password='123456')  # 类型为<class 'django.contrib.auth.models.User'>
            salt_password = Encryption(password).md5_salt()
            user = UserAccount().authenticate(user_name=user_name, password=salt_password)
            print(user)
            if user:
                hrr = HttpResponseRedirect("index/")  # 登录成功，则重定向到index
                hrr.set_cookie('user_name', user, max_age=3600)  # 将用户名插入cookie
                return hrr
            else:
                return render(request, '../templates/sys_main/login.html')
        else:
            return render(request, '../templates/sys_main/login.html')


@csrf_exempt
def logout(request):
    response = HttpResponse('success !!')
    # 清理cookie里保存user_name
    response.delete_cookie('user_name')
    return response


@csrf_exempt
def index(request):
    user_name = request.COOKIES.get('user_name')  # 从cookie中取值
    if user_name:
        return render(request, '../templates/sys_main/index.html', {'user_name': user_name})
    else:
        return redirect('/')


@csrf_exempt
def home(request):
    user_name = request.COOKIES.get('user_name')  # 从cookie中取值
    if user_name:
        return render(request, '../templates/sys_main/home.html')
    else:
        return redirect('/')
