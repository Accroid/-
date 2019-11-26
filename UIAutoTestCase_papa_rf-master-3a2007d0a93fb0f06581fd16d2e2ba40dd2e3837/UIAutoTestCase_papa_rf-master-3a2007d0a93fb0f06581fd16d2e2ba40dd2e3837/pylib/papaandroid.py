# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

b_Pop=(By.ID,"com.xncredit.dxb:id/iv_show_ad_img")

b_Pop_close=(By.XPATH,"//android.widget.LinearLayout[@index=1]/android.widget.ImageView[@index=0]")


# 啪啪钱包
tx_papa=(By.XPATH,"//android.widget.TextView[contains(@text,'啪啪')]")
# 首页按钮
b_Havegood=(By.XPATH,"//android.widget.TextView[contains(@text,'首页')]")
# 商品按钮
b_good=(By.XPATH,"//android.widget.TextView[contains(@text,'商品')]")
# 我的模块按钮
b_My=(By.XPATH,"//android.widget.TextView[contains(@text,'我的')]")

# 立即评估按钮
b_go_value=(By.ID,"com.xncredit.dxb:id/tv_go_value")
# 去实名按钮
b_Realname=(By.ID,"com.xncredit.dxb:id/tv_ok")
# 校验去实名
tx_assertRealname=(By.XPATH,"//android.widget.TextView[contains(@text,'实名认证')]")
# 认证中心按钮
b_Certification_center=(By.ID,"com.xncredit.dxb:id/tv_Certification_center")
# 我的银行卡按钮
b_my_bankcard=(By.ID,"com.xncredit.dxb:id/tv_my_bankcard")
# 订单中心按钮
b_order_center=(By.ID,"com.xncredit.dxb:id/layout_order_center")
# 收货地址按钮
b_goods_address=(By.ID,"com.xncredit.dxb:id/tv_goods_address")
# 信用回收按钮
b_credit_recycling=(By.ID,"com.xncredit.dxb:id/tv_credit_recycling")
b_credit_recycling2=(By.ID,"com.xncredit.dxb:id/btn_sumbit")
# 校验信用回收跳转
tx_credit_recycling=(By.XPATH,"//android.widget.TextView[contains(@text,'信用回收')]")
# 帮助中心按钮
b_help=(By.ID,"com.xncredit.dxb:id/tv_help")

#在线客服
b_Onlinecustomer=(By.XPATH,"//p[text()='在线客服']")
#校验在线客服
tx_assertOnlinecustomer=(By.XPATH,"//android.widget.TextView[contains(@text,'信用管家')]")
#拿钱无忧
b_Witheasymoney=(By.XPATH,"//p[text()='拿钱无忧']")
#校验拿钱无忧
tx_assertWitheasymoney=(By.XPATH,"//android.widget.TextView[contains(@text,'微信公众号')]")
#电话咨询
b_Telephone=(By.XPATH,"//p[text()='电话咨询']")
#校验电话咨询
tx_assertb_Telephone=(By.ID,"com.samsung.android.contacts:id/digits")

# 校验帮助中心跳转
tx_assertHelp=(By.XPATH,"//android.widget.TextView[contains(@text,'常见问题')]")
# 关于我们按钮
b_about=(By.ID,"com.xncredit.dxb:id/tv_about")
# 校验关于我们跳转
tx_assertAbout=(By.XPATH,"//android.widget.TextView[contains(@text,'关于我们')]")

# 首页tab
tab_firstpage=(By.XPATH,"//android.support.v4.view.ViewPager/android.widget.ImageView")
# 校验首页tab跳转
tx_assertFirstpage=(By.ID,"com.xncredit.dxb:id/center")
# 关闭
b_close=(By.XPATH,"//android.widget.LinearLayout[@index=0]/android.widget.RelativeLayout[@index=0]/android.widget.LinearLayout[@index=0]/android.widget.ImageView[@index=0]")

#热卖商品
b_hotProduct=(By.XPATH,"//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[@index=0]")
# 标配
tx_sku1=(By.ID,"com.xncredit.dxb:id/rl_skus_1")
# 标配+官方联保
tx_sku2=(By.ID,"com.xncredit.dxb:id/tv_skus_2")
# 咨询客服
tx_kefus=(By.ID,"com.xncredit.dxb:id/tv_kefu")
# 转卖换钱
b_resell=(By.ID,"com.xncredit.dxb:id/tv_resell")
# 立即购买
b_buy=(By.ID,"com.xncredit.dxb:id/tv_go_guy")

