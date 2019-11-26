*** Settings ***
Test Timeout      2 minutes
Library           pylib.Account.Account
Library           ../pylib/DataItem/Bank_Card.py
Variables         cfg.py

Test Setup      sessiontoken

*** Keywords ***
sessiontoken

    ${result}     biz    ${mobile}   ${password}  LOGIN
    ${token}    evaluate    $result['data']['sessionToken']
    set suite variable     ${sessiontoken}       ${token}

*** Test Cases ***
用户银行卡列表接口-tc0003000-正常情况
    ${ret1}    bankcard_list     ${sessiontoken}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

绑卡——获取验证码-tc0003100-正常情况
    ${ret1}    Get_code     ${sessiontoken}    320621199008284125   吴慧婷   18143488220   6227001329010162407    中国建设银行     01050000    8
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

绑卡——获取验证码-tc0003101-身份证号为空
    ${ret1}    Get_code     ${sessiontoken}    ${SPACE}   吴慧婷   18143488220   6227001329010162407    中国建设银行     01050000    8
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    绑卡基本参数为空

绑卡——获取验证码-tc0003102-姓名为空
    ${ret1}    Get_code     ${sessiontoken}    320621199008284125   ${SPACE}   18143488220   6227001329010162407    中国建设银行     01050000    8
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    绑卡基本参数为空

绑卡——获取验证码-tc0003103-手机号为空
    ${ret1}    Get_code     ${sessiontoken}    320621199008284125   吴慧婷    ${SPACE}      6227001329010162407    中国建设银行     01050000    8
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    绑卡基本参数为空

绑卡——获取验证码-tc0003104-银行卡信息为空
    ${ret1}    Get_code     ${sessiontoken}    320621199008284125   吴慧婷    18143488220    ${SPACE}     中国建设银行     01050000    8
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    绑卡基本参数为空

绑卡——获取验证码-tc0003105-银行名称为空
    ${ret1}    Get_code     ${sessiontoken}    320621199008284125   吴慧婷    18143488220    6227001329010162407     ${SPACE}      01050000    8
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    绑卡基本参数为空

绑卡——获取验证码-tc0003106-银行编号为空
    ${ret1}    Get_code     ${sessiontoken}    320621199008284125   吴慧婷    18143488220    6227001329010162407     中国建设银行    ${SPACE}      8
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    绑卡基本参数为空

绑卡——获取验证码-tc0003107-发薪日为空
    ${ret1}    Get_code     ${sessiontoken}    320621199008284125   吴慧婷    18143488220    6227001329010162407     中国建设银行    01050000     ${SPACE}
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    绑卡基本参数为空

绑卡支持银行列表接口-tc0003200-正常情况
    ${ret1}    Bank_supported     ${sessiontoken}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

设置选择的银行卡为主卡-tc0003300-正常情况
#获取银行卡id
    ${ret1}    bankcard_list     ${sessiontoken}
    ${bank_id}   evaluate    $ret1['data']['bankCardList'][0]['id']
    ${id}     evaluate      str(${bank_id})
    ${ret1}    Bankcard_select     ${sessiontoken}     ${id}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    设置选中的银行卡成功
    should be true    $ret1['result']['success']==${true}

设置选择的银行卡为主卡-tc0003301-id为空
#获取银行卡id
    ${ret1}    Bankcard_select     ${sessiontoken}     ${SPACE}
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    请选择您要选中的银行卡