#!/usr/bin/python
# coding=utf-8
from public import public_class
from encrypt import encrypt

# md = hashlib.md5()  # 构造一个md5


class Base_Information(public_class):

    # 提交基本资料接口
    def Address_Update(self,sessionToken,educationLevel,maritalStatus,livingCity,livingCityCode,livingDetailAddress,position,company,comTel,comCity,comCityCode,comDetailAddr,oicq,industry):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['educationLevel']=educationLevel
        params['maritalStatus']=maritalStatus
        params['livingCity']=livingCity
        params['livingCityCode']=livingCityCode
        params['livingDetailAddress']=livingDetailAddress
        params['position']=position
        params['company']=company
        params['comTel']=comTel
        params['comCity']=comCity
        params['comCityCode']=comCityCode
        params['comDetailAddr']=comDetailAddr
        params['oicq']=oicq
        params['industry']=industry
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'data/basic/save.json')


# 查询基本信息接口
    def data_basic(self,sessionToken):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'data/basic/query.json')
