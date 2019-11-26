*** Settings ***
Test Setup        sessiontoken
Test Timeout      2 minutes    #Test Setup    get sessiontoken AND connectdb    #Test Teardown    Disconnect From Database
Library           pylib.Account.Account
Library           pylib.Buy.Buy
Library           pylib.AboutMe
Library           pylib.Default.Default
Library           ../pylib/DataItem/Bank_Card.py
Library           pylib.Receive_address
Library           pylib.Payment
Variables         cfg.py
Library           DatabaseLibrary
Library           ../DB/connect_db.py

*** Test Cases ***
立即购买-tc0001000-正常情况
    ${ret1}    purchase    ${sessiontoken}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

转卖换钱接口-tc0001100-正常情况
    ${ret1}    resell    ${sessiontoken}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

立即转卖接口-tc0001200-正常情况
    ${ret1}    immedi_resell    ${sessiontoken}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

立即转卖确认转卖接口-tc0001300-未购买商品，立即转卖
    #获取商城id
    ${ret1}    goods_list    ${SPACE}    ${pageIndex}    ${pageSize}    ${sessiontoken}
    ${getid}    evaluate    $ret1['data']['page']['resultObj'][0]['id']
    ${id}    evaluate    str(${getid})
    #查看用户状态
    run_sql_normal_csorder    UPDATE \ cso_user_quota \ set \ state=2 where state != 2 and app_user_id = '2018072411313411360001336550'
    #获取银行卡信息id
    ${ret1}    bankcard_list    ${sessiontoken}
    ${bankInfoId}    evaluate    str($ret1['data']['bankCardList'][0]['id'])
    ${ret1}    immedi_resell_confirm    ${sessiontoken}    ${bankInfoId}    ${id}
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    没有权限

确认发货接口-tc0001400-正常情况
    #查看订单
    #0=待确认 1=购物订单 2=转卖订单'
    #信用支付
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
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}
    run_sql_normal_csorder    update cso_contract_msg set contract_Status=221 where id in(select a.id from(select id from \ cso_contract_msg where gmt_create =(select max(gmt_create) \ from \ cso_contract_msg))a)
    run_sql_normal_csmall    update csm_order set status=4,contract_status=221 where id in(select a.id from(select id from \ csm_order where gmt_create =(select max(gmt_create) \ from \ csm_order))a)
    run_sql_normal_csorder    update cso_repayment_plan set repayment_status=3 where id in(select a.id from(select id from \ cso_repayment_plan where gmt_create =(select max(gmt_create) \ from \ cso_repayment_plan))a)
    run_sql_normal_csmall    DELETE from csm_order ORDER BY id \ desc LIMIT 1
    run_sql_normal_csorder    DELETE from cso_contract_msg ORDER BY id \ desc LIMIT 1
信用支付确认支付接口-tc0001500-正常情况
    #列出收货地址，获取默认地址的id
    ${list}    Address_list    ${sessiontoken}
    @{Addresses}    evaluate    $list['data']['addresses']
    : FOR    ${a}    IN    @{Addresses}
    \    ${b}    evaluate    $a['tolerate']
    \    run keyword if    ${b}==1    log to console    ${a}['id']    Else    pass execution
    #默认地址id
    ${address_id}    evaluate    str(${a}['id'])
    ${ret1}    payment_confirm    ${sessiontoken}   2     7    ${address_id}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}
    run_sql_normal_csmall    DELETE from csm_order ORDER BY id \ desc LIMIT 1
    run_sql_normal_csorder    DELETE from cso_contract_msg ORDER BY id \ desc LIMIT 1

信用支付确认支付接口-tc0001501-正常情况
    #列出收货地址，获取默认地址的id
    ${list}    Address_list    ${sessiontoken}
    @{Addresses}    evaluate    $list['data']['addresses']
    : FOR    ${a}    IN    @{Addresses}
    \    ${b}    evaluate    $a['tolerate']
    \    run keyword if    ${b}==1    log to console    ${a}['id']    Else    pass execution
    #默认地址id
    ${address_id}    evaluate    str(${a}['id'])
    ${ret1}    payment_confirm    ${sessiontoken}     6     1    ${address_id}
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    用户额度不足

信用支付确认支付接口-tc0001502-借款期限不正确
    #列出收货地址，获取默认地址的id
    ${list}    Address_list    ${sessiontoken}
    @{Addresses}    evaluate    $list['data']['addresses']
    : FOR    ${a}    IN    @{Addresses}
    \    ${b}    evaluate    $a['tolerate']
    \    run keyword if    ${b}==1    log to console    ${a}['id']    Else    pass execution
    #默认地址id
    ${address_id}    evaluate    str(${a}['id'])
    ${ret1}    payment_confirm    ${sessiontoken}     6     7    ${address_id}
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    请选择合适的借款期限

转卖换钱确认转卖接口-tc0001600-正常情况
    #获取银行卡信息id
    ${ret1}    bankcard_list    ${sessiontoken}
    ${bankInfoId}    evaluate    str($ret1['data']['bankCardList'][0]['id'])
    ${ret1}    resell_confirm    ${sessiontoken}    7    ${bankInfoId}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}


*** Keywords ***
sessiontoken
    ${result}    biz    ${mobile}    ${password}    LOGIN
    ${token}    evaluate    $result['data']['sessionToken']
    set suite variable    ${sessiontoken}    ${token}
    user_obtain     ${token}
    run_sql_normal_csorder    UPDATE \ cso_user_quota \ set \ state=2,quota_control=100 where state != 2 and app_user_id = '2018072411313411360001336550'

