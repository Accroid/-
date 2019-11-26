#!/usr/bin/python
# coding=utf-8

from public import public_class
from encrypt import encrypt

# md = hashlib.md5()  # 构造一个md5


class Repayment(public_class):

    # 还款接口
    def repay_biz(self, sessionToken,contractId,bizType):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['contractId']=contractId
        params['bizType']=bizType
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'order/repay/biz.json')
