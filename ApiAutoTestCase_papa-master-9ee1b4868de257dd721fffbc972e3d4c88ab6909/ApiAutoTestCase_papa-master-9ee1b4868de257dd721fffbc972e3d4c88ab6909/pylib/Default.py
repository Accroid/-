#!/usr/bin/python
# coding=utf-8
import requests, json

from public import public_class



# md = hashlib.md5()  # 构造一个md5


class Default(public_class):
    # 热门商品接口
    def hot_goods(self,sessionToken):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        #验签
        headers=self.Inspection_sign(params)
        return self.request_get(params,headers,'home.json')

    #商品列表接口
    def goods_list(self,orderByPrice,pageIndex,pageSize,sessionToken):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['orderByPrice']=orderByPrice
        params['pageIndex']=pageIndex
        params['pageSize']=pageSize
        # params['productCode']=self.productCode[1]
        #验签
        headers=self.Inspection_sign(params)
        return self.request_get(params,headers,'item/list.json')

# 订单详情接口
    def order_detail(self,sessionToken,id):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['id']=id
        params['mark']='2'
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'order/detail.json')

# 商品详情接口
    #id为商品id
    def goods_detail(self,sessionToken,id):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['id']=id
        #验签
        headers=self.Inspection_sign(params)
        return self.request_get(params,headers,'item/detail.json')


# 订单列表接口
    def order_list(self,sessionToken,pageIndex,pageSize):
        #传公参
        params=self.public_argument()
        params['sessionToken']=sessionToken
        params['pageIndex']=pageIndex
        params['pageSize']=pageSize
        #验签
        headers=self.Inspection_sign(params)
        return self.request_get(params,headers,'item/order/list.json')

# 广告链接
    def advert_info(self):
        #传公参
        params=self.public_argument()
        #验签
        headers=self.Inspection_sign(params)
        return self.request_post(params,headers,'app/advert/info')


if __name__ == '__main__':
    scm = Default()
    ret = scm.advert_info()
    print (json.dumps(ret, indent=2))