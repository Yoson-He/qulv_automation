# -*- coding: utf-8 -*-
# @Time    : 2017/11/21 10:02
# @Author  : Yoson
# @File    : common.py
# @Software: PyCharm
import sys,time
import operator
import json
import requests
import re
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header

def strClean(string):
    """清除空格和换行符,把中文逗号，引号换成英文符号"""
    try:
        string = string.replace(" ", "").replace("\n", "").replace("，", ",").replace("“", "\'").replace("”", "\'").replace("‘", "\'").replace("’", "\'").replace("\r", "").replace("；", ";")
        string=string.replace("\"", "\'").replace("：", ":")
        return string
    except Exception:
        print("字符处理出错！！！")

def pathProcessor(path):
    """替换path中的参数占位符，如：api/LocalTours/{id}/prices/{useDate}?date={date} 替换成 api/LocalTours/%s/prices/%s?date=%s"""
    return re.sub(r"{.*?}", "%s", path, count=0)

def urlHandle(host, path, uri_params_value):
    path = pathProcessor(path)  # 替换path中的参数占位符
    if uri_params_value is None:
        i = 0
    else:
        uri_params_value = uri_params_value.split(",")  # 有多个参数时，以逗号分隔，返回一个参数值列表
        i = len(uri_params_value)
    # uri参数值拼接到path上
    if path.count("%s") != i:
        print("参数个数与参数值个数不匹配！！！path：%s，uri_params_value：%s" % (path, uri_params_value))
        return 'uri参数个数不匹配'
    elif path.count("%s") != 0:
        path = path % tuple(uri_params_value)  # 把path中的占位符%s替换为具体的参数值
    url = "http://" + host + "/" + path
    return url

def dataHandle(host, api_list, testCase_list):
    """处理获取的测试数据，拼装URL，返回一个可执行的测试用例列表"""
    try:
        # 替换path中的参数占位符
        api_count = len(api_list)
        for i in range(api_count):
            api_list[i]["path"] = pathProcessor(api_list[i]["path"])
        testCase_count = len(testCase_list)
        for i in range(testCase_count):
            uri_params_value = testCase_list[i]["uri_params_value"].split(",")  # 获取用例uri参数值，有多个参数时，以逗号分割，返回一个参数值列表

            # 把用例的uri参数值拼接到对应api的path上
            for j in range(api_count):
                if testCase_list[i]["api_id"] == api_list[j]["api_id"]:
                    if api_list[j]["path"].count("%s") != len(uri_params_value):
                        print("参数个数与参数值个数不匹配！！！id：%s，api_id：%s" % (testCase_list[i]["id"], testCase_list[i]["api_id"]))
                        sys.exit()

                    path = api_list[j]["path"]%tuple(uri_params_value)  # 把path中的占位符%s替换为具体的参数值
                    url = "http://" + host + "/" + path
                    testCase_list[i]["url"] = url
                    testCase_list[i]["method"] = api_list[j]["method"]
                    testCase_list[i]["headers"] = api_list[j]["headers"]
                    break
                if j == api_count-1:
                    print("用例找不到对应的api！！！，id：%s"%testCase_list[i]["id"])
                    sys.exit()
        print("数据处理完成")
        return testCase_list
    except Exception:
        print("数据处理出错！！！")
        sys.exit()

def runTest(testCase_list):
    """执行测试用例，返回测试结果"""
    try:
        test_result_all = []
        all_count = len(testCase_list)
        pass_count = 0
        fail_count = 0
        for testCase in testCase_list:
            headers = testCase["headers"]
            if headers != "":
                try:
                    headers = eval(headers)
                except Exception:
                    return '请求头格式有误'

            if testCase["method"] in["post", "POST"]:
                t = time.time()
                respone_body = requests.request("post", testCase["url"], data=testCase["req_body_value"], headers=headers)
                t = t - time.time()
            elif testCase["method"] in["get", "GET"]:
                t = time.time()
                respone_body = requests.request("get", testCase["url"], params=testCase["req_params_value"],  headers=headers)
                t = t - time.time()
            expected_result = strClean(str(testCase["expected_result"]))
            checkout = actual_result_check(respone_body, expected_result)
            if checkout is None:
                return '预期结果格式输入有误'

            test_result_all.append({"case_id": testCase["case_id"], "api_id": testCase["api_id"], "pass_or_fail": checkout[0], "status_code": checkout[1], "url": testCase["url"], "actual_result": checkout[2], "response_body": respone_body.text, "expected_result": expected_result, "headers": str(respone_body.headers)})
        print("用例已执行完\n本次执行用例总数：%s， 通过%s个，失败%s个" % (all_count, pass_count, fail_count))
        return test_result_all, all_count, pass_count, fail_count
    except Exception:
        print("执行用例出错！！！")
        sys.exit()

