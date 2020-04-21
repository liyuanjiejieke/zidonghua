import requests
import flask.json as json
import random
import win32api
class RunMain():

    #获取随机数  8-16位随机数获取
    @classmethod
    def randomnumber(self):

        num = random.randint(10000000, 9999999999999999)
        return num



    def send_post(self,url,data):

        result=requests.post(url=url,data=data).json()

        # sort_keys 告诉编码器按照字典排序(a到z)输出
        # indent的数值，代表缩进的位数  indent参数根据数据格式缩进显示，读起来更加清晰:
        # 输出真正的中文需要指定ensure_ascii=False
        res = json.dumps(result, ensure_ascii=False,sort_keys=True,indent=2)
        return res
    def send_get(self,url,data):
        result=requests.get(url=url,params=data).json()
        res=json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
        return res
    def run_main(self,method,url,data):
        result=None
        if method == 'post':
            result=self.send_post(url,data)
        elif method =='get':
            result = self.send_get(url,data)
        else:
            print('Method值错误!!!')
        return result

if __name__ == '__main__':
    result1=RunMain().run_main('get','http://192.168.19.28:8000/open/merchant/list',
                               {'appId': 'EW_N3834426110', 'random': 5753004880518156,
                                'sign': '488a4b4413827bea18247cef79c51893'})
    # result2=RunMain().run_main('get','http://127.0.0.1:8888/login','username=xiaoming&pwd=111')
    print(result1)
    aa= RunMain().randomnumber()
    # print(aa)
    # print(result2)
