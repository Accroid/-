*** Settings ***
Library  ../pylib/TC_ppandroid5_old.py



*** Test Cases ***
在登陆账号框内输入错误的手机号（字符类型）-001
    ${ret}    test_old1
    run keyword and continue on failure   should be true    '${ret}' == 'True'


老用户登陆验证，输入已注册的手机号，点击下一步按钮，点击忘记密码按钮-001
    ${ret}    test_old2
    run keyword and continue on failure   should be true    '${ret}' == 'True'


老用户登陆验证，在找回密码页面不输入任何数据，点击完成-001
    ${ret}    test_old3
    run keyword and continue on failure   should be true    '${ret}' == 'True'


在找回密码页面输入错误的密码（长度错误），点击完成-001
    ${ret}    test_old4
    run keyword and continue on failure   should be true    '${ret}' == 'True'


在找回密码页面输入错误的密码（长度错误），点击完成-001
    test_old5
    quit

