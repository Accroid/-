#!/usr/bin/python
# coding=utf-8
from encrypt import encrypt
from public import public_class

# md = hashlib.md5()  # 构造一个md5


class Account(public_class):

    # 检查是否注册用户接口
    def check_registry(self,mobile=None):
        if mobile!=None:
            #传公参one
            params=self.public_argument()
            params['mobile']=encrypt(mobile)
        else:
            params=self.public_argument()
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'user/account/check_registry')

    # 用户，注册，重置密码，退出接口
    def biz(self,mobile,password,bizType=None):
        if bizType!=None:
            # 传公参one
            params = self.public_argument()
            params['mobile'] = encrypt(mobile)
            params['password']=encrypt(password)
            params['bizType']=bizType
        else:
            params = self.public_argument()
            params['mobile'] = encrypt(mobile)
            params['password']=encrypt(password)
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'/user/account/biz.json')

#用户账户信息查询接口
    def user_info(self,sessionToken):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'/user/account/info.json')


if __name__ == '__main__':
    scm = Account()
    ret = scm.biz('18143488220','1234567','LOGIN')
    # print (json.dumps(ret, indent=2))