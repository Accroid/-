*** Settings ***
Test Timeout      2 minutes
Library           pylib.Account.Account
Library           ../pylib/LoanFlow/Application_Loan.py
Library           ../pylib/LoanFlow/LoanQuery.py
Variables         cfg.py
Library           pylib.Receive_address
Library           pylib.Payment
Library           ../DB/connect_db.py
Library           pylib.Buy.Buy
Library           ../pylib/LoanFlow/LoanQuery.py
Library           pylib.Default.Default

Test Setup      sessiontoken

*** Keywords ***
sessiontoken

    ${result}     biz    ${mobile}   ${password}  LOGIN
    ${token}    evaluate    $result['data']['sessionToken']
    set suite variable     ${sessiontoken}       ${token}

*** Test Cases ***
#签约信息查询接口-tc0004400
##获取合同号id
##还款中可查
#    #信用支付
#    #列出收货地址，获取默认地址的id
#    ${list}    Address_list    ${sessiontoken}
#    @{Addresses}    evaluate    $list['data']['addresses']
#    : FOR    ${a}    IN    @{Addresses}
#    \    ${b}    evaluate    $a['tolerate']
#    \    run keyword if    ${b}==1    log to console    ${a}['id']    Else    pass execution
#    #获取默认地址id
#    ${address_id}    evaluate    str(${a}['id'])
#    ${ret1}    payment_confirm    ${sessiontoken}    7    ${address_id}
#    #修改合同状态
#    log to console    购物订单
##    run_sql_normal_csorder    update cso_contract_msg set contract_Status=90 where id in(select a.id from(select id from \ cso_contract_msg where gmt_create =(select max(gmt_create) \ from \ cso_contract_msg))a)
#    ${ret}    order_list    ${sessiontoken}    ${pageIndex}    ${pageSize}
#    ${getid}    evaluate    $ret['data']['page']['resultObj'][0]
#    ${int_id}    evaluate    $getid['id']
#    ${id}    evaluate    str(${int_id})
#    ${ret1}    send_confirm    ${sessiontoken}    ${id}
#    #查询合同id
#    ${contract}    order_detail     ${sessiontoken}   ${id}
#    ${contractId}   evaluate   $contract['data']['order']['contractOrder']['orderNo']
#    #查询签约信息
#    ${ret1}    Sign_Query     ${sessiontoken}     ${contractId}
#    ${ret2}    evaluate    $ret1['result']['message']
#    should be equal    ${ret2}    请求成功
#    should be true    $ret1['result']['success']==${true}
#    run_sql_normal_csmall    DELETE from csm_order ORDER BY id \ desc LIMIT 1
#    run_sql_normal_csorder    DELETE cso_contract_msg ORDER BY id \ desc LIMIT 1

提交订单开始签约接口-tc0004500-正常情况

    #提交订单金额
    ${ret1}    Apply_Engage     ${sessiontoken}
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    申请提交成功
    should be true    $ret1['result']['success']==${true}
    run_sql_normal_csmall    DELETE from csm_order ORDER BY id \ desc LIMIT 1
    run_sql_normal_csorder    DELETE from cso_contract_msg ORDER BY id \ desc LIMIT 1

提交订单开始签约接口-tc0004600-未结清重新下单

    #提交订单金额
    ${ret1}    Apply_Engage     ${sessiontoken}
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    申请提交成功
    should be true    $ret1['result']['success']==${true}
    #重复一条订单，原先订单未结清
    ${ret}    Apply_Engage     ${sessiontoken}
    ${ret3}    evaluate    $ret['result']['message']
    should contain    ${ret3}    操作失败，用户有未结清订单
    run_sql_normal_csmall    DELETE from csm_order ORDER BY id \ desc LIMIT 1
    run_sql_normal_csorder    DELETE from cso_contract_msg ORDER BY id \ desc LIMIT 1