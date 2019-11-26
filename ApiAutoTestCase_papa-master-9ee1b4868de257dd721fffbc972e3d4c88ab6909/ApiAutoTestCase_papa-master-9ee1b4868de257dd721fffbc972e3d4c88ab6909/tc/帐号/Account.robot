*** Settings ***
Test Timeout      2 minutes
Library           pylib.Account.Account
Variables         cfg.py

Test Setup      sessiontoken

*** Keywords ***
sessiontoken

    ${result}     biz    ${mobile}   ${password}  LOGIN
    ${token}    evaluate    $result['data']['sessionToken']
    set suite variable     ${sessiontoken}       ${token}

*** Test Cases ***
检查是否注册用户接口-tc0000001-正常情况
    ${ret1}    check_registry    ${mobile}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

检查是否注册用户接口-tc0000002-输入未注册手机号
    ${ret1}    check_registry    18143480000
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

检查是否注册用户接口-tc0000003-输入错误格式的手机号
    ${ret1}    check_registry    181434800000
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    手机号格式错误

检查是否注册用户接口-tc0000004-手机号输入为空
    ${ret1}    check_registry
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    手机号格式错误

检查是否注册用户接口-tc0000005-手机号输入为空格
    ${ret1}    check_registry    ${SPACE}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    手机号格式错误

检查是否注册用户接口-tc0000006-手机号输入为特殊字符
    ${ret1}    check_registry    ☺
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    手机号格式错误

用户登录，注册，重置密码，退出接口-tc0000100-正常情况
    ${ret1}    biz    ${mobile}   ${password}  LOGIN
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    登录成功
    should be true    $ret1['result']['success']==${true}

用户登录，注册，重置密码，退出接口-tc0000101-手机号输入为空
    ${ret1}    biz    None   ${password}  LOGIN
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    手机号格式错误

用户登录，注册，重置密码，退出接口-tc0000102-密码输入为空
    ${ret1}    biz    ${mobile}   None   LOGIN
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    请输入6-16位英文数字组合作为密码

用户登录，注册，重置密码，退出接口-tc0000103-密码为错误的密码，长度错误
    ${ret1}    biz    ${mobile}     1     LOGIN
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    请输入6-16位英文数字组合作为密码

用户登录，注册，重置密码，退出接口-tc0000104-密码为错误的密码
    ${ret1}    biz    ${mobile}     123456789     LOGIN
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    密码错误，请重试

