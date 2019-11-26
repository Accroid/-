*** Settings ***
Test Timeout      2 minutes
Library           ../pylib/Index.py
Variables         ../cfg.py

*** Test Cases ***
获取更新-tc002000-正常情况
    ${ret}    getAppUpdate
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

首页-banner-可调-tc002100-正常情况
    ${ret}    getBanner
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

首页-项目-可调-tc002200-正常情况
    ${ret}    project
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200