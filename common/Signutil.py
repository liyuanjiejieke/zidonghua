from testFile.readExcel import readExcel
from common.Log import Logger
logname=Logger.logpath()
log=Logger(logname,level='debug')
login_xls=readExcel.get_xls(xls_name='userCase.xlsx',sheet_name='test')


def signa():


    cls =readExcel().get_xls('userCase.xlsx', 'test')

    str=cls[0]
    print(str.get('case_name'))



if __name__ == '__main__':
    signa()