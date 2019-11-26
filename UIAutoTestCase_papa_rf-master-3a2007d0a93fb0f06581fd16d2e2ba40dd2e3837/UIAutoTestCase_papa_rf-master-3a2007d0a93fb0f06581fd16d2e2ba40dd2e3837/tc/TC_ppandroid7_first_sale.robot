#*** Settings ***
#Library  ../pylib/TC_ppandroid7_first_sale.py
#
#
#
#*** Test Cases ***
#新用户第一次转卖流程验证，首页点击banner，并选择一个热卖商品点-001
#    ${ret}    test_first_sale1
#    ${result}   evaluate   $ret
#    run keyword and continue on failure   should be true    '${result}' == 'True'
#    quit