#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# @Time    : 2017/11/15 10:06
# @Author  : HoxHou
# @File    : user_account_views.py
# @Software: PyCharm Community Edition


from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from common_utils.cryptographic_algorithm.make_password import Encryption
from common_utils.db_handler.mysql_engine import MySQLEngine


class UserAccount(object):
    def __init__(self):
        pass

    def sys_user_list(self, page, limit):
        contact_list = MySQLEngine('sys_user').where(state=1)
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

    def authenticate(self, user_name, password):
        """
        需要添加判重
        :param user_name:
        :param password:
        :return:
        """
        user_list = MySQLEngine('sys_user').where(user_name=user_name, password=password, state=1)
        if len(user_list) == 0 or len(user_list) > 1:
            user_name = '账号异常！！'
        elif len(user_list) == 1:
            user_name = user_list[0].get('user_name', '')
        return user_name

    def query(self, user_name, id):
        user_list = MySQLEngine('sys_user').where_or(user_name=user_name, id=id)
        return user_list[0].get('user_name', '')

    def add(self, user_name, realName, password, create_by, user_role, phone):
        try:
            num = 0
            if user_name is None or user_name is '': num += 1
            if password is None or password is '': num += 1
            if create_by is None or create_by is '': num += 1
            if user_role is None or user_role is '': num += 1
            password = Encryption(Encryption(password).make_password()).md5_salt()
            phone = [phone, ''][phone is None or phone is '']
            diff_name = MySQLEngine('sys_user').where(user_name=user_name)
            if len(diff_name) > 0:
                rslt = 2
            else:
                if 0 < num <= 4:
                    rslt = 0
                else:
                    me = MySQLEngine('sys_user')
                    rslt =me.insert_into(user_name=user_name, realName=realName, password=password, create_by=create_by,
                                   user_role=user_role,
                                   phone=phone)
            return rslt
        except BaseException as e:
            print(e)

    def delete(self, id, delete_by):
        """
        软删除，使用update修改状态，不用delete
        :param id:
        :param delete_by:
        :return:
        """
        me = MySQLEngine('sys_user')
        # rslt = me.delete(id=id)
        update_dict = {'update_by': delete_by, 'state': 0}
        rslt = me.update_set(update_dict, id=id)
        return rslt
