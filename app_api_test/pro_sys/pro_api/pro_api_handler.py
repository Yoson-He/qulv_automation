#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# @Time    : 2017/12/6 16:34
# @Author  : HoxHou
# @File    : pro_api_handler.py
# @Software: PyCharm Community Edition

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from app_api_test.pro_sys.pro_api.pro_api_mapper import ProApiMapper, ProReqSingleParamsMapper
from app_api_test.pro_sys.pro_api.pro_api_template import update, api_add_info, module_temp, \
    add_query_menu, edit_query_menu, query_menu, sub_module_temp
from common_utils.common import strClean
from common_utils.db_handler.mysql_engine import MySQLEngine


class ProApiHandler(object):
    def __init__(self):
        pass

    def api_list(self, page, limit):
        base_pro_api_list = MySQLEngine('pro_api').where('limit', state=1).limit(page=page, limit=limit)
        qboss_menu_list = MySQLEngine('q_boss_menu').where(state=1)
        api_list = ProApiMapper('menu_id').mapping(list=base_pro_api_list, relation_list=qboss_menu_list)
        paginator = Paginator(api_list, limit)  # Show 25 contacts per page
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)
        return contacts.object_list, len(api_list)

    def params_list(self, api_id):
        rslt = {}
        if api_id is None: return rslt
        base_pro_api_list = MySQLEngine('pro_api').where(api_id=api_id, state=1)
        rslt = ProReqSingleParamsMapper().mapping(list=base_pro_api_list)
        return rslt

    def api_add(self, QueryDict, create_by):
        try:
            key_list = []
            val_list = []
            module_val = None
            for key in QueryDict:
                if key[:-2] == 'key':
                    key_list.append(str(QueryDict[key]))
                elif key[:-2] == 'val':
                    val_list.append(str(QueryDict[key]))
            params_dict = dict(zip(key_list, val_list))
            query = add_query_menu()
            query['sys_name'] = QueryDict['sys_name']
            query['main_module'] = QueryDict['main_module']
            query['module'] = module_val
            query['sub_module'] = QueryDict['sub_module']
            query['state'] = 1
            menu_id_list = MySQLEngine('q_boss_menu').where(**query)
            if len(menu_id_list) is 0:
                menu_id = 0
            else:
                menu_id = menu_id_list[0]['menu_id']
            insert_dict = api_add_info()
            insert_dict['menu_id'] = menu_id,
            insert_dict['api_name'] = QueryDict.get('api_name', None),
            insert_dict['api_type'] = QueryDict.get('api_type', None),
            insert_dict['method'] = QueryDict.get('method', None),
            insert_dict['path'] = QueryDict.get('path', None),
            insert_dict['headers'] = QueryDict.get('headers', None),
            insert_dict['uri_params'] = QueryDict.get('uri_params', None),
            insert_dict['req_params'] = strClean(str(params_dict)),
            insert_dict['req_body'] = QueryDict.get('req_body', None),
            insert_dict['created_by'] = create_by,
            insert_dict['remark'] = QueryDict.get('remark', None),
            insert_dict['state'] = QueryDict.get('state', None),
            rslt = MySQLEngine('pro_api').insert_into(**insert_dict)
            return rslt
        except BaseException as e:
            print(e)

    def api_edit(self, QueryDict, update_by):
        try:
            print(QueryDict)
            req_key_list = []
            k_list = []
            req_val_list = []
            v_list = []
            module_val = None
            sys_name_val = None
            main_module_val = None
            sub_module_val = None
            api_id = QueryDict.get('api_id', None)
            if api_id is None:
                return None
            else:
                QueryList = []
                for key in QueryDict:
                    if key == 'api_id':
                        pass
                    elif key == 'data[csrfmiddlewaretoken]':
                        pass
                    elif key[5:-1][:-2] == 'key':
                        req_key_list.append(key[5:-1])
                    elif key[5:-1][:-2] == 'val':
                        req_val_list.append(key[5:-1])
                    elif key == 'sys_name':
                        sys_name_val = QueryDict['sys_name']
                    elif key == 'main_module':
                        main_module_val = QueryDict['main_module']
                    elif key == 'module':
                        module_val = QueryDict['module']
                    elif key == 'sub_module_val':
                        sub_module_val = QueryDict['sub_module_val']
                    elif key == 'api_name':
                        api_name = QueryDict['api_name']
                        total = MySQLEngine("pro_api").where_like(api_name=api_name, state=1)
                        if len(total) > 0: pass
                    else:
                        QueryList.append("%s" % (key[5:-1]))
                for req_key in req_key_list:
                    key_v = QueryDict.get('data[%s]' % req_key, None)
                    k_list.append(key_v)
                for req_val in req_val_list:
                    val_v = QueryDict.get('data[%s]' % req_val, None)
                    v_list.append(val_v)
                params_dict = dict(zip(k_list, v_list))
                query = edit_query_menu()
                query['sys_name'] = sys_name_val
                query['main_module'] = main_module_val
                query['module'] = module_val
                query['sub_module'] = sub_module_val
                query['state'] = 1
                menu_id_list = MySQLEngine('q_boss_menu').where(**query)
                QueryList.sort()
                if len(menu_id_list) is 0:
                    menu_id = 0
                else:
                    menu_id = menu_id_list[0]['menu_id']
                # 封装Template模版
                update_dict = update()
                update_dict['menu_id'] = menu_id
                update_dict['updated_by'] = update_by
                update_dict['req_params'] = str(params_dict)
                for i in QueryList:
                    if i in update_dict:
                        update_dict[i] = QueryDict.get('data[' + i + ']', None)
                rslt = MySQLEngine('pro_api').update_set(update_dict, api_id=api_id, state=1)
                return rslt
        except BaseException as e:
            print(e)

    def api_delete(self, api_id, update_by):
        update_dict = {'updated_by': update_by, 'state': 0}
        rslt = MySQLEngine('pro_api').update_set(update_dict, api_id=api_id, state=1)
        if rslt is str: rslt = 0
        return rslt


    def module_list(self, api_id, main_module):
        if main_module is None:
            return module_temp()
        module_list = MySQLEngine("q_boss_menu").where('group_by', main_module=main_module,
                                                       state=1).group_by('module')
        name_list = []
        data_list = []
        for module in module_list:
            module_name = module.get('module', '')
            name_list.append(module_name)
        for val in name_list:
            val_list = [val, val]
            key_list = ['code', 'name']
            key_val_list = dict(zip(key_list, val_list))
            data_list.append(key_val_list)
        if api_id is None:
            rslt = module_temp()
            rslt['data'] = data_list
            return rslt
        else:
            menu_id = MySQLEngine('pro_api').where(api_id=api_id, state=1)[0]['menu_id']
            clicked = MySQLEngine('q_boss_menu').where(menu_id=menu_id, state=1)[0]['sys_name']
            selected = MySQLEngine('q_boss_menu').where(menu_id=menu_id, state=1)[0]['module']
            rslt = module_temp()
            rslt['sys_name'] = clicked
            rslt['data'] = data_list
            rslt['module'] = selected
            return rslt

    def sub_module_list(self, api_id, module, main_module):
        if main_module is None or module is None:
            return sub_module_temp()
        query_list = query_menu()
        query_list['main_module'] = main_module
        query_list['module'] = module
        query_list['state'] = 1
        sub_module_list = MySQLEngine("q_boss_menu").where('group_by', **query_list).group_by('sub_module')
        name_list = []
        data_list = []
        for sub_module in sub_module_list:
            sub_module_name = sub_module.get('sub_module', '')
            name_list.append(sub_module_name)
        for val in name_list:
            val_list = [val, val]
            key_list = ['code', 'name']
            key_val_list = dict(zip(key_list, val_list))
            data_list.append(key_val_list)
        if api_id is None:
            rslt = sub_module_temp()
            rslt['data'] = data_list
            return rslt
        else:
            menu_id = MySQLEngine('pro_api').where(api_id=api_id, state=1)[0]['menu_id']
            selected = MySQLEngine('q_boss_menu').where(menu_id=menu_id, state=1)[0]['sub_module']
            rslt = sub_module_temp()
            rslt['data'] = data_list
            rslt['sub_module'] = selected
            return rslt

    def import_api(self, api_info_channel):
        pass
