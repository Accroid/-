#coding=utf-8
from public import public_class
import cfg,api,Login
from encrypt import encrypt

class Account:
    scm = public_class()
    sc = Login.Login()
    #银行推荐列表
    def getRecommendedList(self,):
        #传公参
        params=self.scm.public_argument()
        return self.scm.request_post(params,api.getRecommendedList)

    #我的账户-可调
    def assetInfo(self,):
        #传公参
        params=self.scm.public_argument()

        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        return self.scm.request_post(params,api.assetInfo)

    #用户是否新手
    def isNewHand(self,):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        return self.scm.request_post(params,api.isNewHand)

    #银行卡限额列表
    def bankLimitList(self,):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        return self.scm.request_post(params,api.bankLimitList)

    #我的银行卡
    def getBankCard(self,):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        return self.scm.request_post(params,api.getBankCard)

    #更换银行卡
    def resetCard(self,):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        return self.scm.request_post(params,api.resetCard)

    #修改支付密码-可调
    def modifyPayPassword(self,):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        return self.scm.request_post(params,api.modifyPayPassword)

    #忘记支付密码 - 可调
    def forgetPayPassword(self,):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        return self.scm.request_post(params,api.forgetPayPassword)

    #实名认证
    def certification(self,acctName,idCode):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        params['acctName'] = encrypt(acctName)
        params['idCode'] = encrypt(idCode)
        return self.scm.request_post(params,api.certification)

if __name__ == '__main__':
    scm = Account()
    ret = scm.assetInfo()
    # print (json.dumps(ret, indent=2))