*** Settings ***
Library  ../pylib/TC_ppandroid8_buy_below.py



*** Test Cases ***
#新用户额度低于商品价格，进行购买商品流程-001
#    ${ret}    test_buy_below1
#    ${result1}    evaluate   $ret[0]
#    ${result2}    evaluate   $ret[1]
#    ${result3}    evaluate   $ret[2]
#    ${result4}    evaluate   $ret[3]
#    ${result5}    evaluate   $ret[4]
#    ${result6}    evaluate   $ret[5]
#    run keyword and continue on failure    should be equal    ${result1}   ${result2}
#    run keyword and continue on failure    should be equal    ${result3}   ${result4}
#    run keyword and continue on failure    should be equal    ${result5}   ${result6}


确认购买页面选中现金支付，点击确认购买按钮-001
    ${ret}    test_buy_below2
    ${result1}    evaluate   $ret[0]
    ${result2}    evaluate   $ret[1]
    ${result3}    evaluate   $ret[2]
    run keyword and continue on failure    should be true    '${result1}' == 'True'
    run keyword and continue on failure    should be true    '${result2}' == 'True'
    run keyword and continue on failure    should be true    '${result3}' == 'True'


在编辑地址页面不输入任何数据，点击保存按钮-001
    ${ret}    test_buy_below3
    ${result1}    evaluate   $ret[0]
    ${result2}    evaluate   $ret[1]
    run keyword and continue on failure    should be equal    ${result1}    ${result2}
    quit