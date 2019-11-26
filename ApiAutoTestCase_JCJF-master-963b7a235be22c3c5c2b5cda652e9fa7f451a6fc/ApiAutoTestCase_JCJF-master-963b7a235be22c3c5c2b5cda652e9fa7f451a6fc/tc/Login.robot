*** Settings ***
Test Timeout      2 minutes
Library           ../pylib/Login.py
Variables         ../cfg.py

*** Test Cases ***
用户登陆-tc004000-正常情况
#mobile,password,accountType,userType
    ${ret}    login    ${mobile}    ${password}    ${accountType}    ${userType}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

用户登陆-tc004001-密码错误
#mobile,password,accountType,userType
    ${ret}    login    ${mobile}    123456    ${accountType}    ${userType}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    用户密码错误
    should contain   ${ret2}    10002

用户登陆-tc004002-accountType为空
#mobile,password,accountType,userType
    ${ret}    login    ${mobile}    ${password}    ${None}    ${userType}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    accountType不能为空
    should contain   ${ret2}    500

#用户登陆-tc004003-userType为空
##mobile,password,accountType,userType
#    ${ret}    login    ${mobile}    ${password}    ${accountType}    ${None}
#    ${ret1}    evaluate   $ret['result']['message']
#    ${ret2}    evaluate   $ret['result']['code']
#    should be equal   ${ret1}    对不起，参数异常
#    should contain   ${ret2}    500

用户登陆-tc004004-手机号少于11位
#mobile,password,accountType,userType
    ${ret}    login    1863040911    ${password}    ${accountType}    ${userType}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should contain   ${ret1}    手机号码格式错误,请重新输入
    should contain   ${ret2}    3005

用户登陆-tc004005-手机号大于11位
#mobile,password,accountType,userType
    ${ret}    login    186304091151    ${password}    ${accountType}    ${userType}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should contain   ${ret1}    手机号码格式错误,请重新输入
    should contain   ${ret2}    3005

用户登陆-tc004006-手机号为中文
#mobile,password,accountType,userType
    ${ret}    login    哈哈    ${password}    ${accountType}    ${userType}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should contain   ${ret1}    手机号码格式错误,请重新输入
    should contain   ${ret2}    3005

用户登陆-tc004007-密码输入为空
#mobile,password,accountType,userType
    ${ret}    login    ${mobile}    ${SPACE}    ${accountType}    ${userType}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should contain   ${ret1}    用户密码错误
    should contain   ${ret2}    10002

用户登陆-tc004008-密码输入为中文
#mobile,password,accountType,userType
    ${ret}    login    ${mobile}    哈哈    ${accountType}    ${userType}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    用户密码错误
    should contain   ${ret2}    10002

#获取签章授权URL-tc004100-正常情况
#    ${ret}    fadada_authorize
#    ${ret1}    evaluate   $ret['result']['message']
#    ${ret2}    evaluate   $ret['result']['code']
#    should be equal   ${ret1}    成功
#    should contain   ${ret2}    200

是否已注册-tc004200-正常情况
#mobile,accountType,userType
    ${ret}    isRegistered    ${mobile}   ${accountType}   ${userType}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

是否已注册-tc004201-手机号为空
#mobile,accountType,userType
    ${ret}    isRegistered    ${SPACE}   ${accountType}   ${userType}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

是否已注册-tc004202-accountType为空
#mobile,accountType,userType
    ${ret}    isRegistered    ${mobile}   ${None}   ${userType}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    accountType不能为空
    should contain   ${ret2}    500

#是否已注册-tc004203-userType为空
##mobile,accountType,userType
#    ${ret}    isRegistered    ${mobile}   ${accountType}   ${None}
#    ${ret1}    evaluate   $ret['result']['message']
#    ${ret2}    evaluate   $ret['result']['code']
#    should be equal   ${ret1}    对不起，参数异常
#    should contain   ${ret2}    500