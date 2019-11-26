*** Settings ***
Test Timeout      2 minutes
Library           pylib.Account.Account
Library           ../pylib/LoanFlow/Repayment.py
Variables         cfg.py
Library           ../pylib/LoanFlow/LoanQuery.py
Library           ../pylib/LoanFlow/Application_Loan.py
Library           ../pylib/LoanFlow/LoanQuery.py
Library           pylib.Receive_address
Library           pylib.Payment
Library           ../DB/connect_db.py
Library           pylib.Buy.Buy
Library           pylib.Default.Default

Test Setup      sessiontoken

*** Keywords ***
sessiontoken

    ${result}     biz    ${mobile}   ${password}  LOGIN
    ${token}    evaluate    $result['data']['sessionToken']
    set suite variable     ${sessiontoken}       ${token}

*** Test Cases ***
还款接口-tc0004300-还款中状态
#获取合同号
#还款中
    #列出收货地址，获取默认地址的id
    ${list}    Address_list    ${sessiontoken}
    @{Addresses}    evaluate    $list['data']['addresses']
    : FOR    ${a}    IN    @{Addresses}
    \    ${b}    evaluate    $a['tolerate']
    \    run keyword if    ${b}==1    log to console    ${a}['id']    Else    pass execution
    #获取默认地址id
    ${address_id}    evaluate    str(${a}['id'])
    ${ret1}    payment_confirm    ${sessiontoken}    2    7    ${address_id}
    #修改合同状态
    log to console    购物订单
    run_sql_normal_csorder    update cso_contract_msg set contract_Status=212 where id in(select a.id from(select id from \ cso_contract_msg where gmt_create =(select max(gmt_create) \ from \ cso_contract_msg))a)
    run_sql_normal_csmall    update csm_order set status=1,contract_status=212 where id in(select a.id from(select id from \ csm_order where gmt_create =(select max(gmt_create) \ from \ csm_order))a)
    ${ret}    order_list    ${sessiontoken}    ${pageIndex}    ${pageSize}
    ${getid}    evaluate    $ret['data']['page']['resultObj'][0]
    ${int_id}    evaluate    $getid['id']
    ${id}    evaluate    str(${int_id})
    ${ret1}    send_confirm    ${sessiontoken}    ${id}
    #查询合同id
    ${contract}    order_detail    ${sessiontoken}    ${id}
    ${contractId}    evaluate    $contract['data']['order']['contractOrder']['orderNo']
    ${ret1}    repay_biz     ${sessiontoken}      ${contractId}    CURRENT
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}
    run_sql_normal_csorder    update cso_contract_msg set contract_Status=221 where id in(select a.id from(select id from \ cso_contract_msg where gmt_create =(select max(gmt_create) \ from \ cso_contract_msg))a)
    run_sql_normal_csmall    update csm_order set status=4,contract_status=221 where id in(select a.id from(select id from \ csm_order where gmt_create =(select max(gmt_create) \ from \ csm_order))a)
    run_sql_normal_csorder    update cso_repayment_plan set repayment_status=3 where id in(select a.id from(select id from \ cso_repayment_plan where gmt_create =(select max(gmt_create) \ from \ cso_repayment_plan))a)

    run_sql_normal_csmall    DELETE from csm_order ORDER BY id \ desc LIMIT 1
    run_sql_normal_csorder    DELETE cso_contract_msg ORDER BY id \ desc LIMIT 1

还款接口-tc0004301-逾期状态
#获取合同号
#逾期
    #列出收货地址，获取默认地址的id
    ${list}    Address_list    ${sessiontoken}
    @{Addresses}    evaluate    $list['data']['addresses']
    : FOR    ${a}    IN    @{Addresses}
    \    ${b}    evaluate    $a['tolerate']
    \    run keyword if    ${b}==1    log to console    ${a}['id']    Else    pass execution
    #获取默认地址id
    ${address_id}    evaluate    str(${a}['id'])
    ${ret1}    payment_confirm    ${sessiontoken}    2    7    ${address_id}
    #修改合同状态
    log to console    购物订单
    run_sql_normal_csorder    update cso_contract_msg set contract_Status=100 where id in(select a.id from(select id from \ cso_contract_msg where gmt_create =(select max(gmt_create) \ from \ cso_contract_msg))a)
    run_sql_normal_csmall    update csm_order set status=1,contract_status=100 where id in(select a.id from(select id from \ csm_order where gmt_create =(select max(gmt_create) \ from \ csm_order))a)
    ${ret}    order_list    ${sessiontoken}    ${pageIndex}    ${pageSize}
    ${getid}    evaluate    $ret['data']['page']['resultObj'][0]
    ${int_id}    evaluate    $getid['id']
    ${id}    evaluate    str(${int_id})
    ${ret1}    send_confirm    ${sessiontoken}    ${id}
    run_sql_normal_csorder    update cso_contract_msg set contract_Status=230 where id in(select a.id from(select id from \ cso_contract_msg where gmt_create =(select max(gmt_create) \ from \ cso_contract_msg))a)
    run_sql_normal_csmall    update csm_order set status=1,contract_status=230 where id in(select a.id from(select id from \ csm_order where gmt_create =(select max(gmt_create) \ from \ csm_order))a)
    run_sql_normal_csorder    update cso_repayment_plan set repayment_status=4 where id in(select a.id from(select id from \ cso_repayment_plan where gmt_create =(select max(gmt_create) \ from \ cso_repayment_plan))a)
    #查询合同id
    ${contract}    order_detail    ${sessiontoken}    ${id}
    ${contractId}    evaluate    $contract['data']['order']['contractOrder']['orderNo']
    ${ret1}    repay_biz     ${sessiontoken}      ${contractId}    CURRENT
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}
    run_sql_normal_csorder    update cso_contract_msg set contract_Status=221 where id in(select a.id from(select id from \ cso_contract_msg where gmt_create =(select max(gmt_create) \ from \ cso_contract_msg))a)
    run_sql_normal_csmall    update csm_order set status=4,contract_status=221 where id in(select a.id from(select id from \ csm_order where gmt_create =(select max(gmt_create) \ from \ csm_order))a)
    run_sql_normal_csorder    update cso_repayment_plan set repayment_status=3 where id in(select a.id from(select id from \ cso_repayment_plan where gmt_create =(select max(gmt_create) \ from \ cso_repayment_plan))a)
    run_sql_normal_csmall    DELETE from csm_order ORDER BY id \ desc LIMIT 1
    run_sql_normal_csorder    DELETE cso_contract_msg ORDER BY id \ desc LIMIT 1

还款接口-tc0004302-合同id为空
    ${ret1}    repay_biz     ${sessiontoken}      ${SPACE}    CURRENT
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    订单号有误
