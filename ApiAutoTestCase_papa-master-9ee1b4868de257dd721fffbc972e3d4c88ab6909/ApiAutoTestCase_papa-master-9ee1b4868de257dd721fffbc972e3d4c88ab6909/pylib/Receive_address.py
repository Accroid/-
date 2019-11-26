#!/usr/bin/python
# coding=utf-8

from encrypt import encrypt
from public import public_class
# md = hashlib.md5()  # 构造一个md5


class Receive_address(public_class):

    # 收货地址新增及更新接口
    def Address_Update(self,sessionToken,name,phone,province,city,district,detail,tolerate,id=None):
        if  id !=None:
            # 传公参
            params = self.public_argument()
            params['sessionToken'] = sessionToken
            params['id'] = id
            params['name'] = encrypt(name)
            params['phone'] = encrypt(phone)
            params['province'] =province
            params['city'] =city
            params['district'] =district
            params['detail'] =encrypt(detail)
            params['tolerate'] =tolerate
        else:
            # 传公参
            params = self.public_argument()
            params['sessionToken'] = sessionToken
            params['name'] = encrypt(name)
            params['phone'] = encrypt(phone)
            params['province'] =province
            params['city'] =city
            params['district'] =district
            params['detail'] =encrypt(detail)
            params['tolerate'] =tolerate
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'address/update.json')


# 收货地址列表接口
    def Address_list(self,sessionToken):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        #验签
        headers=self.Inspection_sign(params)
        return self.request_get(params,headers,'address/list.json')

# 设置默认收货地址
    def Address_setdefault(self,sessionToken,id,tolerate):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['id']=id
        params['tolerate']=tolerate
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'address/setdefault.json')

# 收货地址删除接口
    def Address_delete(self,sessionToken,id):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['id']=id
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'address/delete.json')
