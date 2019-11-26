*** Settings ***
Test Timeout      2 minutes
Library           pylib.Account.Account
Library           ../pylib/DataItem/Shumei.py
Variables         cfg.py

Test Setup      sessiontoken

*** Keywords ***
sessiontoken

    ${result}     biz    ${mobile}   ${password}  LOGIN
    ${token}    evaluate    $result['data']['sessionToken']
    set suite variable     ${sessiontoken}       ${token}

*** Test Cases ***
数美资料保存接口-tc0002800-正常情况
    ${ret1}    data_basic     ${sessiontoken}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

数美资料验证接口-tc0002900-正常情况
    ${ret1}    data_query     ${sessiontoken}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}