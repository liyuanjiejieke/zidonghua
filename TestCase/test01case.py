import json
import unittest

import paramunittest
from common.configHttp import  RunMain
import urllib.parse
# import testFile.readExcel as readExcel
# import testFile.geturlParams as geturlParams
from testFile.geturlParams import geturlParams
from testFile.readExcel import readExcel
# url= geturlParams.get_Url()
# readExcel=readExcel.readExcel()

login_xls=readExcel.get_xls(xls_name='userCase.xlsx',sheet_name='login')
# print("-------------7777777")
# print(login_xls)

@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
    def setParameters(self,case_name,path,query,method):
        self.case_name=str(case_name)
        self.path=str(path)
        self.query=str(query)
        self.method=str(method)
    def description(self):
        self.case_name

    def setUp(self):
        print(self.case_name+"测试开始前准备")
    def test01case(self):
        self.checkResult()
    def tearDown(self):
        print("测试结束，输出log完结\n\n")
    def checkResult(self):   # 断言
        url1='http://127.0.0.1:8888/login?'
        new_url=url1+self.query
        # 将一个完整的URL 中的name=xx&pwd=xxx转换为字典格式{'name':'xxx','pwd':'xxx'}
        data1=dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))
        info=RunMain().run_main(self.method,url1,data1)# 根据Excel中的method调用run_main进行请求并拿到响应
        ss=json.loads(info)
        print("------------------开始读数据--------")

        if self.case_name=='login':
            self.assertEqual(ss['code'],200)
        if self.case_name == 'login_error':
            self.assertEqual(ss['code'],-1)
        if self.case_name == 'login_null':
            self.assertEqual(ss['code'],10001)
