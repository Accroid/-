#!/usr/bin/python
# coding=utf-8
import requests, json, hashlib, urllib2

from public import public_class


md = hashlib.md5()  # 构造一个md5


class Home(public_class):

    # 产品列表接口
    def list(self, sessionToken):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'app/product/list.json')


    # APP配置接口
    def init(self, sessionToken):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'app/config/init.json')

