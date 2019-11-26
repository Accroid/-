*** Settings ***
Test Timeout      2 minutes
Library           ../pylib/My_Asset.py
Library           ../pylib/Project.py
Variables         ../cfg.py

*** Test Cases ***
查询余额及优惠券数量-tc005000-正常情况
#先获取项目id
    ${result}   product_list    1
    ${productId}   evaluate   $result['data']['list'][0]['id']
    ${ret}    getBalanceAndCouponNum    ${productId}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

查询余额及优惠券数量-tc005001-productId为空
##先获取项目id
#    ${result}   product_list    1
#    ${productId}   evaluate   $result['data']['list'][0]['id']
    ${ret}    getBalanceAndCouponNum    ${None}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    项目不存在
    should contain   ${ret2}    4002

我的出借记录详情-可调-tc005100-正常情况
#先获取出借记录订单号
    ${result}   lend_list
    ${orderNo}   evaluate   $result['data']['list'][0]['orderNo']
    ${ret}    lend_detail    ${orderNo}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

我的出借记录详情-可调-tc005101-orderNo为空
##先获取出借记录订单号
#    ${result}   lend_list
#    ${orderNo}   evaluate   $result['data']['list'][0]['orderNo']
    ${ret}    lend_detail    ${None}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    对不起，参数异常
    should contain   ${ret2}    500

收支明细类型-可调-tc005200-正常情况
    ${ret}    transactionType_list
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

我的优惠券列表-可调-tc005300-正常情况
    ${ret}    coupon list    1    ${None}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

我的出借记录-可调-tc005400-正常情况
    ${ret}    lend_list
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

收支明细-可调-tc005500-正常情况
    ${ret}    transaction_list    ${none}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

收支详情-可调-tc005600-正常情况
#先获取收支记录id
    ${result}    transaction_list    ${none}
    ${flowId}    evaluate     $result['data']['list'][0]['flowId']
    ${ret}    transaction_detail    ${flowId}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

收支详情-可调-tc005601-flowId为空
##先获取收支记录id
#    ${result}    transaction_list    ${none}
#    ${flowId}    evaluate     $result['data']['list'][0]['flowId']
    ${ret}    transaction_detail    ${None}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    	flowId不能为空
    should contain   ${ret2}    500

我的资产-tc005700-正常情况
    ${ret}    assetDetail
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200
