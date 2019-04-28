# import requests
# import bs4
# from bs4 import BeautifulSoup
# import json
#
# # r = requests.get('https://unsplash.com')
# # print(r.text)
#
# # data = {"applicationCode":"DPC","captcha":"","code":"15221738888","password":"738888"}
# #
# # re = requests.post('https://uat-gateway.dr-elephant.net/savr-biz/visitRecord/addIfNotExist', data=data)
# #
# # print(re.status_code)
#
#
# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# </body>
# </html>
# """
# soup = BeautifulSoup(html_doc, 'lxml')  # 声明BeautifulSoup对象
# find = soup.find('p')  # 使用find方法查到第一个p标签
# print("find's return type is ", type(find))  # 输出返回值类型
# print("find's content is", find)  # 输出find获取的值
# print("find's Tag Name is ", find.name)  # 输出标签的名字
# print("find's Attribute(class) is ", find['class'])  # 输出标签的class属性值
# print("NavigableString is：", find.string)       # 输出标签中文本内容（不包含标签）
#
# markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"     # 定义一个注释
# soup2 = BeautifulSoup(markup, 'lxml')    # 声明BeautifulSoup对象
# comment = soup2.b.string
# # comment = soup.p.string
# print("打印注释的类型", type(comment))    # 注释的类型
#
# if type(comment) == bs4.element.Comment:    # 通过字符串的类型来判断字符串是否为注释
#     print("%s 是注释！" % comment)
# else:
#     print("%s 不是注释！" % comment)
#
#
# print("head's content is", soup.head)   # 输出head标签的值
# print("title's content is", soup.title)     # 输出title标签的值
#
# print("***************************************************")
#
# # 对body标签的直接子节点进行循环打印
# for child in soup.body.children:
#     if child is None:
#         pass
#     else:
#         print(child.name)
#
# print("*****************************************************")
#
# # 对title标签的父节点进行循环打印
# for parent in soup.title.parents:
#     if parent is None:
#         print(parent)
#     else:
#         print(parent.name)
#
# print("****************************************************")
#
# # 对p标签的兄弟节点循环打印
# for sibling in soup.p.next_siblings:
#     print(repr(sibling))
#
# print("****************************************************")
#
# print(soup.find_all("title"))
# print(soup.find_all('p', "title"))
# print(soup.find_all('a'))
# print(soup.find_all(id='link2'))
#
# print("*********************************************************")
#
# appointStartTime = "19:50"
# appointEndTime = "19:55"
# visitStartTime = "2019-04-19 19:50:00"
# visitEndTime = "2019-04-19 19:55:00"
#
#
# data_appoint = {
#   "userCode": "13698000000",
#   "userName": "剧亚东",
#   "doctorCode": "15221738888",
#   "doctorName": "谢国勇1",
#   "orgCode": "110151",
#   "orgName": "北大医院",
#   "serviceCode": "42",
#   "serviceName": "专家门诊",
#   "servicePrice": 0,
#   "serviceType": "4",
#   "appointStartTime": appointStartTime,
#   "appointEndTime": appointEndTime,
#   "appointOrderTime": "2019-04-19",
#   "orderStatus": "10",
#   "doctorSchedulingCode": "7c7061339ea940ecaae66e613260a882",
#   "deptCode": "030200",
#   "deptName": "消化内科",
#   "status": "ACT",
#   "storeName": "check-美年大健康测试店",
#   "storeCode": "01006"
# }
#
# data_add = {
#   "userCode": "13698000000",
#   "userName": "剧亚东",
#   "doctorCode": "15221738888",
#   "doctorName": "谢国勇1",
#   "orgCode": "110151",
#   "orgName": "北大医院",
#   "serviceCode": "42",
#   "serviceName": "专家门诊",
#   "servicePrice": 0,
#   "serviceType": "4",
#   "appointStartTime": appointStartTime,
#   "appointEndTime": appointEndTime,
#   "appointOrderTime": "2019-04-19",
#   "orderStatus": "10",
#   "doctorSchedulingCode": "7c7061339ea940ecaae66e613260a882",
#   "deptCode": "030200",
#   "deptName": "消化内科",
#   "status": "ACT",
#   "storeName": "check-美年大健康测试店",
#   "storeCode": "01006"
# }
#
#
# headers = {
#   "content-type": "application/json",
#   "Accept": "*/*",
#   "token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ7XCJjb2RlXCI6XCIxMzY5ODAwMDAwMFwiLFwiYXBwbGljYXRpb25Db2RlXCI6XCJVUENcIn0iLCJleHAiOjE1NTYyNDQ4MTZ9.MEavNFqiTKFFiaPXHbcg2kS-mAC3e0aDBIoLVzOvTgFNo5R7ircRkpVCtvG_K8m3GXjz_3UTzm0C3j_3sz6IXg"
# }
#
# url_appoint = "https://uat-gateway.dr-elephant.net/savr-biz/appointDrPatient/saveAppoint"
# url_add = "https://uat-gateway.dr-elephant.net/savr-biz/appointDrPatient/add"
# url_order = "https://uat-gateway.dr-elephant.net/order-biz/orderInfo/createAlipayQrVideoOrder"
# url_visit = "https://uat-gateway.dr-elephant.net/savr-biz/visitRecord/addIfNotExist"
#
# re_appoint = requests.post(url_appoint, json=data_appoint, headers=headers)
# re_add = requests.post(url_add, json=data_add, headers=headers)
#
# # 处理re_add的返回内容 获取appiontCode
# appiontCode_value = re_add.json()["appiontCode"]
# print(re_add.json())
# print(appiontCode_value)
#
# data_order = {
#     "userCode": "13698000000",
#     "appointStartTime": appointStartTime,
#     "idCardNumber": "150422198207055113",
#     "phoneNumber": "13698000000",
#     "sex": "1",
#     "birthDate": "1982-07-05",
#     "userName": "剧亚东",
#     "thanksMoney": 0,
#     "serviceNumber": appiontCode_value,
#     "paymentAmount": 0,
#     "amount": 0,
#     "preAmount": "0.00",
#     "orderAmount": 0,
#     "doctorCode": "15221738888",
#     "doctorName": "谢国勇1",
#     "resetion": "消化内科",
#     "orgCode": "110151",
#     "orgName": "北大医院",
#     "storeName": "check-美年大健康测试店",
#     "storeCode": "01006",
#     "store": "01006",
#     "deviceType": "PC",
#     "serviceCode": "42",
#     "serviceType": "专家门诊",
#     "currentdate": "2019-04-19",
#     "allTime": visitStartTime,
#     "allTimeEnd": visitEndTime,
#     "orderDetail": [
#         {
#             "patiName": "剧亚东",
#             "resersection": "消化内科",
#             "serviceType": "专家门诊",
#             "serviceTypeCode": "42",
#             "reserDoctor": "谢国勇1",
#             "thanksMoney": 0,
#             "reservStore": "check-美年大健康测试店",
#             "reserTime": "2019-04-19 19:00:00",
#             "reserAmount": 0,
#             "patiNumber": "150422198207055113"
#         }
#     ]
# }
#
# print(data_order)
#
# re_order = requests.post(url_visit, json=data_order, headers=headers)
# print(re_order.json())
#
# data_visit = {
#     "appiontCode": appiontCode_value,
#     "doctorCode": "15221738888",
#     "doctorName": "谢国勇1",
#     "serviceCode": "42",
#     "serviceName": "专家门诊",
#     "storeName": "check-美年大健康测试店",
#     "storeCode": "01006",
#     "deptName": "消化内科",
#     "orgCode": "110151",
#     "orgName": "北大医院",
#     "visitEndTime": visitStartTime,
#     "visitStartTime": visitEndTime,
#     "deptCode": "030000",
#     "visitStatus": "100",
#     "phoneNumber": "13698000000",
#     "sex": "1",
#     "birthDate": "1982-07-05",
#     "userCode": "13698000000",
#     "userName": "剧亚东",
#     "thanksMoney": "0",
#     "patientCode": "",
#     "patientName": ""
# }
#
#
# re_visit = requests.post(url_visit, json=data_visit, headers=headers)
#
# print(re_visit.json())
#
#
#
#
#

# import requests  # 导入requests 模块
# from bs4 import BeautifulSoup  # 导入BeautifulSoup 模块
# from selenium import webdriver  # 导入Selenium的webdriver
# from selenium.common.exceptions import TimeoutException
#
# driver = webdriver.Chrome()
# driver.set_page_load_timeout(10)
# driver.set_script_timeout(10)
#
#
# def get_url():
#     try:
#         re = requests.get('http://tieba.baidu.com/p/6112839021')
#     except TimeoutException:
#         print("页面加载超时，强行结束加载！")
#         # driver.execute_script('window.stop()')  # 执行超时强行结束加载的js
#     else:
#         return re.text
#
# def get_lxml():
#     soup = BeautifulSoup(get_url(), 'lxml')
#     img_title = soup.find('h1', class_='core_title_txt')['title']
#     print(img_title)
#
# get_lxml()

#
# str = [1,2,3,4,5,6,7]
# a = str.pop()
# print(a)
# print(str)

import re

path = 'E:\\PycharmProjects\\picture\\▼SonYoonJoo▲180530"?*&^<>\资源_2018 "Summer in Guam"系列合集！！'

fileName = re.sub('[\/:*?"<>|]', '', path) # 去掉非法字符
print(path)
print(fileName)
