*** Settings ***
Test Timeout      2 minutes
Library           ../pylib/Project.py
Variables         ../cfg.py

*** Test Cases ***
借款人资金使用情况-tc006000-正常情况
#先获取项目id
    ${result}   product_list    1
    ${productId}   evaluate   $result['data']['list'][0]['id']
    ${ret}    fundUseInfo    ${productId}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

借款人资金使用情况-tc006001-productId为空
##先获取项目id
#    ${result}   product_list    1
#    ${productId}   evaluate   $result['data']['list'][0]['id']
    ${ret}    fundUseInfo    ${None}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    	productId不能为空
    should contain   ${ret2}    500

是否可以购买标的-tc006100-正常情况
    ${ret}   isbuy
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

借款人信息-tc006200-正常情况
    ${ret}   loan_info    ${productId}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

借款人信息-tc006201-productId为空
    ${ret}   loan_info    ${productId}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

项目列表-可调-tc006300-正常情况
    ${ret}   product_list    1
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

项目基本信息-可调-tc006400-正常情况
#先获取项目id
    ${result}   product_list    1
    ${productId}   evaluate   $result['data']['list'][0]['id']
    ${ret}    product_detail    ${productId}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

项目基本信息-可调-tc006401-productId为空
##先获取项目id
#    ${result}   product_list    1
#    ${productId}   evaluate   $result['data']['list'][0]['id']
    ${ret}    product_detail    ${None}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    	productId不能为空
    should contain   ${ret2}    500

确认出借-可调-tc006500-正常情况
#先获取项目id
    ${result}   product_list    1
    ${productId}   evaluate   $result['data']['list'][0]['id']
    ${ret}    product_detail    ${productId}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

确认出借-可调-tc006501-productId为空
##先获取项目id
#    ${result}   product_list    1
#    ${productId}   evaluate   $result['data']['list'][0]['id']
    ${ret}    product_detail    ${None}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    	productId不能为空
    should contain   ${ret2}    500

项目出借记录-可调-tc006600-正常情况
#先获取项目id
    ${result}   product_list    1
    ${productId}   evaluate   $result['data']['list'][0]['id']
    ${ret}    product_lendRecord    ${productId}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

项目出借记录-可调-tc006601-productId为空
#先获取项目id
    ${result}   product_list    1
    ${productId}   evaluate   $result['data']['list'][0]['id']
    ${ret}    product_lendRecord    ${None}
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    	productId不能为空
    should contain   ${ret2}    500

借款人图片-tc006700-正常情况
#先获取项目id
    ${result}   product_list    1
    ${productId}   evaluate   $result['data']['list'][0]['id']
    ${ret}    logout    ${productId}    2
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200

借款人图片-tc006701-productId为空
##先获取项目id
#    ${result}   product_list    1
#    ${productId}   evaluate   $result['data']['list'][0]['id']
    ${ret}    logout    ${None}    2
    ${ret1}    evaluate   $ret['result']['message']
    ${ret2}    evaluate   $ret['result']['code']
    should be equal   ${ret1}    成功
    should contain   ${ret2}    200