#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# @Time    : 2017/11/24 16:40
# @Author  : HoxHou
# @File    : sps.py
# @Software: PyCharm Community Edition


# 查询加权装饰器
def weighting(query_type_1):
    print(query_type_1)
    def _pump(func):
        def __kernel(query_type_2,*args, **kwargs):
            query_type_3 =query_type_2+query_type_1
            print(query_type_2,args, kwargs,'this')
            d=kwargs.items()
            func(query_type_3,args,**kwargs )

        return __kernel

    return _pump


# @weighting(query_type='or')
# def myfunc(s,**kwargs):
#     p=s+1
#     print(s,p,kwargs)
#     return p




@weighting(query_type_1=10)
def que(query_type, *args, **kwargs):
    # args = ["`" + "`,`".join(list(args)) + "`", '*'][len(args) is 0]
    # cond = ["WHERE " + self.__query_condition_(query_type, **kwargs), ''][len(kwargs) is 0]
    # sql = "SELECT {fields} FROM {table} ".format(fields=args, table=self.db_table) + cond
    # print(sql)
    print(query_type,*args,kwargs)

shh=122
# dict_ss={'ll':123}
que(3,shh,dict_ss=5)