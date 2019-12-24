import os
import configparser
import testFile.getpathInfo as getpathInfo

#调用实例化，还记得这个类返回的路径为
path = getpathInfo.get_path()

#这句话是在path路径下再加一级
config_path = os.path.join(path, 'config.ini')


#调用外部的读取配置文件的方法
config = configparser.ConfigParser()

config.read(config_path, encoding='utf-8')

class ReadConfig():
    def get_http(self,name):
        value=config.get('HTTP',name)
        return value
    def get_email(self,name):
        value=config.get('EMAIL',name)
        return value
    def get_mysql(self,name):
        value=config.get('DATABASE',name)
        return value

if __name__ == '__main__':
    print(ReadConfig().get_http('baseurl'))