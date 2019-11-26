#!/usr/bin/python
# coding=utf-8

from public import public_class
from encrypt import encrypt
from cfg import productCode

# md = hashlib.md5()  # 构造一个md5

class Application_Loan(public_class):

    # 签约信息查询接口
    def Sign_Query(self, sessionToken,contractId):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['contractId']=contractId
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'order/apply/signature.json')

    # 提交订单金额接口
    def Apply_submit(self, sessionToken,loanAmount,loanTerm,contractId,loanUsage):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['contractId']=contractId
        params['loanAmount']=loanAmount
        params['loanTerm']=loanTerm
        params['loanUsage']=loanUsage
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'order/apply/submit.json')

    # 金额预算接口
    def Apply_calculate(self, sessionToken,loanAmount,loanTerm,contractId):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['contractId']=contractId
        params['loanAmount']=loanAmount
        params['loanTerm']=loanTerm
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'order/apply/calculate.json')


    # 额度、优惠券信息获取接口
    def Apply_Creditline(self, sessionToken,contractId):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['contractId']=contractId
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'order/apply/creditline.json')


    # 提交订单,开始签约接口
    def Apply_Engage(self, sessionToken):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['productCode']=self.productCode[0]
        params['productVersion']=self.productVersion
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'order/apply/engage.json')
