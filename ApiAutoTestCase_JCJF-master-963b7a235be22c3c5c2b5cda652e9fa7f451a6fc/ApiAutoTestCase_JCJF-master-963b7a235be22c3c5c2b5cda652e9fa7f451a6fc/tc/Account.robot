*** Settings ***
Test Timeout      2 minutes
Library           ../pylib/Account.py
Variables         ../cfg.py

*** Test Cases ***
银行推荐列表-tc000100-正常情况
    ${ret}    getRecommendedList
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

我的账户-可调-tc000200-正常情况
    ${ret}    assetInfo
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

用户是否新手-tc000300-正常情况
    ${ret}    isNewHand
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

银行卡限额列表-tc000400-正常情况
    ${ret}    bankLimitList
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

我的银行卡-tc000500-正常情况
    ${ret}    getBankCard
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

更换银行卡-tc000600-正常情况
    ${ret}    resetCard
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

修改支付密码-可调-tc000700-正常情况
    ${ret}    modifyPayPassword
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

忘记支付密码-可调-tc000800-正常情况
    ${ret}    forgetPayPassword
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

实名认证-可调-tc000900-正常情况
    ${ret}    certification     ${acctName}    ${idCode}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    用户已实名认证
    should contain   ${ret2}    3003