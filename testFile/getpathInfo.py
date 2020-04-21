import os
def get_path():
    path = os.path.split(os.path.realpath(__file__))[0]
    # print(os.path.dirname(path))
    return path
# if __name__ == '__main__':
#     print('测试路径为：',get_path())




