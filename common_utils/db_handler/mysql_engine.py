#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# @Time    : 2017/11/14 15:45
# @Author  : HoxHou
# @File    : mysql_engine.py
# @Software: PyCharm Community Edition




import re

import pymysql

from config.config_handler import conf


class MySQLEngine(object):
    def __init__(self, db_table):
        """
        MySQL 数据库ORM
        :param db_table:
        """

        self.db_table = db_table
        self.host = conf.get('mysql', 'host')
        self.user = conf.get('mysql', 'user')
        self.password = conf.get('mysql', 'password')
        self.charset = conf.get('mysql', 'charset')
        self.db = conf.get('mysql', 'name')
        try:
            conn = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                   database=self.db, charset=self.charset, connect_timeout=100)
        except pymysql.Error:
            raise
        self.__conn = conn

    def __execute(self, type, sql):
        """

        :param type:
        :param sql:
        :return:
        """
        try:
            print(sql)  # 后期保存到日志模块
            self.cursor = self.__conn.cursor()
            if type is 'query':
                self.cursor.execute(sql)
                data_list = self.cursor.fetchall()
                # print(data_list)
                print("totals:%d" % (len(data_list)))
                db_fields = [desc[0] for desc in self.cursor.description]
                # print(db_fields)
                result = []
                for row in data_list:
                    objDict = {}
                    # 字典键值对
                    for index, value in enumerate(row):
                        objDict[db_fields[index]] = value
                    result.append(objDict)
                # print(result)#后期保存到日志模块
                return result
            elif type in ('insert', 'update', 'delete'):
                try:
                    self.cursor.execute(sql)
                    self.__conn.commit()
                    print("受影响的行：%d" % (self.cursor.rowcount))
                    return self.cursor.rowcount
                except pymysql.Error:
                    raise
        finally:
            self.__conn.close()

    def __query(self, query_type, correlation=None, extend_type=None, *args, **kwargs):
        """
        
        :param query_type: 
        :param correlation: 
        :param extend_type: 
        :param args: 
        :param kwargs: 
        :return: 
        """
        args = ["`%s`" % "`,`".join(list(args)), '*'][len(args) is 0]
        if query_type is 'table':
            cond = ["WHERE " + self.__query_condition_(query_type, correlation, **kwargs), ''][len(kwargs) is 0]
        else:
            cond = ["WHERE " + self.__query_condition_(query_type, correlation, **kwargs), 'WHERE'][len(kwargs) is 0]
        sql = "SELECT {fields} FROM {table} ".format(fields=args, table=self.db_table) + cond
        if extend_type is None:
            action = self.__execute('query', sql)
        else:
            action = sql
        return action

    @staticmethod
    def __query_condition_(query_type, correlation, **kwargs):
        """
        
        :param query_type: 
        :param correlation: 
        :param kwargs: 
        :return: 
        """
        cond_str = []
        for key, value in kwargs.items():
            if value == None:
                continue
            key = [key, key[0:len(key) - 1]][re.sub("\D", "", key) is not '' and int(re.sub("\D", "", key)) > 1]
            if type(value) is list:
                return "%s IN (%s)" % (key, str(value).split('[')[1].split(']')[0])
            elif query_type in ('!=', '>', '<', '>=', '<='):
                cond_str.append(("`%s` %s \"%s\"" % (key, query_type, value)))
            elif query_type is 'like':
                cond_str.append(("`%s` %s \"%%%s\"" % (key, query_type, value)))
            else:
                cond_str.append(("`%s`=\"%s\"" % (key, value)))
        cond_str = [' AND '.join(cond_str), ' OR '.join(cond_str)][correlation is 1]
        return cond_str

    def insert_into(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        keys_list = []
        vals_list = []
        for key, value in kwargs.items():
            keys_list.append("%s" % key)  # sql server 需要加上[]
            vals_list.append("\"%s\"" % value)
        keys = ','.join(keys_list)
        vals = ','.join((vals_list))
        sql = "INSERT INTO %s (%s) VALUES (%s)" % (self.db_table, keys, vals)
        return self.__execute('insert', sql)

    def update_set(self, update_dict, **kwargs):
        """

        :param update_dict:
        :param kwargs:
        :return:
        """
        update_fields = []
        for keys, value in update_dict.items():
            update_fields.append("%s=\"%s\"" % (keys, value))  # sql server 需要加上[]
        cond = self.__query_condition_('=', 0, **kwargs)
        sql = "UPDATE %s SET %s WHERE %s" % (self.db_table, ','.join(update_fields), cond)
        return self.__execute('update', sql)

    def delete_where(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        cond = self.__query_condition_('=', 0, **kwargs)
        sql = "DELETE FROM %s WHERE %s" % (self.db_table, cond)
        return self.__execute('delete', sql)

    @classmethod
    def __weighting(cls, sql, db_table, extend_type=None):
        return Extend(cls, sql, db_table, extend_type)

    def table(self):
        """

        :return:
        """
        return self.__query('table')

    def where(self, extend_type=None, *args, **kwargs):
        """
        fields1=val1
        fields2=val2
        MySQLEngine("table_name").where('and',fields1,fields2,dict1=val1, dict2=val2).like('and',dict1=val1,dict2=val2)
        :param extend_type:
        :param args:
        :param kwargs:
        :return:
        """
        if  extend_type not in ('and', 'or', 'limit', 'group_by'):
            return self.__query('=', 0, *args, **kwargs)
        else:
            sql = self.__query('=', 0, extend_type, *args, **kwargs)
            return self.__weighting(sql, self.db_table, extend_type)

    def where_or(self, extend_type=None, *args, **kwargs):
        """

        :param extend_type:
        :param args:
        :param kwargs:
        :return:
        """
        if  extend_type not in ('and', 'or', 'limit', 'group_by'):
            return self.__query('=', 1, *args, **kwargs)
        else:
            sql = self.__query('=', 1, extend_type, *args, **kwargs)
            return self.__weighting(sql, self.db_table, extend_type)

    def where_like(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        return self.__query('like', 1, *args, **kwargs)

    def defined(self, type, sql):
        """

        :param type:1、query 2、insert  4、update 3、delete
        :param sql:
        :return:
        """
        return self.__execute(type, sql)


class Extend(object):
    def __init__(self, model, sql, db_table, extend_type=None):
        """

        :param model:
        :param sql:
        :param db_table:
        """
        self.extend_type = extend_type
        self.model = model
        self.sql = sql
        self.db_table = db_table
        self.host = conf.get('mysql', 'host')
        self.user = conf.get('mysql', 'user')
        self.password = conf.get('mysql', 'password')
        self.charset = conf.get('mysql', 'charset')
        self.db = conf.get('mysql', 'name')
        try:
            conn = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                   database=self.db, charset=self.charset, connect_timeout=100)
        except pymysql.Error:
            raise
        self.__conn = conn

    def __execute(self, type, sql):
        """

        :param type:
        :param sql:
        :return:
        """
        try:
            print(sql)  # 后期保存到日志模块
            self.cursor = self.__conn.cursor()
            if type is 'query':
                self.cursor.execute(sql)
                data_list = self.cursor.fetchall()
                # print(data_list)
                print("totals:%d" % (len(data_list)))
                db_fields = [desc[0] for desc in self.cursor.description]
                # print(db_fields)
                result = []
                for row in data_list:
                    objDict = {}
                    # 字典键值对
                    for index, value in enumerate(row):
                        objDict[db_fields[index]] = value
                    result.append(objDict)
                # print(result)#后期保存到日志模块
                return result
            elif type in ('insert', 'update', 'delete'):
                try:
                    self.cursor.execute(sql)
                    self.__conn.commit()
                    print("受影响的行：%d" % (self.cursor.rowcount))
                    return self.cursor.rowcount
                except pymysql.Error:
                    raise
        finally:
            self.__conn.close()

    def like(self, query_type=None, **kwargs):
        """

        :param query_type:
        :param kwargs:
        :return:
        """
        extend_type = ['', (self.extend_type).upper()][self.extend_type in ('and', 'or')]
        cond_str = []
        for key, value in kwargs.items():
            cond_str.append((" `%s` Like \"%%%s%%\"" % (key, value)))
        cond_str = (' %s ' % ([query_type.upper(), 'OR'][query_type is None])).join(cond_str)
        return self.__execute('query', self.sql + extend_type + cond_str)

    def limit(self, **kwargs):
        page = int(kwargs['page'])
        limit = int(kwargs['limit'])
        cond_str = " LIMIT %s,%s" % ((page - 1) * limit, (page * limit))
        return self.__execute('query', self.sql + cond_str)

    def group_by(self, grouping):
        cond_str = " GROUP BY `%s` " % (grouping)
        return self.__execute('query', self.sql + cond_str)







# MySQLEngine("sys_user").where('or', id=1, user_name=1).like('and', id=2, user_name='23')
# MySQLEngine("pro_api").where('limit', state=1).limit(page=1, limit=10)
# MySQLEngine("sys_user").where_like(id=2, user_name='admin')
# MySQLEngine("q_boss_menu").where('group_by', sys_name="订单系统").group_by('main_module')
# MySQLEngine("pro_api").where(state=1)