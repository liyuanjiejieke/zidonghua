import requests
param={"userName":"lslslh","passWord":"111qqq"}
r=requests.get("http://192.168.19.28:8000/open/login",params=param)
# 获得响应状态码
print(r.status_code)
#获得字符串方式的响应体
print(r.text)
# 字节方式的响应体。会自动为你解码gzip和deflate
# print(r.content)
# 以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
print(r.headers)
# 获取URl
print(r.url)
# 编码格式  requests
print(r.encoding)
# 获取cookie
print(r.cookies)
# 返回原始响应体
print(r.raw)
# 失败请求   非200响应，抛出异常
print(r.raise_for_status())