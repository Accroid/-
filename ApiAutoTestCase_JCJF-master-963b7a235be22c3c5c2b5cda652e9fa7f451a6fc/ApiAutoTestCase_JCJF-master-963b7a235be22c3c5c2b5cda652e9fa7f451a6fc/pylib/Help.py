#coding=utf-8
from public import public_class
import cfg,api,Login

class Help:
    scm = public_class()
    sc = Login.Login()

    #精选活动列表
    def activityList(self):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        return self.scm.request_post(params,api.getInviteList)

    #官方公告列表
    def noticeList(self):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        return self.scm.request_post(params,api.noticeList)

    #根据类型获取问题列表
    #可根据列表获取类型id
    def findListByTypeId(self,typeId):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        params['typeId'] = typeId
        return self.scm.request_post(params,api.findListByTypeId)

#帮助类型列表
    def getHelpTypeList(self,):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        return self.scm.request_post(params,api.getHelpTypeList)

    #热门问题
    def getHotList(self,):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        return self.scm.request_post(params,api.getHotList)

#官方公告详情
    def getNewsInfo(self,newsId):
        #传公参
        params=self.scm.public_argument()
        result = self.sc.login(cfg.mobile,cfg.password,cfg.accountType,cfg.userType)
        params['token'] = result['data']['token']
        params['newsId'] = newsId
        return self.scm.request_post(params,api.getNewsInfo)

if __name__ == '__main__':
    scm = Help()
    ret = scm.findListByTypeId()  # print (json.dumps(ret, indent=2))