# 您还未登录，取消
b_cancel=(By.ID,"com.xncredit.dxb:id/cancel")
# 您还未登录，去登录
b_tologin=(By.ID,"com.xncredit.dxb:id/submit")
# 价格按钮
b_price=(By.ID,"com.xncredit.dxb:id/right")
# 第一个商品的价格
tx_firstprice=(By.XPATH,"//android.support.v7.widget.RecyclerView[@index=0]/android.widget.LinearLayout[@index=0]/android.widget.TextView[@index=2]")
# 第三个商品的价格
tx_secondprice=(By.XPATH,"//android.support.v7.widget.RecyclerView[@index=0]/android.widget.LinearLayout[@index=2]/android.widget.TextView[@index=2]")


#输入手机号
edit_iphone=(By.ID,"com.xncredit.dxb:id/login_cet_phone")
# 下一步
b_next=(By.ID,"com.xncredit.dxb:id/tv_click")
# 输入密码
edit_pwd=(By.ID,"com.xncredit.dxb:id/login_cet_pwd")
# 输入密码
edit_pwd2=(By.ID,"com.xncredit.dxb:id/register_cet_pwd")
# 图形验证码
edit_picverification=(By.ID,"com.xncredit.dxb:id/register_cet_img_code")
# 请输入验证码
edit_verification=(By.ID,"com.xncredit.dxb:id/register_cet_code")
# 登录
b_login=(By.XPATH,"//android.widget.TextView[contains(@text,'登录')]")
# 注册
b_login2=(By.ID,"com.xncredit.dxb:id/tv_click")
# 忘记密码
b_forgetpwd=(By.ID,"com.xncredit.dxb:id/login_tv_forget")
# 登录-完成
b_loginsure=(By.ID,"com.xncredit.dxb:id/tv_click")
#校验点击忘记密码
tx_assertforgetpwd=(By.ID,"com.xncredit.dxb:id/register_cet_pwd")
# 找回密码-输入新密码
edit_register_cet_pwd=(By.ID,"com.xncredit.dxb:id/register_cet_pwd")
# 找回密码-输入图形验证码
edit_register_cet_img_code=(By.ID,"com.xncredit.dxb:id/register_cet_img_code")
# 找回密码-验证码
edit_register_cet__code=(By.ID,"com.xncredit.dxb:id/register_cet__code")
edit_register_cet__code2=(By.ID,"com.xncredit.dxb:id/register_cet_code")
# 找回密码-完成
b_finish=(By.ID,"com.xncredit.dxb:id/tv_click")


#转卖换钱-我知道了
b_know=(By.ID,"com.xncredit.dxb:id/tv_know")
# 转卖换钱-仍然转卖
b_resellrenran=(By.ID,"com.xncredit.dxb:id/tv_resell")

# 订单详情
tx_orderDetails=(By.XPATH,"//android.widget.TextView[contains(@text,'订单详情')]")


# 商品转卖
#七天
b_seven=(By.XPATH,"//android.widget.TextView[contains(@text,'7天')]")
# 14天
b_fourteen=(By.XPATH,"//android.widget.TextView[contains(@text,'14天')]")
#1期
b_Phase1=(By.XPATH,"//android.widget.TextView[contains(@text,'1期')]")
#2期
b_Phase2=(By.XPATH,"//android.widget.TextView[contains(@text,'2期')]")
#3期
b_Phase3=(By.XPATH,"//android.widget.TextView[contains(@text,'3期')]")
# 确认转卖
b_Confirmtoresell=(By.XPATH,"//android.widget.TextView[contains(@text,'确认转卖')]")

# 商品购买
# 现金支付
b_CashPayments=(By.XPATH,"//android.widget.TextView[contains(@text,'现金支付')]")
# 选择银行卡1
b_SelectBank1=(By.XPATH,"//android.widget.TextView[contains(@text,'选择银行卡')]")
# 选择银行卡2
b_SelectBank2=(By.ID,"com.xncredit.dxb:id/tv_bank_name")
# 信用支付
b_CreditPayment=(By.XPATH,"//android.widget.TextView[contains(@text,'信用支付')]")
# 确认购买
b_ConfirmPurchase=(By.ID,"com.xncredit.dxb:id/tv_sumbit")
#确认支付
b_pay=(By.ID,"com.xncredit.dxb:id/tv_sumbit")
# 签署合同页面
tx_assertPay=(By.XPATH,"//android.widget.TextView[contains(@text,'签署合同')]")


