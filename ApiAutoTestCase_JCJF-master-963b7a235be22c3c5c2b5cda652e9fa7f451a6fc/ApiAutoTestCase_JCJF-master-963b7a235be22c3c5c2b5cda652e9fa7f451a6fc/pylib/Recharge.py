#coding=utf-8
from public import public_class
import cfg,api,Login

class Recharge:
    scm = public_class()
    sc = Login.Login()

    #查询充值的银行卡信息-可调
    def getBankCard(self,):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        return self.scm.request_post(params,api.getBankCard)

    #提现/提现列表-可调
    def withdraw_list(self):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        return self.scm.request_post(params,api.withdraw_list)

    #充值可调
    def recharge(self,amount):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        params['amount'] = amount
        return self.scm.request_post(params,api.recharge)

    #提现可调
    def withDraw(self,amount):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        params['amount'] = amount
        return self.scm.request_post(params,api.withDraw)

if __name__ == '__main__':
    scm = Recharge()
    ret = scm.getBankCard()
    # print (json.dumps(ret, indent=2))