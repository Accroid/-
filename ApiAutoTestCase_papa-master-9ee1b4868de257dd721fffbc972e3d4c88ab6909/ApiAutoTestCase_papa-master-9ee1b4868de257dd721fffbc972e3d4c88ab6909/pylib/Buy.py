#!/usr/bin/python
# coding=utf-8
from encrypt import encrypt
from public import public_class

from encrypt import encrypt

from cfg import productCode
# md = hashlib.md5()  # 构造一个md5


class Buy(public_class):
    # 立即购买接口
    def purchase(self,sessionToken):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['productCode']=productCode[1]
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'business/purchase/detail.json')

    # 专卖换钱接口
    def resell(self,sessionToken):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['productCode']=productCode[1]
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'business/resell/pay.json')

# 立即转卖接口
    def immedi_resell(self,sessionToken):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'business/resell/immediate.json')

# 立即转卖确认转卖接口
    def immedi_resell_confirm(self,sessionToken,bankInfoId,id):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['bankInfoId']=bankInfoId
        params['id']=id
        params['productCode']=productCode[0]
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'business/purchase/confirm.json')

# 确认发货接口接口
    def send_confirm(self,sessionToken,id):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['id']=id
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'shipment/confirm.json')


# 信用支付确认支付接口
    def payment_confirm(self,sessionToken,productCode,term,receivingAddressId):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['productCode']=productCode
        params['term']=term
        params['receivingAddressId']=receivingAddressId
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'credit/payment/confirm.json')


# 转卖换钱确认转卖接口
    def resell_confirm(self,sessionToken,term,bankInfoId):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['productCode']=productCode[1]
        params['term']=term
        params['bankInfoId']=bankInfoId
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'business/resell/confirm.json')


# 确认收货接口
    def delivery_confirm(self,sessionToken,id):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['id']=id
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'delivery/confirm.json')


# if __name__ == '__main__':
#     scm = Buy()
#     ret = scm.resell_confirm('70fdb5c64203463684bcc3c9c15423e0', '7', '15', 'd2b5f4fea338489cb4be73795bf6e79c')
#     print (json.dumps(ret, indent=2))

if __name__ == '__main__':
    scm = Buy()
    ret = scm.purchase('5f9dd81dd26141358f8b532a6013a1cd')
    # print (json.dumps(ret, indent=2))