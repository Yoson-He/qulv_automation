#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# @Time    : 2017/11/24 15:23
# @Author  : HoxHou
# @File    : bs4_demo.py
# @Software: PyCharm Community Edition



import requests
from bs4 import BeautifulSoup



url='http://main.qboss-product.next.qulv.com/Inventory/CountryCity/Index'
res=requests.get(url)
content = res.text  # 获取网页源码
print(content)
soup=BeautifulSoup(content,'html.parser')
for src in soup.select('src'):  #因为图片存在img标签里，因此select里选取img标签
    print(src)



print("<-------%%%%-------->")

url_login = 'http://qhub.next.qulv.com'
browser = webdriver.PhantomJS(executable_path=PhantomJS())
browser.get(url_login)
browser.find_element_by_id('Username').send_keys("admin")
browser.find_element_by_id('Password').send_keys('123')
browser.find_element_by_class_name("btn-submit").click()
# 获得 cookie信息



cookie = ";".join([item["name"] + "=" + item["value"] for item in browser.get_cookies()])
print(cookie)
query_url = "http://main.qboss-product.next.qulv.com/Product/UniveseProduct/Index"

result = requests.request(url=query_url, method='GET',
                          data=None, headers=None, cookies=dict(Cookie=cookie))
print(result.text)
browser.quit()
# header = {
# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
# 'Connection': 'keep-alive',
# 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
# }
#
