*** Settings ***
Test Timeout      2 minutes
Library           pylib.Account.Account
Library           ../pylib/DataItem/Contact.py
Variables         cfg.py

Test Setup      sessiontoken

*** Keywords ***
sessiontoken

    ${result}     biz    ${mobile}   ${password}  LOGIN
    ${token}    evaluate    $result['data']['sessionToken']
    set suite variable     ${sessiontoken}       ${token}

*** Test Cases ***
联系人查询接口-tc0003400-正常情况
    ${ret1}    Contact_query     ${sessiontoken}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

#提交联系人接口-tc0003500
##查询contacts
#    ${ret}    Contact_query     ${sessiontoken}
#    ${contacts}     evaluate    $ret['data']['contacts']
#    ${ret1}    Contact_save     ${sessiontoken}       ${contacts}    ${mailList}
#    ${ret2}    evaluate    $ret1['result']['message']
#    should be equal    ${ret2}    请求成功
#    should be true    $ret1['result']['success']==${true}