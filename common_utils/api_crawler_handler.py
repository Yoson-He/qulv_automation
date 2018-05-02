#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# @Time    : 2017/12/4 10:56
# @Author  : HoxHou
# @File    : api_crawler_handler.py
# @Software: PyCharm Community Edition

import pickle
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from common_utils.selenium.webdriver import chrome, PhantomJS


class APICrawler(object):
    def __init__(self,login_url,user_name,password):
        self.login_url=login_url
        self.user_name=user_name
        self.password=password

    def get_cookies(self):
        browser = webdriver.PhantomJS(executable_path=PhantomJS())
        browser.get(self.login_url)
        browser.find_element_by_id('Username').send_keys(self.user_name)
        browser.find_element_by_id('Password').send_keys(self.password)
        browser.find_element_by_class_name("btn-submit").click()
        # 获得 cookie信息
        cookie_list = browser.get_cookies()
        # print(cookie_list)
        browser.quit()
        cookie_dict = {}
        for cookie in cookie_list:
            # 写入文件
            f = open(cookie['name'] + '.txt', 'w')
            pickle.dump(cookie, f)
            f.close()

        return cookie_dict





login_url="http://qhub.next.qulv.com"
user_name="admin"
password="123"
# API_Crawler(login_url,user_name,password).get_cookies()