#!/usr/bin/python
# coding=utf-8
import requests, json
from pprint import pprint
# from md5 import md5
# from encrypt import encrypt
import cfg


# md = hashlib.md5()  # 构造一个md5

class public_class:

    # 检查是否注册用户接口
    def public_argument(self,):
        params = {
            'appVersion': cfg.appVersion,
            'platformType': cfg.platformType,
            'appVersionCode': cfg.appVersionCode,
            'packageName' : cfg.packageName,
            'deviceType': cfg.deviceType,
            'accountType':cfg.accountType,
            'deviceSystemVersion': cfg.deviceSystemVersion,
            'deviceNo': cfg.deviceNo,
            'appChannel': cfg.appChannel,
            'deviceModel': cfg.deviceModel,
            'userType': cfg.userType,
        }
        return params

#     def Inspection_sign(self,params):
#         list = sorted(params.items(), key=lambda item: item[0])
# #参考文章 https://www.cnblogs.com/dylan-wu/p/6041465.html
#         str = ''
#         for one in list:
#             str += one[0].replace(' ', '') + '=' + one[1].replace(' ', '') + '&'
#         str += 'v__s_k_=xinyong234@21@#$fasd'
#         md5_str = md5(str)
#         headers = {'_nsign': md5_str.upper(), '_nversion': 'default'}
#         return headers

    def request_post(self,params,link):
        url = '{}/{}'.format(cfg.URL, link)
        response = requests.post(url, data=params, verify=False)
        bodyDict = response.json()
        print json.dumps(bodyDict, indent=2).decode('unicode-escape')
        return bodyDict

    def request_get(self,params,link):
        url = '{}/{}'.format(cfg.URL, link)
        response = requests.get(url, params=params, verify=False)
        bodyDict = response.json()
        print json.dumps(bodyDict, indent=2).decode('unicode-escape')
        return bodyDict