*** Settings ***
Test Timeout      2 minutes    #Test Setup    get sessiontoken AND connectdb    #Test Teardown    Disconnect From Database
Library           pylib.Account
Library           pylib.Buy
Library           pylib.Default.Default
Library           pylib.Receive_address
Library           pylib.Payment
Library           ../pylib/DataItem/Bank_Card.py
Library           ../pylib/LoanFlow/LoanQuery.py
Variables         cfg.py
Library           DatabaseLibrary


Test Setup      sessiontoken

*** Keywords ***
sessiontoken

    ${result}     biz    ${mobile}   ${password}  LOGIN
    ${token}    evaluate    $result['data']['sessionToken']
    set suite variable     ${sessiontoken}       ${token}

*** Test Cases ***
收货地址新增-tc0002400-正常情况
    #id,name,phone,province,city,district,detail,tolerate
    #tolerate：0否，1是
    ${ret1}    Address_Update    ${sessiontoken}    李四    18143482201    浙江省
    ...    杭州市    西湖区    双龙街199号    1
    #列出收货地址，获取默认地址的id
    ${list}    Address_list    ${sessiontoken}
    @{Addresses}    evaluate    $list['data']['addresses']
    : FOR    ${a}    IN    @{Addresses}
    \    ${b}    evaluate    $a['tolerate']
    \    run keyword if    ${b}==1    log to console     ${a}['id']
    \    ...    ELSE    log     跳过
    #通过默认地址id删除刚刚新添加的地址
    ${address_id}     evaluate     str(${a}['id'])
    ${ret}    Address_delete    ${sessiontoken}    ${address_id}
    ${ret2}    evaluate    $ret['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

收货地址更新-tc0002401-正常情况
    #id,name,phone,province,city,district,detail,tolerate
    #tolerate：0否，1是
    ${ret1}    Address_Update    ${sessiontoken}    李四    18143482201    浙江省
    ...    杭州市    西湖区    双龙街199号    1
    #列出收货地址，获取默认地址的id
    ${list}    Address_list    ${sessiontoken}
    @{Addresses}    evaluate    $list['data']['addresses']
    : FOR    ${a}    IN    @{Addresses}
    \    ${b}    evaluate    $a['tolerate']
    \    run keyword if    ${b}==1    log    ${a}
    \    exit for loop
    ${default_id}    evaluate   str($a['id'])
    #更新地址
    ${ret1}    Address_Update    ${sessiontoken}    王二    18143482201    浙江省
    ...    杭州市    西湖区    双龙街199号    1    ${default_id}
    ${list1}    Address_list    ${sessiontoken}
    @{Addresse}    evaluate    $list1['data']['addresses']
    : FOR    ${a1}    IN    @{Addresse}
    \    ${b1}    evaluate    $a1['tolerate']
    \    run keyword if    ${b1}==1    log    ${a1}
    \    exit for loop
    ${default_id1}    evaluate   str($a1['id'])
    #通过默认地址id删除刚刚新添加的地址
    ${ret}    Address_delete    ${sessiontoken}    ${default_id1}
    ${ret2}    evaluate    $ret['result']['message']
    should contain    ${ret2}    请求成功

收货地址新增-tc0002402-收货人为空
    #id,name,phone,province,city,district,detail,tolerate
    #tolerate：0否，1是
    ${ret1}    Address_Update    ${sessiontoken}    ${SPACE}   18143482201    浙江省
    ...    杭州市    西湖区    双龙街199号    1
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    收货人为空

收货地址新增-tc0002403-手机号为空
    #id,name,phone,province,city,district,detail,tolerate
    #tolerate：0否，1是
    ${ret1}    Address_Update    ${sessiontoken}    王二    ${SPACE}    浙江省
    ...    杭州市    西湖区    双龙街199号    1
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    手机号码格式错误

收货地址新增-tc0002404-手机号为11位
    #id,name,phone,province,city,district,detail,tolerate
    #tolerate：0否，1是
    ${ret1}    Address_Update    ${sessiontoken}    王二    181434822011    浙江省
    ...    杭州市    西湖区    双龙街199号    1
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    手机号码格式错误

收货地址新增-tc0002405-手机号小于11位
    #id,name,phone,province,city,district,detail,tolerate
    #tolerate：0否，1是
    ${ret1}    Address_Update    ${sessiontoken}    王二    1814348220    浙江省
    ...    杭州市    西湖区    双龙街199号    1
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    手机号码格式错误

收货地址新增-tc0002406-收货地址省为空
    #id,name,phone,province,city,district,detail,tolerate
    #tolerate：0否，1是
    ${ret1}    Address_Update    ${sessiontoken}    王二    18143482201   ${SPACE}
    ...    杭州市    西湖区    双龙街199号    1
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    收货地址省为空

#收货地址新增-tc0002405
#    #id,name,phone,province,city,district,detail,tolerate
#    #tolerate：0否，1是
#    ${ret1}    Address_Update    ${sessiontoken}    王二    18143482201   浙江省   ${SPACE}
#    ...       西湖区    双龙街199号    1
#    ${ret2}    evaluate    $ret1['result']['message']
#    should contain    ${ret2}    收货地址市为空
#
#收货地址新增-tc0002406
#    #id,name,phone,province,city,district,detail,tolerate
#    #tolerate：0否，1是
#    ${ret1}    Address_Update    ${sessiontoken}    王二    18143482201   浙江省   杭州市   ${SPACE}
#    ...       双龙街199号    1
#    ${ret2}    evaluate    $ret1['result']['message']
#    should contain    ${ret2}    收货地址区为空

收货地址新增-tc0002407-收货详细地址为空
    #id,name,phone,province,city,district,detail,tolerate
    #tolerate：0否，1是
    ${ret1}    Address_Update    ${sessiontoken}    王二    18143482201   浙江省   杭州市   西湖区   ${SPACE}
    ...        1
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    收货详细地址为空

#收货地址新增-tc0002408-是否默认为空
#    #id,name,phone,province,city,district,detail,tolerate
#    #tolerate：0否，1是
#    ${ret1}    Address_Update    ${sessiontoken}    王二    18143482201   浙江省   杭州市   西湖区   双龙街199号   ${SPACE}
#    ${ret2}    evaluate    $ret1['result']['message']
#    should contain    ${ret2}    非法请求
