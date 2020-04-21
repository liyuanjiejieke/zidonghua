import requests

paran ={"userName":"SHlibaoshC","passWord":"111qqq"}
r=requests.get("http://testclubshop.liantuobank.com/open/login",params=paran)

print(r.status_code)  #打印状态码
print(r.content) # 字节方式的响应体  会自动为你解码gzip 和 deflate压缩
print(r.headers)
print("=================")#以字典对象存储服务器响应头，但是这个字典比较特殊  字典键不区分大小写  若键不存在则返回None
print(r.json())  # requests 中内置的JSON解码器    requests 的方便之处还在于  对特定类型的响应  例如JSON可以直接获取
print(r.url) # 获取url
print(r.encoding) # 编码格式  requests自动检测编码
print(r.cookies)  #获取cookies
print(r.raw) # 返回原始响应体    r.text  字符串方式的响应体 会自动根据响应头部的字符串编码进行解码
print(r.raise_for_status())  #失败请求 非200响应  抛出异常
print(r.text)