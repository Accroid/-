*** Settings ***
Library  ../pylib/TC_ppandroid9_buy_above.py



*** Test Cases ***
新用户估值额度高于商品价格进行信用支付购买商品流程，购买到待发货-001
    test_buy_above1


订单为待发货状态，且卡内余额等于还款金额，进行还款操作-001
    ${ret}    test_buy_above2
    ${result1}    evaluate   $ret[0]
    ${result2}    evaluate   $ret[1]
    ${result3}    evaluate   $ret[2]
    ${result4}    evaluate   $ret[3]
#    ${result5}    evaluate   $ret[4]
    run keyword and continue on failure    should be equal    ${result1}   ${result2}
    run keyword and continue on failure    should be equal    ${result3}   ${result4}
#    run keyword and continue on failure   should be true    '${result5}' == 'True'


订单为已发货状态，且卡内余额等于还款金额，进行还款操作-001
    ${ret}    test_buy_above3
    ${result1}    evaluate   $ret[0]
    ${result2}    evaluate   $ret[1]
    ${result3}    evaluate   $ret[2]
    run keyword and continue on failure    should be equal    ${result1}   ${result2}
    run keyword and continue on failure   should be true    '${result3}' == 'True'
    quit

#订单为已完成状态，且卡内余额等于还款金额，进行还款操作-001
#    ${ret}    test_buy_above4
#    ${result1}    evaluate   $ret[0]
#    ${result2}    evaluate   $ret[1]
#    ${result3}    evaluate   $ret[2]
#    ${result4}    evaluate   $ret[3]
#    ${result5}    evaluate   $ret[4]
#    run keyword and continue on failure    should be equal    ${result1}   ${result2}
#    run keyword and continue on failure    should be equal    ${result3}   ${result4}
#    run keyword and continue on failure   should be true    '${result5}' == 'True'
#    quit