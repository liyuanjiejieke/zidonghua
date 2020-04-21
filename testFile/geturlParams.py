import testFile.readConfig as readConfig
ReadConfig=readConfig.ReadConfig()
class geturlParams():
    @classmethod
    def get_Url(self):
        new_url=ReadConfig.get_http('scheme')+'://'+ReadConfig.get_http('baseurl')+':'+ReadConfig.get_http('port')+'/login'+'?'
        return new_url
# if __name__ == '__main__':
#     print(geturlParams.get_Url())