def actual_result_check(respone_body,expected_result):
    actual_result = []
    pass_or_fail = 'PASS'
    status_code = respone_body.status_code
    expected_result = expected_result.split(";")
    for each in expected_result:
        if re.match(r'test\[(.*?)]:(.*)', each) is not None:
            name = re.match(r'test\[(.*?)]:(.*)', each).group(1)
            string = re.match(r'test\[(.*?)]:(.*)', each).group(2)
            check = 'PASS'
            #print(name+ '  '+string)

            #状态码等于
            if re.match(r'responseCode==(.*)', string) is not None:
                if str(status_code) != re.match(r'responseCode==(.*)', string).group(1):
                    check = 'FAIL'
                    pass_or_fail = 'FAIL'

            #返回值等于

            elif re.match(r'responseBody==(.*)', string) is not None:
                if strClean(respone_body.text) != strClean(re.match(r'responseBody==(.*)', string).group(1)):
                    check = 'FAIL'
                    pass_or_fail = 'FAIL'

            #返回值包含
            elif re.match(r'responseBody.has\((.*)\)', string) is not None:
                if re.match(r'responseBody.has\((.*)\)', string).group(1) not in respone_body.text:
                    check = 'FAIL'
                    pass_or_fail = 'FAIL'

            #检查一个json值
            elif re.match(r'data\[(.*?)]==(.*)', string) is not None:
                key = re.match(r'data\[(.*?)]==(.*)', string).group(1)
                value = re.match(r'data\[(.*?)]==(.*)', string).group(2)

                if key in respone_body.json():
                    if type(respone_body.json()[key]) in (int, float):
                        value = float(value)
                    if respone_body.json()[key] != value:
                        check = 'FAIL'
                        pass_or_fail = 'FAIL'
                elif key in respone_body.json()['Data']:
                    if type(respone_body.json()['Data'][key]) in (int, float):
                        try:
                            value = float(value)
                        except Exception:
                            pass
                    if value in ['null', 'NULL']:
                        value = None
                    if respone_body.json()['Data'][key] != value:
                        check = 'FAIL'
                        pass_or_fail = 'FAIL'
                else:
                    check = 'FAIL'
                    pass_or_fail = 'FAIL'
            else:
                return None
            actual_result.append(check+'：'+name+'\r')
        else:
            return None

    return pass_or_fail, status_code, actual_result

def resultProcessor(test_result_all,all_count, pass_count, fail_count):
    # 处理测试结果，格式化测试报告
    test_report = "<html><body><p>本次执行用例总数：%s， 通过%s个，失败%s个" % (all_count, pass_count, fail_count)
    test_report += "<p><table border='1px'><tr><th>status</th><th>status_code</th><th>id</th><th>api_id</th><th>expected_result</th><th>test_result</th></tr>"
    for each in test_result_all:
        test_report += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (each["status"], each["status_code"], each["id"], each["api_id"], each["expected_result"], each["actual_result"])

    test_report += "</table></body></html>"

    return test_report

def sendMail(text):
    try:
        sender = "TestAutomated@qulv.com"  # 发件人邮箱账号
        password = "ABCabc123"  # 发件人邮箱密码
        receivers = ["yongzhen-he@qulv.com", "Hox@qulv.com"]  # 收件人邮箱账号

        msg = MIMEText(text, "html", "utf-8")
        msg["From"] = formataddr(["接口自动化", sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg["To"] = str(receivers)[1:-1]  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg["Subject"] = "接口测试报告"        # 邮件主题
     
        server = smtplib.SMTP("mail.qulv.com", 25)  # 创建邮件服务器连接
        server.starttls() #TLS加密
        server.login(sender, password)  # 登录邮件服务器，括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(sender, receivers, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        print("邮件发送成功")
    except smtplib.SMTPException as reason:
        print(reason)
        sys.exit()






