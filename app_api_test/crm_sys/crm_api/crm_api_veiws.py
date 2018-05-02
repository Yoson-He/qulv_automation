#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# @Time    : 2017/12/6 9:47
# @Author  : HoxHou
# @File    : crm_api_veiws.py
# @Software: PyCharm Community Edition

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt





@csrf_exempt
def api_unit_page(request):
    return render(request, '../templates/sys_main/user_from.html')