*** Settings ***
Test Timeout      2 minutes
Library           ../pylib/Help.py
Variables         ../cfg.py

*** Test Cases ***
精选活动列表-tc001000-正常情况
    ${ret}    activityList
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

官方公告列表-tc001100-正常情况
    ${ret}    activityList
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

根据类型获取问题列表-tc001200-正常情况
#获取问题类型
    ${result}     getHelpTypeList
    ${typeId}    evaluate    $result['data']['list'][0]['id']
#获取问题列表
    ${ret}    findListByTypeId    ${typeId}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

根据类型获取问题列表-tc001201-类型为空
##获取问题类型
#    ${result}     getHelpTypeList
#    ${typeId}    evaluate    $result['data']['list'][0]['id']
#获取问题列表
    ${ret}    findListByTypeId    ${None}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    对不起，参数异常
    should contain   ${ret2}    500

热门问题-tc001300-正常情况
    ${ret}    getHotList
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

官方公告详情-tc001400-正常情况
    ${ret}    getNewsInfo    ${newsId}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

官方公告详情-tc001401-公告ID为空
    ${ret}    getNewsInfo    ${None}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

帮助类型列表-tc008000
    ${ret}    getHelpTypeList
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200