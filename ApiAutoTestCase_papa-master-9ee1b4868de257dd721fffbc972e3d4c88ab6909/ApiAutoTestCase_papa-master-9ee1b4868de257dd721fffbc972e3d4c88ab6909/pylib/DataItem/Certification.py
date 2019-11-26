#!/usr/bin/python
# coding=utf-8

from public import public_class
from encrypt import encrypt
from requests_toolbelt.multipart.encoder import MultipartEncoder


class Certification(public_class):

    # 修改实名信息接口
    def Certification_Update(self, sessionToken,idCardNo,fullname):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['idCardNo']=encrypt(idCardNo)
        params['fullname']=encrypt(fullname)
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'data/certification/update.json')

    # 检测是否可以修改实名信息接口
    def Certification_Check(self, sessionToken):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'data/certification/check.json')

    # 资料填写进度接口
    def Fill_progress(self, sessionToken):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['productCode']=self.productCode[0]
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'data/fill/progress.json')

    # # 保存实名认证信息
    # def save_data(self, sessionToken,fullname,idCardNo,gender,birthdate,ocrEthnicity,ocrResidentialAddr,ocrIssuingAuthority,ocrValidStart,ocrValidEnd):
    #     #传公参
    #     params=self.public_argument()
    #     params['sessionToken']=sessionToken
    #     params['fullname']=encrypt(fullname)
    #     params['idCardNo']=encrypt(idCardNo)
    #     # params['idCardPositivePic']=idCardPositivePic
    #     # params['idCardOppositePic']=idCardOppositePic
    #     params['gender']=gender
    #     params['birthdate']=birthdate
    #     params['ocrEthnicity']=ocrEthnicity
    #     params['ocrResidentialAddr']=encrypt(ocrResidentialAddr)
    #     params['ocrIssuingAuthority']=ocrIssuingAuthority
    #     params['ocrValidStart']=ocrValidStart
    #     params['ocrValidEnd']=ocrValidEnd
    #     params['idCardPositivePic']=('filename', open('picture.png', 'rb'),'image/png')
    #     params['idCardPositivePic']=('filename', open('picture.png', 'rb'),'image/png')
    #     multipart_encoder = MultipartEncoder(params
    #     )
    #     #验签
    #     headers=self.Inspection_sign(params)
    #     headers['Content-Type'] = multipart_encoder.content_type
    #
    #     return self.request_post(multipart_encoder,headers,'data/ocr/save.json')
#
# if __name__ == '__main__':
#     scm = Certification()
#     ret = scm.save_data('0589d3f54c2b4abca8d3d430f088cd01','王尼玛','410422199002155952','男','1990-02-15','汉族','母鸡啊','横县公安局','2017-01-03','2037-01-03')
#     # print (json.dumps(ret, indent=2))