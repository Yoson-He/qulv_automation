#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# @Time    : 2017/12/4 15:02
# @Author  : HoxHou
# @File    : webdriver.py
# @Software: PyCharm Community Edition


import os


def chrome():
    return os.path.split(os.path.realpath(__file__))[0] + '\\chromedriver.exe'


def PhantomJS():
    return os.path.split(os.path.realpath(__file__))[0] + '\phantomjs-2.1.1-windows\\bin\phantomjs.exe'
