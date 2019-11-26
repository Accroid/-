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


class AboutMe(public_class):

    # 用户状态接口
    def user_state(self,sessionToken):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'user/msg/state.json')

    # 额度估值接口
    def user_obtain(self,sessionToken):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'user/quota/obtain.json')

# 认证中心接口
    def data_steps(self,sessionToken):
        def user_obtain(self, sessionToken):
            # 传公参
            params = self.public_argument()
            params['sessionToken'] = sessionToken
            # 验签
            headers = self.Inspection_sign(params)
            return self.request_post(params, headers, 'data/fill/steps.json')


if __name__ == '__main__':
    scm = AboutMe()
    ret = scm.user_obtain('09c90dc03c1d42e9bb41ffb6842f7bc2')
    print (json.dumps(ret, indent=2))