# 订单中心订单状态
tx_state=(By.XPATH,"//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[@index=0]/android.widget.LinearLayout[@index=0]/android.widget.LinearLayout[@index=0]/android.widget.TextView[@index=1]")


# 新建地址
b_create_address=(By.XPATH,"//android.widget.TextView[contains(@text,'+ 新建地址')]")
# 收货人姓名
edit_consigneename=(By.ID,"com.xncredit.dxb:id/et_name")
# 收货人手机号
edit_consigneiphone=(By.ID,"com.xncredit.dxb:id/et_phone")
# 所在地区
edit_location=(By.ID,"com.xncredit.dxb:id/tv_area")
# 省
b_provice=(By.XPATH,"//android.widget.TextView[contains(@text,'北京')]")
# 城
b_city=(By.XPATH,"//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[@index=0]/android.widget.TextView[@index=0]")
# 区
b_district=(By.XPATH,"//android.widget.TextView[contains(@text,'东城')]")
# 确定
b_sure=(By.XPATH,"//android.widget.TextView[contains(@text,'确定')]")
# 街道门派
edit_detail=(By.ID,"com.xncredit.dxb:id/et_detail")
# 提交
b_submit=(By.ID,"com.xncredit.dxb:id/tv_commit")
# 删除地址
b_delete_address=(By.ID,"com.xncredit.dxb:id/tv_commit")
# 校验收货人姓名
tx_assertName=(By.ID,"com.xncredit.dxb:id/tv_name")

# 添加银行卡
b_add_bank=(By.XPATH,"//android.widget.TextView[contains(@text,'+ 添加银行卡')]")
#银行名称

# 填写银行卡号
edit_bank_number=(By.ID,"com.xncredit.dxb:id/et_bank_number")
# 发薪日
b_pay_day=(By.ID,"com.xncredit.dxb:id/tv_pay_day_prompt")
#
b_day=(By.XPATH,"//android.widget.TextView[contains(@text,'1')]")
# 确认
b_ok=(By.ID,"com.xncredit.dxb:id/tv_ok")
# 手机号
edit_bank_phone=(By.ID,"com.xncredit.dxb:id/et_bank_phone")

# 订单中心-第已个订单订单状态
tx_firstorder_state=(By.XPATH,"//android.support.v7.widget.RecyclerView[@index=0]/android.widget.LinearLayout[@index=0]/android.widget.LinearLayout[@index=0]/android.widget.LinearLayout[@index=0]/android.widget.TextView[@index=1]")
# 订单中心-第二个订单订单状态
secondorder_state=(By.XPATH,"//android.support.v7.widget.RecyclerView[@index=0]/android.widget.LinearLayout[@index=1]/android.widget.LinearLayout[@index=0]/android.widget.LinearLayout[@index=0]/android.widget.TextView[@index=1]")
# 订单中心-第三个订单订单状态
thirdorder_state=(By.XPATH,"//android.support.v7.widget.RecyclerView[@index=0]/android.widget.LinearLayout[@index=2]/android.widget.LinearLayout[@index=0]/android.widget.LinearLayout[@index=0]/android.widget.TextView[@index=1]")
# 订单中心-第四个订单订单状态
fourthorder_state=(By.XPATH,"//android.support.v7.widget.RecyclerView[@index=0]/android.widget.LinearLayout[@index=3]/android.widget.LinearLayout[@index=0]/android.widget.LinearLayout[@index=0]/android.widget.TextView[@index=1]")

# 商品页  多期的商品
b_multiphase_product=(By.XPATH,"//android.support.v7.widget.RecyclerView[@index=0]/android.widget.LinearLayout[@index=1]/android.widget.LinearLayout[@index=0]")


# 已结清
tx_assertSettlement=(By.XPATH,"//android.widget.TextView[contains(@text,'已结清')]")

# 退出登录
b_login_out=(By.ID,"com.xncredit.dxb:id/tv_login_out")
#退出登录-确定
b_login_out_sure=(By.ID,"com.xncredit.dxb:id/submit")