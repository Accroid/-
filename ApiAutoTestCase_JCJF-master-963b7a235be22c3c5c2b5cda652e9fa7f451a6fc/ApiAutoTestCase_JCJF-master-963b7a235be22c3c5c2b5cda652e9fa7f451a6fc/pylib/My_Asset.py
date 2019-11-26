#coding=utf-8
from public import public_class
import cfg,api,Login

class My_Asset:
    scm = public_class()
    sc = Login.Login()

    #查询余额及优惠券数量
    def getBalanceAndCouponNum(self,productId):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        params['productId'] = productId
        return self.scm.request_post(params,api.getBalanceAndCouponNum)

    #我的出借记录详情-可调
    def lend_detail(self,orderNo):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        params['orderNo'] = orderNo
        return self.scm.request_post(params,api.lend_detail)

    #收支明细类型-可调
    def transactionType_list(self):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        return self.scm.request_post(params,api.transactionType_list)

    #我的优惠券列表-可调
    def coupon_list(self,couponStatus,productId):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        params['couponStatus'] = couponStatus
        params['productId'] = productId
        return self.scm.request_post(params,api.coupon_list)

    #我的出借记录-可调
    def lend_list(self):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        return self.scm.request_post(params,api.lend_list)

    #收支明细-可调
    def transaction_list(self,type):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        params['type'] = type
        return self.scm.request_post(params,api.transaction_list)

    #收支详情-可调
    def transaction_detail(self,flowId):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        params['flowId'] = flowId
        return self.scm.request_post(params,api.transaction_detail)

    #我的资产-可调
    def assetDetail(self):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        return self.scm.request_post(params,api.assetDetail)

if __name__ == '__main__':
    scm = My_Asset()
    ret = scm.getUserByInviteCode()  # print (json.dumps(ret, indent=2))