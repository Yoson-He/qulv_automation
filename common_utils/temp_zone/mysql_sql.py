#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# @Time    : 2017/11/24 17:42
# @Author  : HoxHou
# @File    : mysql_sql.py
# @Software: PyCharm Community Edition







#
# query_type_2 = 'this'
# extend_query(query_type_2)





# @weighting(query_type='or')
# def myfunc(s,**kwargs):
#     p=s+1
#     print(s,p,kwargs)
#     return p




# @weighting(query_type_1=10)
# def que(query_type, *args, **kwargs):
#     # args = ["`" + "`,`".join(list(args)) + "`", '*'][len(args) is 0]
#     # cond = ["WHERE " + self.__query_condition_(query_type, **kwargs), ''][len(kwargs) is 0]
#     # sql = "SELECT {fields} FROM {table} ".format(fields=args, table=self.db_table) + cond
#     # print(sql)
#     print(query_type,*args,**kwargs)
#
# shh=122
# que(3,shh,dict_ss=5)






# 查询加权装饰器
# def weighting(query_type):
#     def _pump(func):
#         def __kernel(**kwargs):
#             print(kwargs)
#             func(query_type, **kwargs)
#
#         return __kernel
#
#     return _pump
#
# # query_type=3
#
# @weighting(query_type=3)
# def myfunc(s,**kwargs):
#     p=s+1
#     print(s,p,kwargs)
#     return p
#
# dict={'name' : 'alam' ,'age' :12}
# myfunc(**dict)


# def deco(func):
#     print("before myfunc() called.")
#     func()
#     print("  after myfunc() called.")
#     return func
#
#
# @deco
# def myfunc():
#     print(" myfunc() called.")
