#!/var/python3/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/12/7 22:36
# @Author  : HoxHou
# @File    : pro_api_template.py
# @Software: PyCharm Community Edition


def qboss_menu():
    template = {
        'menu_id': None,
        'sys_name': None,
        'main_module': None,
        'module': None,
        'sub_module': None
    }
    return template


def req_params():
    template = {
        'menu_id': None,
        'sys_name': None,
        'main_module': None,
        'module': None,
        'sub_module': None
    }
    return template


def api_add_info():
    template = {
        'menu_id': None,
        'api_name': None,
        'api_type': None,
        'method': None,
        'path': None,
        'headers': None,
        'uri_params': None,
        'req_params': None,
        'req_body': None,
        'created_by': None,
        'remark': None,
        'state': None,
    }
    return template


def add_query_menu():
    template = {
        'sys_name': None,
        'main_module': None,
        'module': None,
        'sub_module': None,
        'state': None
    }
    return template


def edit_query_menu():
    template = {
        'sys_name': None,
        'main_module': None,
        'module': None,
        'sub_module': None,
        'state': None
    }
    return template


def query_menu():
    template = {
        'main_module': None,
        'module': None,
        'sub_module': None,
        'state': None
    }
    return template


def update():
    template = {
        'api_name': None,
        'menu_id':None,
        'api_type': None,
        'req_body': None,
        'uri_params': None,
        'req_params': None,
        'headers': None,
        'method': None,
        'remark': None,
        'state': None,
        'path': None,
        'updated_by': None
    }
    return template


def main_module_temp():
    template = {
        "message": None,
        "main_module": None,
        "data": None,
    }
    return template


def module_temp():
    template = {
        "message": None,
        "module": None,
        "data": None,
    }
    return template


def sub_module_temp():
    template = {
        "message": None,
        "sub_module": None,
        "data": None,
    }
    return template

def import_temp():
    template = {
        "message": None,
        "sys_name": None,
        "sub_module": None,
        "data": None,
    }
    return template

