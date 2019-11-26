#!/usr/bin/python
# coding=utf-8
import requests, json
from  common.cfg import deviceType,appIdCHSName,packageName,packageCHSName,productCode,productSku,\
    appVersion,appChannel,deviceNo,appUserId,deviceSystemVersion,deviceModel,localProvinceName,localCityName,URL,appId
from pprint import pprint
from common.md5 import md5
from common.encrypt import encrypt



class Account:
    def __init__(self):
        self.URL = URL
        self.deviceType = deviceType
        self.appId = appId
        self.appIdCHSName = appIdCHSName
        self.appVersion = appVersion
        self.appChannel = appChannel
        self.deviceNo = deviceNo
        self.appUserId = appUserId
        self.deviceSystemVersion = deviceSystemVersion
        self.deviceModel = deviceModel
        self.packageName = packageName
        self.packageCHSName = packageCHSName
        self.productCode = productCode
        self.productSku = productSku
        self.localProvinceName = localProvinceName
        self.localCityName = localCityName

   # 用户，注册，重置密码，退出接口
    def biz(self,mobile,password,bizType):
        params = {
            'deviceType': self.deviceType,
            'appId': 'papa',
            'appIdCHSName': self.appIdCHSName,
            'packageName' : self.packageName,
            'packageCHSName': self.packageCHSName,
            'productCode':self.productCode,
            'productSku':self.productSku,
            'appVersion': self.appVersion,
            'appChannel': self.appChannel,
            'deviceNo': self.deviceNo,
            # 'appUserId': self.appUserId,
            'deviceSystemVersion': self.deviceSystemVersion,
            'deviceModel': self.deviceModel,
            'localProvinceName':self.localProvinceName,
            'localCityName':self.localCityName,
            # 'sessiontoken':sessiontoken,
            'mobile': encrypt(mobile),
            'password':encrypt(password),
            'bizType':bizType
        }
        list = sorted(params.items(), key=lambda item: item[0])
        str = ""
        # print(type(list))
        # print(list)
        for one in list:
            print (type(one[1]))
            print (one[1])
            if type(one[1])=="<class 'bytes'>":
                str(one[1])
            str += one[1]
        print(str)
        str += 'v__s_k_=xinyong234@21@#$fasd'
        md5_str = md5(str)
        headers = {
            '_nsign': md5_str.upper(),
            '_nversion': 'default'
        }
        url = '{}/{}'.format(URL, 'user/account/biz.json')
        response = requests.post(url, data=params, headers=headers, verify=False)
        bodyDict = response.json()
        pprint(bodyDict, indent=2)
        return bodyDict

if __name__ == '__main__':
    scm = Account()
    ret = scm.biz('13735865796', '123456', 'LOGIN')