#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# @Time    : 2017/11/24 15:23
# @Author  : HoxHou
# @File    : bs4_demo.py
# @Software: PyCharm Community Edition




import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from common_utils.selenium.webdriver import chrome, PhantomJS

url='http://qhub.next.qulv.com'
browser = webdriver.Chrome(chrome())
browser.get(url)
browser.find_element_by_id('Username').send_keys("admin")
browser.find_element_by_id('Password').send_keys('123')
browser.find_element_by_class_name("btn-submit").click()
cookiestr=";".join([item["name"] + "=" + item["value"] for item in browser.get_cookies()])
browser.quit()
query_url="http://main.qboss-product.next.qulv.com/Inventory/CountryCity/Index"
result = requests.request(url=query_url, method='POST',data=None,
                          headers=None,cookies=dict(cookies_are=cookiestr))
content = result.text

soup=BeautifulSoup(content,'html.parser')
for script in soup.select('script'):
    print(script)

