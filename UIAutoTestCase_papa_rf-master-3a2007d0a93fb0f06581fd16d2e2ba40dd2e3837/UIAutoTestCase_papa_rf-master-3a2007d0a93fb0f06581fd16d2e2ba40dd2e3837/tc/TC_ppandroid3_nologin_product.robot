#*** Settings ***
#Library  ../pylib/TC_ppandroid3_nologin_product.py
##Library  ../pylib/TerminalHandle_TK.py
#
#
#*** Test Cases ***
#商品详情 验证各个模块点击跳转-001
#    ${ret}    test_addloan_have_nodata
#    ${result}   evaluate   $ret[0]
#    run keyword and continue on failure   should be true    '${result}' == 'True'
#    ${result1}   evaluate   $ret[1]
#    ${result2}   evaluate   $ret[2]
#    run keyword and continue on failure    should be equal    ${result1}    ${result2}
#    quit