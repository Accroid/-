#!/usr/bin/python
# coding=utf-8

from public import public_class
from encrypt import encrypt

# md = hashlib.md5()  # 构造一个md5


class Shumei(public_class):

    # 数美资料保存接口
    def data_basic(self, sessionToken):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['deviceId']=self.deviceNo
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'data/shumei/save.json')

    # 数美资料验证接口
    def data_query(self, sessionToken):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'data/shumei/query.json')
