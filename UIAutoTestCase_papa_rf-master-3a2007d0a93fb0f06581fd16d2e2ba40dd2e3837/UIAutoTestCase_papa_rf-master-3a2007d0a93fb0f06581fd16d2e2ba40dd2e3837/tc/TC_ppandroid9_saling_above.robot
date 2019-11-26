*** Settings ***
Library  ../pylib/TC_ppandroid9_saling_above.py


*** Test Cases ***
单期转卖成功，还款，银行卡余额等于还款金额-001
    ${ret}    test_saling_above1
    ${result1}    evaluate   $ret[0]
    ${result2}    evaluate   $ret[1]
    run keyword and continue on failure    should be equal    ${result1}    ${result2}


转卖选择多期，提前结清，点击查看还款计划-001
    ${ret}    test_saling_above2
    ${result1}    evaluate   $ret[0]
    ${result2}    evaluate   $ret[1]
    run keyword and continue on failure    should be equal    ${result1}    ${result2}


多期转卖成功，已存在逾期，点击查看还款计划-001
    ${ret}    test_saling_above3
    ${result1}    evaluate   $ret[0]
    ${result2}    evaluate   $ret[1]
    run keyword and continue on failure    should be equal    ${result1}    ${result2}
    quit