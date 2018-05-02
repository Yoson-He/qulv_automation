#!/var/python3/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/12/7 21:57
# @Author  : HoxHou
# @File    : pro_api_mapper.py
# @Software: PyCharm Community Edition
from app_api_test.pro_sys.pro_api.pro_api_template import qboss_menu
from common_utils.common import strClean

class ProApiMapper(object):
    def __init__(self, matching):
        self.matching = matching

    def mapping(self, **kwargs):
        qboss_menu_list = []
        pro_api_list = []
        for template in kwargs['relation_list']:
            extend = qboss_menu()
            for key in extend:
                extend[key] = template[key]
            qboss_menu_list.append(extend)
        for pro_api_dict in kwargs['list']:
            for qboss_menu_dict in qboss_menu_list:
                if pro_api_dict[self.matching] == qboss_menu_dict[self.matching]:
                    pro_api_list.append({**pro_api_dict, **qboss_menu_dict})
        return pro_api_list



class ProReqParamsMapper(object):
    def __init__(self, matching):
        self.matching = matching

    def mapping(self, **kwargs):
        # 创建赋值
        key_val_list = []
        for i in range(0, len(kwargs['list'])):
            key_list = []
            val_list = []
            key_dict = {}
            val_dict = {}
            req_params = strClean(kwargs['list'][i]['req_params'])
            req_params_dict = eval(req_params)
            for key in req_params_dict:
                key_list.append(key)
                val_list.append(req_params_dict[key])
            for num in range(len(req_params_dict)):
                key_dict['api_id'] = kwargs['list'][i]['api_id']
                key_dict['key-' + str(num + 1)] = key_list[num]
                val_dict['val-' + str(num + 1)] = req_params_dict[key_list[num]]
            key_val_list.append(dict(key_dict, **val_dict))
        # 合并
        pro_api_list = []
        for pro_api_dict in kwargs['list']:
            for req_params_dict in key_val_list:
                if pro_api_dict[self.matching] == req_params_dict[self.matching]:
                    pro_api_list.append({**pro_api_dict, **req_params_dict})
        return pro_api_list


class ProReqSingleParamsMapper(object):
    def __init__(self):
        pass
    def mapping(self, **kwargs):
        # 创建赋值
        key_val_dict = {}
        for i in range(0, len(kwargs['list'])):
            key_list = []
            val_list = []
            key_dict = {}
            val_dict = {}
            req_params = strClean(kwargs['list'][i]['req_params'])
            req_params_dict = eval(req_params)
            for key in req_params_dict:
                key_list.append(key)
                val_list.append(req_params_dict[key])
            for num in range(len(req_params_dict)):
                key_dict['api_id'] = kwargs['list'][i]['api_id']
                key_dict['key_' + str(num + 1)] = key_list[num]
                val_dict['val_' + str(num + 1)] = req_params_dict[key_list[num]]
            key_val_dict=dict(key_dict, **val_dict)
        return key_val_dict