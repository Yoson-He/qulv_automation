#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Time    : 2017/8/9 14:44
# @Author  : HoxHou
# @File    : config_handler.py
# @Software: PyCharm Community Edition


import configparser
import os

"""
config配置文件
"""

class ConfigHandler:
    def get(self, section, key):
        """
         1.基本的读取配置文件
            -read(filename) 直接读取ini文件内容
            -sections() 得到所有的section，并以列表的形式返回
            -options(section) 得到该section的所有option
            -items(section) 得到该section的所有键值对
            -get(section,option) 得到section中option的值，返回为string类型
            -getint(section,option) 得到section中option的值，返回为int类型，还有相应的getboolean()和 getfloat() 函数。
        2.基本的写入配置文件
            -add_section(section) 添加一个新的section
            -set( section, option, value) 对section中的option进行设置，需要调用write将内容写入配置文件。
        :return:
        """
        try:
            config = configparser.ConfigParser()
            path = os.path.split(os.path.realpath(__file__))[0] + '\\public.conf'
            config.read(path)
            return config.get(section, key)
        except BaseException as error:
            return error


conf = ConfigHandler()
