*** Settings ***
#Test Setup        get sessiontoken AND connectdb
#Test Teardown     Disconnect From Database
Test Timeout      2 minutes
Library           pylib.Account
Library           pylib.Buy
Library           pylib.Default.Default
Library           pylib.Receive_address
Library           pylib.Payment
Library           ../pylib/DataItem/Bank_Card.py
Library           ../pylib/LoanFlow/LoanQuery.py
Variables         cfg.py
Library           DatabaseLibrary
Library           ../DB/connect_db.py
Library           pylib.AboutMe

Test Setup      get sessiontoken AND connectdb

*** Keywords ***
get sessiontoken AND connectdb

    ${result}     biz    ${mobile}   ${password}  LOGIN
    ${token}    evaluate    $result['data']['sessionToken']
    set suite variable     ${sessiontoken}       ${token}
    user_obtain     ${token}
    run_sql_normal_csorder    UPDATE \ cso_user_quota \ set \ state=2,quota_control=100 where state != 2 and app_user_id = '2018072411313411360001336550'

#    Connect to database using custom params    pymysql    host='192.168.0.52',port=3306,user='test',passwd='csldata@2017',db='csldata'

Inparameter
    [Arguments]    ${statement}
    Execute Sql String    ${statement}

*** Test Cases ***
现金支付确认购买接口-tc0001800-正常情况
#productCode,productSku,receivingAddressId，bankInfoId必填
#先获取列表中第一个地址id
    ${ret}     Address_list    ${sessiontoken}
    ${address}   evaluate    $ret['data']['addresses'][0]
    ${address_id}   evaluate     $address['id']
    ${receivingAddressId}    evaluate    str(${address_id})
#获取第一张银行卡信息id
    ${bank}    bankcard_list     ${sessiontoken}
    ${bankid}  evaluate    $bank['data']['bankCardList'][0]['id']
    ${bankInfoId}    evaluate   str(${bankid})
#确认购买
    ${ret1}    purchase_Pay     ${sessiontoken}     ${receivingAddressId}   ${bankInfoId}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

现金支付确认购买接口-tc0001801-收货地址id为空
#productCode,productSku,receivingAddressId，bankInfoId必填
#收货地址为空
#获取第一张银行卡信息id
    ${bank}    bankcard_list     ${sessiontoken}
    ${bankid}  evaluate    $bank['data']['bankCardList'][0]['id']
    ${bankInfoId}    evaluate   str(${bankid})
#确认购买
    ${ret1}    purchase_Pay     ${sessiontoken}      ${SPACE}   ${bankInfoId}
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    收货地址id为空

立即还款接口-tc0001900-正常情况
#contractId,bizType必填
#bizType:CURRENT:当期还款，ALL：全部结清
#分期账单分期还款
    #列出收货地址，获取默认地址的id
    ${list}    Address_list    ${sessiontoken}
    @{Addresses}    evaluate    $list['data']['addresses']
    : FOR    ${a}    IN    @{Addresses}
    \    ${b}    evaluate    $a['tolerate']
    \    run keyword if    ${b}==1    log to console    ${a}['id']    Else    pass execution
    #通过默认地址id删除刚刚新添加的地址
    ${address_id}    evaluate    str(${a}['id'])
    ${ret1}    payment_confirm    ${sessiontoken}   2     7    ${address_id}
    #修改合同状态
    log to console    购物订单
    run_sql_normal_csorder    update cso_contract_msg set contract_Status=100 where id in(select a.id from(select id from \ cso_contract_msg where gmt_create =(select max(gmt_create) \ from \ cso_contract_msg))a)
    run_sql_normal_csmall    update csm_order set status=1,contract_status=100 where id in(select a.id from(select id from \ csm_order where gmt_create =(select max(gmt_create) \ from \ csm_order))a)
    ${ret}    order_list    ${sessiontoken}    ${pageIndex}    ${pageSize}
    ${getid}    evaluate    $ret['data']['page']['resultObj'][0]
    ${int_id}    evaluate    $getid['id']
    ${id}    evaluate    str(${int_id})
    ${ret1}    send_confirm    ${sessiontoken}    ${id}
#先获取合同ID
    ${ret}     Msg_state    ${sessiontoken}
    ${contractId}      evaluate    $ret['data']['contract']['contractId']
