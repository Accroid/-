#!/usr/bin/python
# coding=utf-8

from public import public_class
from encrypt import encrypt

# md = hashlib.md5()  # 构造一个md5


class Contact(public_class):

    # 联系人查询接口
    def Contact_query(self, sessionToken):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'data/contact/query.json')

    # 提交联系人接口
    def Contact_save(self, sessionToken,contacts,mailList):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['contacts']=encrypt(contacts)
        params['mailList']=encrypt(mailList)
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'data/contact/save.json')
