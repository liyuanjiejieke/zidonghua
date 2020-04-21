import os
from xlrd import open_workbook
from testFile.getpathInfo import get_path
# 拿到该项目所在的绝对路径
path = get_path()

print(path)
print("-----------------------------")
class readExcel(object):

    # 根据开始行    结束行 取值
    @classmethod
    def get_xlsA(self, xls_name, sheet_name,strnum_hang,endnum_hang):  # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
        cls = []
        # 获取用例文件路径
        xlsPath = os.path.join(path, 'case', xls_name)
        file = open_workbook(xlsPath)  # 打开用例Excel
        sheet = file.sheet_by_name(sheet_name)  # 获得打开Excel的sheet
        # 获取这个sheet内容行数
        row_Num = sheet.nrows
        col_Num = sheet.ncols
        key = sheet.row_values(0)  # 这是第一行数据，作为字典的key值
        if row_Num <= 1:
            print("没数据")
        else:
            j = 1
            for i in range(strnum_hang,endnum_hang):
                d ={}
                values = sheet.row_values(j)
                for x in range(col_Num):
                    # 把key值对应的value赋值给key，每行循环
                    d[key[x]]=values[x]
                j+=1
                # 把字典加到列表中
                cls.append(d)
        return cls



    # 根据开始行   结束行    开始列  结束列
    @classmethod
    def get_xlsB(self, xls_name, sheet_name,strnum_hang,endnum_hang,strnum_lie,endnum_lie):  # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
        cls = []
        # 获取用例文件路径
        xlsPath = os.path.join(path, 'case', xls_name)
        file = open_workbook(xlsPath)  # 打开用例Excel
        sheet = file.sheet_by_name(sheet_name)  # 获得打开Excel的sheet
        # 获取这个sheet内容行数
        row_Num = sheet.nrows
        col_Num = sheet.ncols
        key = sheet.row_values(0)  # 这是第一行数据，作为字典的key值
        if row_Num <= 1:
            print("没数据")
        else:
            j = 1
            for i in range(strnum_hang,endnum_hang):
                d ={}
                values = sheet.row_values(j)
                for x in range(strnum_lie,endnum_lie):
                    # 把key值对应的value赋值给key，每行循环
                    d[key[x]]=values[x]
                j+=1
                # 把字典加到列表中
                cls.append(d)
        return cls

    def get_xlsC(self, xls_name, sheet_name):  # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
        cls = []
        # 获取用例文件路径
        xlsPath = os.path.join(path,'case', xls_name)
        file = open_workbook(xlsPath)  # 打开用例Excel
        sheet = file.sheet_by_name(sheet_name)  # 获得打开Excel的sheet
        # 获取这个sheet内容行数
        nrows = sheet.nrows
        for i in range(nrows):  # 根据行数做循环
            if sheet.row_values(i)[0] != u'case_name':  # 如果这个Excel的这个sheet的第i行的第一列不等于case_name那么我们把这行的数据添加到cls[]
                cls.append(sheet.row_values(i))
        return cls



if __name__ == '__main__':  # 我们执行该文件测试一下是否可以正确获取Excel中的值


    # print(readExcel().get_xls('userCase.xlsx', 'login'))
    list=readExcel().get_xls('userCase.xlsx', 'test2', 1, 2)
    print(list[0])
    # print(readExcel().get_xls('userCase.xlsx', 'login')[1])
