#!/usr/bin/env python#coding:utf-8
import hashlib
import common.configHttp as configHttp
from common.Log import Logger
logname = Logger.logpath()
log = Logger(logname, level='debug')

class signclass():





    def signtestas(apikey,body):
        # 测试的域名
        # path = "http://192.168.19.28:8000"+urlpath+"?"

        # apikey = apikey  # 验证密钥，由开发提供
        # body = body

        for key in list(body.keys()):
            if not body.get(key):
                del body[key]
        # 按照升序排列，得到的是一个列表，列表的元素为元组
        url_params1 = sorted(body.items(), key=lambda d: d[0], reverse=False)
        values = []
        for li in url_params1:

            newsmbol = ('=',)
            # 元组中增加一个新元素
            li = li[:1] + newsmbol + li[1:]
            # 元组转化为字符串，整型不能转化，list包含数字，不能直接转化成字符串
            value = "".join('%s' % id for id in li)
            values.append(value)


        values1 = values[:]
        values1.append('key='+apikey)
        sign1 = "&".join(values1)
        sign = signclass.jiamimd5(sign1)
        #将得到的字符串中的字母全部转化为小写
        signxiao=sign.lower()


        # # 添加到请求对象中
        # body["sign"] = signxiao
        # log.logger.debug(signxiao)
        #
        # info= configHttp.RunMain.send_post('post', path, body)
        # print(info)
        # MD5加密

        return signxiao



    def jiamimd5(src):
        m = hashlib.md5()
        m.update(src.encode('UTF-8'))
        return m.hexdigest()






if __name__ == '__main__':
    randomx = configHttp.RunMain.randomnumber()
    body = {'random': randomx, 'appId': 'EW_N3834426110'}
    stra=signclass.signtestas("d6c59f0883ab9deae32e74e91a0999f6",body)
    print(stra+"--------------------")