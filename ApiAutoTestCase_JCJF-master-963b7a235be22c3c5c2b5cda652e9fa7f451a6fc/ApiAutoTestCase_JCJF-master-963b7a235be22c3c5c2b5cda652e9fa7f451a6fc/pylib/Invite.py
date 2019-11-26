#coding=utf-8
from public import public_class
import cfg,api,Login

class Invite:
    scm = public_class()
    sc = Login.Login()

    #邀请列表
    def getInviteList(self):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        return self.scm.request_post(params,api.getInviteList)

    #获取当前用户邀请码
    def getInviteCode(self,):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        return self.scm.request_post(params,api.getInviteCode)

    #获取邀请人信息-h5
    def getUserByInviteCode(self,):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        ret = self.getInviteCode()
        params['inviteCode'] = ret['data']['inviteCode']
        return self.scm.request_post(params,api.getUserByInviteCode)

if __name__ == '__main__':
    scm = Invite()
    ret = scm.getUserByInviteCode()
    # print (json.dumps(ret, indent=2))