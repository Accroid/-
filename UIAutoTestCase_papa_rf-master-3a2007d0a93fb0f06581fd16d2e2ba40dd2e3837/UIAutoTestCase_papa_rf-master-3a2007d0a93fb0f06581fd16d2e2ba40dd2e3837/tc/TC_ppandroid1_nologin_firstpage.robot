*** Settings ***
Library  ../pylib/TC_ppandroid1_nologin_firstpage.py



*** Test Cases ***
首页-有好货页面页面元素验证-001
    ${ret}    test_nologin_firstpage
    ${result1}   evaluate   $ret[0]
    run keyword and continue on failure   should be true    '${result1}' == 'True'
    ${result2}   evaluate   $ret[1]
    run keyword and continue on failure   should be true    '${result2}' == 'True'
    ${result3}   evaluate   $ret[2]
    run keyword and continue on failure   should be true    '${result3}' == 'True'
    ${result4}   evaluate   $ret[2]
    run keyword and continue on failure   should be true    '${result4}' == 'True'
    quit


