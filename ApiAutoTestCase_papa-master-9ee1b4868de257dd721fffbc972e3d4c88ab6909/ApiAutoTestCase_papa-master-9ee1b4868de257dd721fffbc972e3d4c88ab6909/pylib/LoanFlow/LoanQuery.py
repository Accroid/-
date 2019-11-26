#!/usr/bin/python
# coding=utf-8

from public import public_class
from encrypt import encrypt

# md = hashlib.md5()  # 构造一个md5


class LoanQuery(public_class):

    # 我的贷款接口
    def Msg_list(self, sessionToken):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'order/msg/list.json')

    # 贷款详情接口
    def Msg_detail(self, sessionToken,contractId):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['contractId']=contractId
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'order/msg/detail.json')

    # 还款计划接口
    def Msg_repayments(self, sessionToken,contractId):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['contractId']=contractId
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'order/msg/repayments.json')


    # 订单状态接口(首页)
    def Msg_state(self, sessionToken):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'order/msg/state.json')
