*** Settings ***
Library  ../pylib/TC_ppandroid4_new.py



*** Test Cases ***
新用户注册验证，在登陆账号框内输入错误的手机号（长度）-001
    ${ret}    test_new1
    run keyword and continue on failure   should be true    '${ret}' == 'True'


新用户注册验证，在登陆账号框内输入错误的手机号（字符类型）-001
    ${ret}    test_new2
    run keyword and continue on failure   should be true    '${ret}' == 'True'



新用户注册验证，在登陆账号框内输入未注册过的手机号，点击下一步，并在设置密码页面输入不符合密码规则的密码（长度）-001
    ${ret}    test_new3
    ${result1}   evaluate   $ret[0]
    run keyword and continue on failure   should be true    '${result1}' == 'True'
    ${result2}   evaluate   $ret[1]
    run keyword and continue on failure    should not be empty    '${ret}' == 'True'
    quit