#!/usr/bin/python
# coding=utf-8

from public import public_class
from cfg import productCode

from encrypt import encrypt

# md = hashlib.md5()  # 构造一个md5

class Payment(public_class):
    # 现金支付确认购买接口
    def purchase_Pay(self,sessionToken,receivingAddressId,bankInfoId):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['receivingAddressId']=receivingAddressId
        params['bankInfoId']=bankInfoId
        params['productCode']=productCode[1]
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'business/purchase/pay.json')


    # 立即还款接口
    def bizNew(self,sessionToken,bizType,contractId=None):
        if contractId!=None:
            # 传公参
            params = self.public_argument()
            params['sessionToken'] = sessionToken
            params['bizType'] = bizType
            params['contractId'] = contractId

        else:
            # 传公参
            params = self.public_argument()
            params['sessionToken'] = sessionToken
            params['bizType'] = bizType
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'order/repay/bizNew.json')


    # 获取还款地址接口
    def repay_link(self,sessionToken,contractId,bizType,bankInfoId):
        # 传公参
        params = self.public_argument()
        params['sessionToken'] = sessionToken
        params['contractId'] = contractId
        params['bizType'] = bizType
        params['bankInfoId'] = bankInfoId
        # 验签
        headers = self.Inspection_sign(params)
        return self.request_post(params, headers, 'order/repay/link.json')
