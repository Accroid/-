#coding=utf-8
from public import public_class
import cfg,api

class Index:
    scm = public_class()

    #获取更新
    def getAppUpdate(self,):
        #传公参
        params=self.scm.public_argument()
        return self.scm.request_post(params,api.getAppUpdate)

    #首页-banner - 可调
    def getBanner(self,):
        #传公参
        params=self.scm.public_argument()
        return self.scm.request_post(params,api.getBanner)

    #首页-项目-可调
    def project(self,):
        #传公参
        params=self.scm.public_argument()
        return self.scm.request_post(params,api.project)

if __name__ == '__main__':
    scm = Index()
    ret = scm.getBanner()
    # print (json.dumps(ret, indent=2))