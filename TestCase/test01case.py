import json
import unittest
import paramunittest
from common import configHttp
from common.signtest import signclass
from common.configHttp import  RunMain
from testFile.readExcel import readExcel
from common.Log import Logger

logname=Logger.logpath()
log=Logger(logname,level='debug')

login_xls=readExcel.get_xlsA(xls_name='userCase.xlsx', sheet_name='login',strnum_hang=1,endnum_hang=3)

path="/open/merchant/list"

@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):

    def setParameters(self, appId):
        self.appId = str(appId)
    # def setUp(self):
    #
    #     print(self.case_name+"测试开始前准备")

    def test01case(self):
        self.checkResult()

    # def tearDown(self):
    #     print("测试结束，输出log完结\n\n")

    def checkResult(self):  # 断言
        random=configHttp.RunMain.randomnumber()

        list=readExcel.get_xlsA("userCase.xlsx","login",1,3)
        # print(list[0])
        data1=list[0]
        data1.setdefault("random",random)
        print(str(data1))
        apikey="d6c59f0883ab9deae32e74e91a0999f6"
        signkey = signclass.signtestas(apikey, data1)
        data1.setdefault("sign", signkey)

        print(data1)
        url1 = 'http://192.168.19.28:8000/open/merchant/list?'
        # new_url = url1+

        # 将一个完整的URL中的name = & pwd = 转换为{'name': 'xxx', 'pwd': 'bbb'}
        # data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))
        # print(str(str(data1))+"======================================================")

        info = RunMain().send_post(url1,data1)  # 根据Excel中的method调用run_main进行请求并拿到响应
        print(info + "=====================")
        ss = json.loads(info)  # 将响应转为字典格式
        print(str(ss))

        if ss['code']=="SUCCESS":
            log.logger.debug('登录成功')

            #     log.logger.debug('登录成功')
        # if self.case_name == 'login':
        #     self.assertEqual(ss['code'], "SUCCESS")
        #     log.logger.debug('登录成功')
        # else:
            self.assertEqual(ss['code'], "FALSE")
            log.logger.debug('登录失败')



if __name__ == '__main__':

    unittest.main()
    # testUserLogin().test01case()
    # testUserLogin.checkResult()








