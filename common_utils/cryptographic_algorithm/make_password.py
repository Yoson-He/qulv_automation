#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# @Time    : 2017/11/15 10:37
# @Author  : HoxHou
# @File    : make_password.py
# @Software: PyCharm Community Edition
import hashlib


class Encryption(object):
    def __init__(self, password):
        self.password = password

    def md5_salt(self):
        # ====  MD5加盐  ====#
        md5 = hashlib.md5('qulv_test'.encode('utf-8'))
        md5.update(self.password.encode('utf-8'))
        return md5.hexdigest()

    def make_password(self):
        md5 = hashlib.md5()
        md5.update(self.password.encode('utf-8'))
        # ====  sha1  ====#
        sha1 = hashlib.sha1()
        sha1.update(self.password.encode('utf-8'))
        return md5.hexdigest() + sha1.hexdigest()
