#coding=utf-8
from public import public_class
import cfg,api,Login

class Project:
    scm = public_class()
    sc = Login.Login()

    #借款人资金使用情况
    def fundUseInfo(self,productId):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        params['productId'] = productId
        return self.scm.request_post(params,api.fundUseInfo)

    #是否可以购买标的
    def isbuy(self):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        return self.scm.request_post(params,api.isbuy)

    #借款人信息
    def loan_info(self,productId):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        params['productId'] = productId
        return self.scm.request_post(params,api.loan_info)

    #项目列表-可调
    def product_list(self,type):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        params['type'] = type
        return self.scm.request_post(params,api.product_list)

    #项目基本信息-可调
    def product_detail(self,productId):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        params['productId'] = productId
        return self.scm.request_post(params,api.product_detail)

    #确认出借-可调
    def product_confirmInvest(self,productId,couponCode,amount):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        params['productId'] = productId
        params['couponCode'] = couponCode
        params['amount'] = amount
        return self.scm.request_post(params,api.product_confirmInvest)

    #项目出借记录-可调
    def product_lendRecord(self,productId):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        params['productId'] = productId
        return self.scm.request_post(params,api.product_lendRecord)

    #借款人图片
    def logout(self,productId,type):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        params['productId'] = productId
        params['type'] = type
        return self.scm.request_post(params,api.logout)


if __name__ == '__main__':
    scm = My_Asset()
    ret = scm.getUserByInviteCode()  # print (json.dumps(ret, indent=2))