#立即还款（代发货状态）
    ${ret1}    bizNew     ${sessiontoken}       CURRENT    ${contractId}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}
    run_sql_normal_csorder    update cso_contract_msg set contract_Status=221 where id in(select a.id from(select id from \ cso_contract_msg where gmt_create =(select max(gmt_create) \ from \ cso_contract_msg))a)
    run_sql_normal_csmall    update csm_order set status=4,contract_status=221 where id in(select a.id from(select id from \ csm_order where gmt_create =(select max(gmt_create) \ from \ csm_order))a)
    run_sql_normal_csorder    update cso_repayment_plan set repayment_status=3 where id in(select a.id from(select id from \ cso_repayment_plan where gmt_create =(select max(gmt_create) \ from \ cso_repayment_plan))a)
    run_sql_normal_csmall    DELETE from csm_order ORDER BY id \ desc LIMIT 1
    run_sql_normal_csorder    DELETE from cso_contract_msg ORDER BY id \ desc LIMIT 1

立即还款接口-tc0001901-单期账单一次还清
#contractId,bizType必填
#bizType:CURRENT:当期还款，ALL：全部结清
#单期账单一次还清
    #列出收货地址，获取默认地址的id
    ${list}    Address_list    ${sessiontoken}
    @{Addresses}    evaluate    $list['data']['addresses']
    : FOR    ${a}    IN    @{Addresses}
    \    ${b}    evaluate    $a['tolerate']
    \    run keyword if    ${b}==1    log to console    ${a}['id']    Else    pass execution
    #通过默认地址id删除刚刚新添加的地址
    ${address_id}    evaluate    str(${a}['id'])
    ${ret1}    payment_confirm    ${sessiontoken}   2     7    ${address_id}
    #修改合同状态
    log to console    购物订单
    run_sql_normal_csorder    update cso_contract_msg set contract_Status=100 where id in(select a.id from(select id from \ cso_contract_msg where gmt_create =(select max(gmt_create) \ from \ cso_contract_msg))a)
    run_sql_normal_csmall    update csm_order set status=1,contract_status=100 where id in(select a.id from(select id from \ csm_order where gmt_create =(select max(gmt_create) \ from \ csm_order))a)
    ${ret}    order_list    ${sessiontoken}    ${pageIndex}    ${pageSize}
    ${getid}    evaluate    $ret['data']['page']['resultObj'][0]
    ${int_id}    evaluate    $getid['id']
    ${id}    evaluate    str(${int_id})
    ${ret1}    send_confirm    ${sessiontoken}    ${id}
#先获取合同ID
    ${ret}     Msg_state    ${sessiontoken}
    ${contractId}      evaluate    $ret['data']['contract']['contractId']
#立即还款（代发货状态）
    ${ret1}    bizNew     ${sessiontoken}       ALL   ${contractId}
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    当前状态不能一次性结清
    run_sql_normal_csorder    update cso_contract_msg set contract_Status=221 where id in(select a.id from(select id from \ cso_contract_msg where gmt_create =(select max(gmt_create) \ from \ cso_contract_msg))a)
    run_sql_normal_csmall    update csm_order set status=4,contract_status=221 where id in(select a.id from(select id from \ csm_order where gmt_create =(select max(gmt_create) \ from \ csm_order))a)
    run_sql_normal_csorder    update cso_repayment_plan set repayment_status=3 where id in(select a.id from(select id from \ cso_repayment_plan where gmt_create =(select max(gmt_create) \ from \ cso_repayment_plan))a)
    run_sql_normal_csmall    DELETE from csm_order ORDER BY id \ desc LIMIT 1
    run_sql_normal_csorder    DELETE from cso_contract_msg ORDER BY id \ desc LIMIT 1

