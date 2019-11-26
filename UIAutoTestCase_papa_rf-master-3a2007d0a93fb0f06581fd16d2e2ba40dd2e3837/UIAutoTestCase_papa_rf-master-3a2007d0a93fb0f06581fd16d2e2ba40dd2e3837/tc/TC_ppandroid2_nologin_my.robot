*** Settings ***
Library  ../pylib/TC_ppandroid2_nologin_my.py



*** Test Cases ***
“我的”页面验证页面要素跳转-001
    ${ret}  test_nologin_my
    ${result1}   evaluate   $ret[0]
    run keyword and continue on failure   should be true    '${result1}' == 'True'
    ${result2}   evaluate   $ret[1]
    run keyword and continue on failure   should be true    '${result2}' == 'True'
    quit