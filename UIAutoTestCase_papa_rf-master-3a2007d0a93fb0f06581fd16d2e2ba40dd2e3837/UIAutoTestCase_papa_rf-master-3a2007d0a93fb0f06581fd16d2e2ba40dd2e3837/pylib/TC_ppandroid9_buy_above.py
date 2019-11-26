# _*_ coding:utf-8 _*_
import sys

import TerminalHandle_TK
import dataprovide,stringHelper,papaandroid,sql_normal_csmall,sql_normal_csorder

sys.path.append("..")
import unittest
from time import sleep
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class TC_ppandroid9_buy_above:
    sc = TerminalHandle_TK.TerminalHandle_TK()
    #新用户估值额度高于商品价格进行 信用支付购买商品流程
    def test_buy_above1(self):
        """“新用户估值额度高于商品价格进行信用支付购买商品流程，购买到待发货"""''
        self.sc.initialization()
        self.sc.pop_close()
        # self.login('vip')
        # 在商品详情页面点击确认转卖
        self.sc.click_button(papaandroid.b_good)
        self.sc.click_button(papaandroid.b_hotProduct)
        # 信用支付购买
        self.sc.click_button(papaandroid.b_buy)
        self.sc.click_button(papaandroid.b_CreditPayment)
        self.sc.click_button(papaandroid.b_ConfirmPurchase)
        #选择分期
        self.sc.click_button(papaandroid.b_seven)
        self.sc.back()
        self.sc.back()
        self.sc.back()


    def test_buy_above2(self):
        """“订单为待发货状态，且卡内余额等于还款金额，进行还款操作"""''
        self.sc.click_button(papaandroid.b_My)
        self.sc.click_button(papaandroid.b_order_center)
        sleep(5)
        order_state = self.sc.driver.find_element_by_xpath(papaandroid.thirdorder_state[1]).text
        result1=order_state
        result2='待发货'
        myms = sql_normal_csmall.mysql_connect(sql_normal_csmall.db_info)
        myms_csorder = sql_normal_csorder.mysql_connect(sql_normal_csorder.db_info)
        myms_csorder.sql_assign_exec(
            " update cso_repayment_plan set repayment_status=3 where contract_id='CO20180803003959191'")
        myms_csorder.sql_assign_exec(
            "update cso_contract_msg set contract_Status=221 where id='CO20180803003959191' ")
        myms.sql_assign_exec(
            "update csm_order set status=4,contract_status=221 where contract_no ='CO20180803003959191'")
        self.sc.back()
        self.sc.back()
        self.sc.back()
        self.sc.click_button(papaandroid.b_order_center)
        sleep(3)
        order_state2= self.sc.driver.find_element_by_xpath(papaandroid.thirdorder_state[1]).text
        result3 = order_state2
        result4 = '交易完成'
        myms_csorder.sql_assign_exec(
            " update cso_repayment_plan set repayment_status=1 where contract_id='CO20180803003959191'")
        myms_csorder.sql_assign_exec(
            "update cso_contract_msg set contract_Status=212 where id='CO20180803003959191' ")
        myms.sql_assign_exec(
            "update csm_order set status=2,contract_status=212 where contract_no ='CO20180803003959191'")
        self.sc.back()
        self.sc.back()
        return result1,result2,result3,result4


    def test_buy_above3(self):
        """“订单为已发货状态，且卡内余额等于还款金额，进行还款操作"""''
        # 修改待发货到已发货
        # self.click_button(papaandroid.b_My)
        self.sc.click_button(papaandroid.b_order_center)
        myms = sql_normal_csmall.mysql_connect(sql_normal_csmall.db_info)
        myms.sql_assign_exec(
            "update csm_order set status='3' where user_id='2018072411392004050001343390' and id='660' ")
        myms_csorder = sql_normal_csorder.mysql_connect(sql_normal_csorder.db_info)
        myms_csorder.sql_assign_exec(
            " update cso_repayment_plan set repayment_status=3 where contract_id='CO20180803003959191'")
        myms_csorder.sql_assign_exec(
            "update cso_contract_msg set contract_Status=221 where id='CO20180803003959191' ")
        myms.sql_assign_exec(
            "update csm_order set status=4,contract_status=221 where contract_no ='CO20180803003959191'")
        self.sc.back()
        self.sc.back()
        self.sc.click_button(papaandroid.b_order_center)
        sleep(6)
        order_state = self.sc.driver.find_element_by_xpath(papaandroid.thirdorder_state[1]).text
        # self.assertEqual(order_state, '交易完成')
        result1 = order_state
        result2 = '交易完成'
        self.sc.click_button(papaandroid.thirdorder_state)
        result3=self.sc.isElement(papaandroid.tx_assertSettlement)
        myms_csorder.sql_assign_exec(
            " update cso_repayment_plan set repayment_status=1 where contract_id='CO20180803003959191'")
        myms_csorder.sql_assign_exec(
            "update cso_contract_msg set contract_Status=212 where id='CO20180803003959191' ")
        myms.sql_assign_exec(
            "update csm_order set status=2,contract_status=212 where contract_no ='CO20180803003959191'")
        self.sc.back()
        self.sc.back()
        self.sc.back()
        return result1,result2,result3


    def quit(self):
        self.sc.driver.close_app()
        self.sc.driver.quit()




