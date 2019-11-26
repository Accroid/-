*** Settings ***
Test Timeout      2 minutes
Library           ../pylib/Invite.py
Variables         ../cfg.py

*** Test Cases ***
邀请列表-tc003000-正常情况
    ${ret}    getInviteList
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

获取当前用户邀请码-tc003100-正常情况
    ${ret}    getInviteCode
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

获取邀请人信息-h5-tc003200-正常情况
    ${ret}    getUserByInviteCode
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200