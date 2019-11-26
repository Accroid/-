*** Settings ***
Test Setup        sessiontoken
Test Timeout      2 minutes
Library           pylib.Account.Account
Library           ../pylib/LoanFlow/LoanQuery.py
Variables         cfg.py
Library           ../pylib/LoanFlow/Application_Loan.py
Library           ../pylib/LoanFlow/LoanQuery.py
Library           pylib.Receive_address
Library           pylib.Payment
Library           ../DB/connect_db.py
Library           pylib.Buy.Buy
Library           pylib.Default.Default

*** Test Cases ***
我的贷款接口-tc0003900-正常情况
    ${ret1}    Msg_list    ${sessiontoken}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

贷款详情接口-tc0004000-正常情况
    #获取合同号id
    #还款中和逾期的才能调这个接口
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
    #查询合同id
    ${contract}    order_detail    ${sessiontoken}    ${id}
    ${contractId}    evaluate    $contract['data']['order']['contractOrder']['orderNo']
    ${ret1}    Msg_detail    ${sessiontoken}    ${contractId}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}
    run_sql_normal_csorder    update cso_contract_msg set contract_Status=221 where id in(select a.id from(select id from \ cso_contract_msg where gmt_create =(select max(gmt_create) \ from \ cso_contract_msg))a)
    run_sql_normal_csmall    update csm_order set status=4,contract_status=221 where id in(select a.id from(select id from \ csm_order where gmt_create =(select max(gmt_create) \ from \ csm_order))a)
    run_sql_normal_csorder    update cso_repayment_plan set repayment_status=3 where id in(select a.id from(select id from \ cso_repayment_plan where gmt_create =(select max(gmt_create) \ from \ cso_repayment_plan))a)
    run_sql_normal_csmall    DELETE from csm_order ORDER BY id \ desc LIMIT 1
    run_sql_normal_csorder    DELETE cso_contract_msg ORDER BY id \ desc LIMIT 1

贷款详情接口-tc0004001-合同Id为空
    #获取合同号id
    #还款中和逾期的才能调这个接口
    ${ret1}    Msg_detail    ${sessiontoken}    ${SPACE}
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    订单号有误

还款计划接口-tc0004100-正常情况
    #获取合同号id
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
    #查询合同id
    ${contract}    order_detail    ${sessiontoken}    ${id}
    ${contractId}    evaluate    $contract['data']['order']['contractOrder']['orderNo']
    ${ret1}    Msg_repayments    ${sessiontoken}    ${contractId}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

还款计划接口-tc0004101-合同id为空
    #获取合同号id
    ${ret1}    Msg_repayments    ${sessiontoken}    ${SPACE}
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    合同号有误

订单状态接口-tc0004200-正常情况
    ${ret1}    Msg_state    ${sessiontoken}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

*** Keywords ***
sessiontoken
    ${result}    biz    ${mobile}    ${password}    LOGIN
    ${token}    evaluate    $result['data']['sessionToken']
    set suite variable    ${sessiontoken}    ${token}
