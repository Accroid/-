*** Settings ***
Test Timeout      2 minutes
Library           pylib.Account.Account
Library           pylib.Default.Default
Variables         cfg.py

Test Setup      sessiontoken

*** Keywords ***
sessiontoken

    ${result}     biz    ${mobile}   ${password}  LOGIN
    ${token}    evaluate    $result['data']['sessionToken']
    set suite variable     ${sessiontoken}       ${token}

*** Test Cases ***
热门商品接口-tc0000500-已登录
    ${ret1}    hot_goods     ${sessiontoken}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

热门商品接口-tc0000501-未登录
    ${ret1}    hot_goods     ${SPACE}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

商品列表接口-tc0000600-已登录
#价格排序：null或0=升序 1=降序
    ${ret1}    goods_list     ${SPACE}   ${pageIndex}    ${pageSize}    ${sessiontoken}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

商品列表接口-tc0000601-未登录
#价格排序：null或0=升序 1=降序
    ${ret1}    goods_list     ${SPACE}   ${pageIndex}    ${pageSize}    ${SPACE}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

订单详情接口-tc0000700-正常情况
#此id为526
#查看订单列表，通过订单列表取出订单id
    ${ret}    order_list     ${sessiontoken}   ${pageIndex}  ${pageSize}
    ${getid}   evaluate      $ret['data']['page']['resultObj'][0]
    ${int_id}     evaluate    $getid['id']
    ${id}    evaluate     str(${int_id})
    ${ret1}    order_detail     ${sessiontoken}   ${id}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

订单详情接口-tc0000701-未登录
#此id为526
#查看订单列表，通过订单列表取出订单id
    ${ret}    order_list     ${sessiontoken}   ${pageIndex}  ${pageSize}
    ${getid}   evaluate      $ret['data']['page']['resultObj'][0]
    ${int_id}     evaluate    $getid['id']
    ${id}    evaluate     str(${int_id})
    ${ret1}    order_detail     ${SPACE}   ${id}
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    当前登录失效，请重新登录

订单详情接口-tc0000702-订单Id为空
#此id为526
#查看订单列表，通过订单列表取出订单id
    ${ret1}    order_detail     ${sessiontoken}   ${SPACE}
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    订单id为空

商品详情接口-tc0000800-正常情况
#此id为526
    ${ret1}    goods_list     ${SPACE}   ${pageIndex}    ${pageSize}    ${sessiontoken}
    ${getid}   evaluate     $ret1['data']['page']['resultObj'][0]['id']
    ${id}    evaluate     str(${getid})
    ${ret1}    goods_detail     ${sessiontoken}   ${id}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

商品详情接口-tc0000801-未登录
#此id为526
    ${ret1}    goods_list     ${SPACE}   ${pageIndex}    ${pageSize}    ${sessiontoken}
    ${getid}   evaluate     $ret1['data']['page']['resultObj'][0]['id']
    ${id}    evaluate     str(${getid})
    ${ret1}    goods_detail     ${SPACE}   ${id}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

订单列表接口-tc0000900-正常情况
    ${ret1}    order_list     ${sessiontoken}   ${pageIndex}  ${pageSize}
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}

订单列表接口-tc0000901-未登录
    ${ret1}    order_list     ${SPACE}   ${pageIndex}  ${pageSize}
    ${ret2}    evaluate    $ret1['result']['message']
    should contain    ${ret2}    当前登录失效，请重新登录

广告链接接口-tc0000910-正常情况
    ${ret1}    advert_info
    ${ret2}    evaluate    $ret1['result']['message']
    should be equal    ${ret2}    请求成功
    should be true    $ret1['result']['success']==${true}