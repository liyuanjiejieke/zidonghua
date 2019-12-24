import flask
import json
from flask import request
import paramunittest
# 创建一个服务  把当前这个puthon文件当做一个服务
server=flask.Flask(__name__)
@server.route('/login',methods=['get','post'])
def login():
    username=request.values.get('username')
    pwd=request.values.get('pwd')
    if username and pwd:
        if username == 'xiaoming' and pwd == '111':
            res={'code':200,'message':'登录成功'}
            return json.dumps(res,ensure_ascii=False)
        else:
            res={'code':-1,'message':'账号或密码错误'}
            return json.dumps(res, ensure_ascii=False)
    else:
        res={'code':10001,'message':'参数不能为空'}
        return json.dumps(res, ensure_ascii=False)
if __name__=='__main__':
    server.run(debug=True,port=8888,host='127.0.0.1')