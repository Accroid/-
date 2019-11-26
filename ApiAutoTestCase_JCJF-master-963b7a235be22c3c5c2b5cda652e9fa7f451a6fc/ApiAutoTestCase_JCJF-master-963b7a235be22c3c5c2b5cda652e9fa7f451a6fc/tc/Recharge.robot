*** Settings ***
Test Timeout      2 minutes
Library           ../pylib/Recharge.py
Variables         ../cfg.py

*** Test Cases ***
查询充值的银行卡信息-可调-tc007000-正常情况
    ${ret}    getBankCard
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

提现/提现列表-可调-tc007100-正常情况
    ${ret}    withdraw_list
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

充值可调-tc007200-正常情况
    ${ret}    recharge   100
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

提现可调-tc007300-正常情况
    ${ret}    withDraw   100
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200