#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# @Time    : 2017/11/24 13:54
# @Author  : HoxHou
# @File    : inv_center_api.py
# @Software: PyCharm Community Edition
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from common_utils.db_handler.mysql_engine import MySQLEngine


class inv_center_api(object):
    def __init__(self):
        pass

    def api_list(self, page, limit):
        contact_list = MySQLEngine('pro_api').where(state=1)
        paginator = Paginator(contact_list, limit)  # Show 25 contacts per page
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)
        return contacts.object_list, len(contact_list)

    def add(self, QueryDict, create_by):
        try:
            key_list = []
            val_list = []
            for k in QueryDict:
                if k[:-2] == 'key':
                    key_list.append(str(QueryDict[k]))
                elif k[:-2] == 'val':
                    val_list.append(str(QueryDict[k]))
            params_dict = dict(zip(key_list, val_list))
            rslt = MySQLEngine('pro_api').insert_into(module=QueryDict.get('module', None),
                                                                 sub_module=QueryDict.get('sub_module', None),
                                                                 api_name=QueryDict.get('api_name', None),
                                                                 api_type=QueryDict.get('api_type', None),
                                                                 method=QueryDict.get('method', None),
                                                                 path=QueryDict.get('path', None),
                                                                 headers=QueryDict.get('headers', None),
                                                                 uri_params=QueryDict.get('uri_params', None),
                                                                 req_params=str(params_dict),
                                                                 req_body=QueryDict.get('req_body', None),
                                                                 create_by=create_by,
                                                                 remark=QueryDict.get('remark', None),
                                                                 state=QueryDict.get('state', None),
                                                                 )
            return rslt
        except BaseException as e:
            print(e)

    def edit(self, QueryDict, update_by):
        try:
            req_key_list = []
            k_list = []
            req_val_list = []
            v_list =[]
            id = QueryDict.get('id', None)
            QueryList = []
            for key in QueryDict:
                if key == 'id':
                    pass
                elif key == 'data[csrfmiddlewaretoken]':
                    pass
                elif key[5:-1][:-2] == 'key':
                    req_key_list.append(key[5:-1])
                elif key[5:-1][:-2] == 'val':
                    req_val_list.append(key[5:-1])
                else:
                    QueryList.append("" + key[5:-1] + "")
            for req_key in req_key_list:
                key_v=QueryDict.get('data[%s]'%req_key, None)
                k_list.append(key_v)
            for req_val in req_val_list:
                val_v=QueryDict.get('data[%s]'%req_val, None)
                v_list.append(val_v)
            params_dict = dict(zip(k_list, v_list))
            QueryList.sort()
            # 封装Page类
            update_dict = {
                'api_name': None,
                'api_type': None,
                'req_body': None,
                'uri_params': None,
                'req_params': None,
                'headers': None,
                'method': None,
                'module': None,
                'remark': None,
                'state': None,
                'path': None,
                'sub_module': None,
                'update_by': None
            }
            update_dict['id'] = id
            update_dict['update_by'] = update_by
            update_dict['req_params'] = str(params_dict)
            for i in QueryList:
                update_dict[i] = QueryDict.get('data[' + i + ']', None)
            rslt = MySQLEngine('pro_api').update_set(update_dict, id=id)
            return rslt
        except BaseException as e:
            print(e)

    def delete(self, id, update_by):
        me = MySQLEngine('pro_api')
        update_dict = {'update_by': update_by, 'state': 0}
        rslt = me.update_set(update_dict, id=id)
        if rslt is str: rslt = 0
        return rslt

    def sub_module_list(self, module):
        sub_module_list = MySQLEngine('q_boss_sys_menu').where(module=module)
        list = []
        rslt_list = []
        for sub_module in sub_module_list:
            sub_module_name = sub_module.get('sub_module', '')
            list.append(sub_module_name)
        for val in list:
            val_list = [val, val]
            key_list = ['code', 'name']
            rslt = dict(zip(key_list, val_list))
            rslt_list.append(rslt)
        return rslt_list

    def edit_sub_module(self, api_id):
        if api_id is None:
            sub_module = None
        else:
            api_info = MySQLEngine('pro_api').where(id=api_id)
            sub_module = api_info[0].get('sub_module')
        return sub_module