立即还款接口-tc0001902-多期账单全部结清
#contractId,bizType必填
#bizType:CURRENT:当期还款，
#ALL：全部结清
    #列出收货地址，获取默认地址的id
    ${list}    Address_list    ${sessiontoken}
    @{Addresses}    evaluate    $list['data']['addresses']
    : FOR    ${a}    IN    @{Addresses}
    \    ${b}    evaluate    $a['tolerate']
    \    run keyword if    ${b}==1    log to console    ${a}['id']    Else    pass execution
    #通过默认地址id删除刚刚新添加的地址
    ${address_id}    evaluate    str(${a}['id'])
    ${ret1}    payment_confirm    ${sessiontoken}   1     2    ${address_id}
    #修改合同状态
    log to console    购物订单
    run_sql_normal_csorder    update cso_contract_msg set contract_Status=100 where id in(select a.id from(select id from \ cso_contract_msg where gmt_create =(select max(gmt_create) \ from \ cso_contract_msg))a)
    run_sql_normal_csmall    update csm_order set status=1,contract_status=100 where id in(select a.id from(select id from \ csm_order where gmt_create =(select max(gmt_create) \ from \ csm_order))a)
    ${ret}    order_list    ${sessiontoken}    ${pageIndex}    ${pageSize}
    ${getid}    evaluate    $ret['data']['page']['resultObj'][0]
    ${int_id}    evaluate    $getid['id']
    ${id}    evaluate    str(${int_id})
    ${ret1}    send_confirm    ${sessiontoken}    ${id}
##先获取合同ID
    ${ret}     Msg_state    ${sessiontoken}
    ${contractId}      evaluate    $ret['data']['contract']['contractId']
    run_sql_normal_csmall    update csm_order set status=3 where contract_no='${contractId}'
#立即还款（代发货状态）
    ${ret1}    bizNew     ${sessiontoken}       ALL   ${contractId}
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    请求成功
    run_sql_normal_csorder    update cso_contract_msg set contract_Status=221 where id in(select a.id from(select id from \ cso_contract_msg where gmt_create =(select max(gmt_create) \ from \ cso_contract_msg))a)
    run_sql_normal_csmall    update csm_order set status=4,contract_status=221 where id in(select a.id from(select id from \ csm_order where gmt_create =(select max(gmt_create) \ from \ csm_order))a)
    run_sql_normal_csorder    update cso_repayment_plan set repayment_status=3 where id in(select a.id from(select id from \ cso_repayment_plan where gmt_create =(select max(gmt_create) \ from \ cso_repayment_plan))a)
    run_sql_normal_csmall    DELETE from csm_order ORDER BY id \ desc LIMIT 1
    run_sql_normal_csorder    DELETE from cso_contract_msg ORDER BY id \ desc LIMIT 1

立即还款接口-tc0001903-合同ID为空
#contractId,bizType必填
#bizType:CURRENT:当期还款，ALL：全部结清

#立即还款（代发货状态
    ${ret1}    bizNew     ${sessiontoken}      CURRENT
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}   订单号有误

获取还款地址接口-tc0002000-正常情况
#contractId,bizType,bankInfoId必填
#bizType:CURRENT:当期还款，ALL：全部结清
#先获取合同ID
    ${ret}     Msg_state    ${sessiontoken}
    ${contractId}      evaluate    $ret['data']['contract']['contractId']
#获取第一张银行卡信息id
    ${bank}    bankcard_list     ${sessiontoken}
    ${bankid}  evaluate    $bank['data']['bankCardList'][0]['id']
    ${bankInfoId}    evaluate   str(${bankid})
#立即还款（代发货状态）
    ${ret1}    repay_link     ${sessiontoken}   ${contractId}   ALL   ${bankInfoId}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

获取还款地址接口-tc0002001-contractId为空
#contractId,bizType,bankInfoId必填
#bizType:CURRENT:当期还款，ALL：全部结清
    log to console   合同ID为空
#获取第一张银行卡信息id
    ${bank}    bankcard_list     ${sessiontoken}
    ${bankid}  evaluate    $bank['data']['bankCardList'][0]['id']
    ${bankInfoId}    evaluate   str(${bankid})
#立即还款（代发货状态）
    ${ret1}    repay_link     ${sessiontoken}   ${SPACE}   ALL   ${bankInfoId}
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    订单号有误

获取还款地址接口-tc0002002-bankInfoId为空
#contractId,bizType,bankInfoId必填
#bizType:CURRENT:当期还款，ALL：全部结清
    log to console   银行卡id为空
    #先获取合同ID
    ${ret}     Msg_state    ${sessiontoken}
    ${contractId}      evaluate    $ret['data']['contract']['contractId']
#立即还款（代发货状态）
    ${ret1}    repay_link     ${sessiontoken}   ${contractId}   ALL   ${SPACE}
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    请先绑定银行卡