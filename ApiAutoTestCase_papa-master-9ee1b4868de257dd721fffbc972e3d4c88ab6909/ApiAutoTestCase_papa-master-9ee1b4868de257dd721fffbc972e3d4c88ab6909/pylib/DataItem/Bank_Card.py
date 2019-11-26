#!/usr/bin/python
# coding=utf-8
import requests, json
from  cfg import deviceType,appIdCHSName,packageName,packageCHSName,productCode,productSku,\
    appVersion,appChannel,deviceNo,appUserId,deviceSystemVersion,deviceModel,localProvinceName,localCityName,URL,appId
from pprint import pprint
from md5 import md5
from public import public_class
from encrypt import encrypt

# md = hashlib.md5()  # 构造一个md5

import sys
print sys.path

class Bank_Card(public_class):

    # 用户银行卡列表接口
    def bankcard_list(self, sessionToken):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'data/bankcard/list.json')

    # 绑卡——获取验证码
    def Get_code(self, sessionToken,idCardNo,fullname,mobile,bankCardNo,bankName,bankCode,payday):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['idCardNo']=encrypt(idCardNo)
        params['fullname']=encrypt(fullname)
        params['mobile']=encrypt(mobile)
        params['bankCardNo']=encrypt(bankCardNo)
        params['bankName']=bankName
        params['bankCode']=bankCode
        params['payday']=payday
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'data/bank/getCode.json')


    # 银行卡排序接口
    def Bankcard_sort(self, sessionToken,ids):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['ids']=ids
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'data/bankcard/sort.json')


    # 设置选择的银行卡为主卡
    def Bankcard_select(self, sessionToken,id):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['id']=id
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'data/bankcard/select.json')

    # 解绑银行卡接口
    def Bankcard_unbind(self, sessionToken,id):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['id']=id
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'data/bankcard/unbind.json')

    # 提交绑卡（新版已停用）
    def Bankcard_bind(self, sessionToken,fullname,idCardNo,mobile,bankCardNo,bankSimpleName,bankCode,payday):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['fullname']=fullname
        params['idCardNo']=idCardNo
        params['mobile']=mobile
        params['bankCardNo']=bankCardNo
        params['bankSimpleName']=bankSimpleName
        params['bankCode']=bankCode
        params['payday']=payday
        #验签
        headers=self.Inspection_sign(params)
        return self.request_get(params,headers,'data/bankcard/bind.htm')

    # 绑卡支持银行列表接口
    def Bank_supported(self, sessionToken):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        #验签
        headers=self.Inspection_sign(params)
        return self.request_get(params,headers,'data/bank/supported.json')


if __name__ == '__main__':
    scm = Bank_Card()
    ret = scm.bankcard_list('70fdb5c64203463684bcc3c9c15423e0')
    print (json.dumps(ret, indent=2))