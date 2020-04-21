import logging
from logging import handlers
import time
import os
from testFile.getpathInfo import get_path

class Logger(object):
    level_relations={
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }
    @classmethod
    def __init__(self,filename,level='debug',when='D',
                 backCount=3,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d) - %(levelname)s:%(message)s]'):

        self.logger=logging.getLogger(filename)
        format_str=logging.Formatter(fmt) #设置日志的格式
        self.logger.setLevel(self.level_relations.get(level)) #设置日志的级别
        sh=logging.StreamHandler() # 往屏幕上输出
        sh.setFormatter(format_str)  #设置屏幕上的显示格式
        #往文件里写入指定间隔时间自动生成文件的处理器
        th=handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,
                                             encoding='utf-8')
        th.setFormatter(format_str) # 设置文件里写入的格式
        self.logger.addHandler(sh) # 把对象加到logger里
        self.logger.addHandler(th) #

    @classmethod
    def logpath(self):
        pathdir = get_path()
        # 获取文件上一级
        pathshang = os.path.dirname(pathdir)
        current_time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))  # 返回当前时间
        curren_path = os.path.join(pathshang, 'result')
        path3 = ''
        # 在该路径下新建下级目录
        new_name = path3.join(curren_path) + '/logsss/'
        print(new_name + "==========")
        dir_time = time.strftime('%Y%m%d', time.localtime(time.time()))  # 返回当前时间的年月日作为目录名称

        isExists = os.path.exists(new_name + dir_time)  # 判断该目录是否存在
        if not isExists:
            os.makedirs(new_name + dir_time)
            print(new_name + dir_time + "目录创建成功")

        else:
            # 如果目录存在则不创建，并提示目录已存在
            print(new_name + "目录 %s 已存在" % dir_time)

        log_name = new_name + dir_time + '/' + current_time + '.log'  # 定义日志文件的路径以及名称

        return log_name
