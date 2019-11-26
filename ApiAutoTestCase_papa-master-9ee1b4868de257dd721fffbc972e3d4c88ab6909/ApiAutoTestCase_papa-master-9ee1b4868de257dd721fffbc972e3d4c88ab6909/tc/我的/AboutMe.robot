*** Settings ***
Test Timeout      2 minutes
Library           pylib.Account
Library           pylib.Buy
Library           pylib.Default.Default
Library           pylib.Receive_address
Library           pylib.Payment
Library           pylib.AboutMe
Library           ../pylib/DataItem/Bank_Card.py
Library           ../pylib/LoanFlow/LoanQuery.py
Variables         cfg.py
#Resource          ../rflib/KeyWords.robot
Library           ../DB/connect_db.py

Test Setup      sessiontoken

*** Keywords ***
sessiontoken

    ${result}     biz    ${mobile}   ${password}  LOGIN
    ${token}    evaluate    $result['data']['sessionToken']
    set suite variable     ${sessiontoken}       ${token}

*** Test Cases ***
用户账户信息查询接口-tc0000200-正常情况
    ${ret1}    user_info     ${sessiontoken}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

用户状态接口-tc0002100-正常情况
    ${ret1}    user_state     ${sessiontoken}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

额度估值接口-tc0002200-正常情况
    ${ret1}    user_obtain     ${sessiontoken}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}
    run_sql_normal_csorder    UPDATE \ cso_user_quota \ set \ state=2,quota_control=100 where state != 2 and app_user_id = '2018072411313411360001336550'

认证中心接口-tc0002300-正常情况
    ${ret1}    user_obtain     ${sessiontoken}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}