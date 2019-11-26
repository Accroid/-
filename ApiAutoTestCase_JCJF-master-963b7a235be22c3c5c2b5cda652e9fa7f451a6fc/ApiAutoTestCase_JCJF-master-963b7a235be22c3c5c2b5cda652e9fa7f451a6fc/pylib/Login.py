#coding=utf-8
from public import public_class
import cfg,api
from encrypt import encrypt

class Login:
    scm = public_class()

    #用户登陆
    def login(self,mobile,password,accountType,userType):
        #传公参
        params=self.scm.public_argument()
        params['mobile'] = encrypt(mobile)
        params['password'] = encrypt(password)
        params['accountType'] = accountType
        params['userType'] = userType
        return self.scm.request_post(params,api.login)

    # #获取签章授权URL
    # def fadada_authorize(self,):
    #     #传公参
    #     params=self.scm.public_argument()
    #     result = self.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
    #     params['token'] = result['data']['token']
    #     return self.scm.request_post(params,api.fadada_authorize)

    #是否已注册
    def isRegistered(self,mobile,accountType,userType):
        #传公参
        params=self.scm.public_argument()
        result = self.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        params['mobile'] = mobile
        params['accountType'] = accountType
        params['userType']  = userType
        return self.scm.request_post(params,api.isRegistered)

    #退出登陆
    def logout(self,):
        #传公参
        params=self.scm.public_argument()
        result = self.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        return self.scm.request_post(params,api.logout)



if __name__ == '__main__':
    scm = Login()
    ret = scm.login('18630409115','ly123456','T','0')
    # print (json.dumps(ret, indent=2))