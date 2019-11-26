#coding=utf-8
from public import public_class
import cfg,api

class Contract:
    scm = public_class()

    #获取用户签章授权地址
    def authorize(self,):
        #传公参
        params=self.scm.public_argument()
        return self.scm.request_post(params,api.authorize)


if __name__ == '__main__':
    scm = Contract()
    ret = scm.authorize()
    # print (json.dumps(ret, indent=2))