*** Settings ***
Test Timeout      2 minutes
Library           pylib.Account.Account
Library           ../pylib/DataItem/Certification.py
Variables         cfg.py

Test Setup      sessiontoken

*** Keywords ***
sessiontoken

    ${result}     biz    ${mobile}   ${password}  LOGIN
    ${token}    evaluate    $result['data']['sessionToken']
    set suite variable     ${sessiontoken}       ${token}

*** Test Cases ***
检测是否可以修改实名信息接口-tc0003600-正常情况
    ${ret1}    Certification_Check     ${sessiontoken}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

资料填写进度接口-tc0003700-正常情况
    ${ret1}    Fill_progress     ${sessiontoken}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}