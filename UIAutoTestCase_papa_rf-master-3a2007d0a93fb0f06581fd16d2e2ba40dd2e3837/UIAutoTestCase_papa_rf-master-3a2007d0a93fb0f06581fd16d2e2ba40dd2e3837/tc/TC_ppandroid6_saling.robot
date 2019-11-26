*** Settings ***
Library  ../pylib/TC_ppandroid6_saling.py


*** Test Cases ***
首次注册用户，已填写资料认证，进行转卖流程-001
    ${ret}    test_saling
    ${result}   evaluate   $ret
    run keyword and continue on failure   should be true    '${result}' == 'True'
    quit