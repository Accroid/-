#!/usr/bin/python
# coding=utf-8
import requests, json
from cfg import deviceType, appIdCHSName, packageName, packageCHSName, productCode, productSku, appVersion, appChannel, \
    deviceNo, appUserId, deviceSystemVersion, deviceModel, localProvinceName, localCityName, URL, appId,productVersion
from pprint import pprint
from md5 import md5
from encrypt import encrypt


# md = hashlib.md5()  # 构造一个md5

class public_class:
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
        self.productCode =productCode
        self.productVersion = productVersion

    # 检查是否注册用户接口
    def public_argument(self,):
        params = {
            'deviceType': self.deviceType,
            'appId': 'papa',
            'appIdCHSName': self.appIdCHSName,
            'packageName' : self.packageName,
            'packageCHSName': self.packageCHSName,
            # 'productCode':self.productCode,
            'productSku':self.productSku,
            'appVersion': self.appVersion,
            'appChannel': self.appChannel,
            'deviceNo': self.deviceNo,
            'appUserId': self.appUserId,
            'deviceSystemVersion': self.deviceSystemVersion,
            'deviceModel': self.deviceModel,
            'localProvinceName':self.localProvinceName,
            'localCityName':self.localCityName,
            'productVersion':self.productVersion
        }
        return params

    def Inspection_sign(self,params):
        list = sorted(params.items(), key=lambda item: item[0])
#参考文章 https://www.cnblogs.com/dylan-wu/p/6041465.html
        str = ''
        for one in list:
            str += one[0].replace(' ', '') + '=' + one[1].replace(' ', '') + '&'
        str += 'v__s_k_=xinyong234@21@#$fasd'
        md5_str = md5(str)
        headers = {'_nsign': md5_str.upper(), '_nversion': 'default'}
        return headers

    def request_post(self,params,headers,link):
        url = '{}/{}'.format(URL, link)
        response = requests.post(url, data=params, headers=headers, verify=False)
        bodyDict = response.json()
        print json.dumps(bodyDict, indent=2).decode('unicode-escape')
        return bodyDict

    def request_get(self,params,headers,link):
        url = '{}/{}'.format(URL, link)
        response = requests.get(url, params=params, headers=headers, verify=False)
        bodyDict = response.json()
        print json.dumps(bodyDict, indent=2).decode('unicode-escape')
        return bodyDict