# _*_ coding:utf-8 _*_
import sys

from Task import TK_papaandroid, TK_TerminalHandle
from common import dataprovide, main_package,stringHelper
from element_locator import papaandroid
import imp
from common import script_ultils
sys.path.append("..")
import unittest
from time import sleep
from Task import TK_TerminalHandle
from common import sql_normal_csmall,sql_normal_csorder

class Case(TK_papaandroid.Task, TK_TerminalHandle.TerminalHandle, unittest.TestCase):
    #新用户估值额度高于商品价格进行 信用支付购买商品流程
    def test_buy_above1(self):
        """“新用户估值额度高于商品价格进行信用支付购买商品流程，购买到待发货"""''
        self.pop_close()
        # self.login('vip')
        # 在商品详情页面点击确认转卖
        self.click_button(papaandroid.b_good)
        self.click_button(papaandroid.b_hotProduct)
        # 信用支付购买
        self.click_button(papaandroid.b_buy)
        self.click_button(papaandroid.b_CreditPayment)
        self.click_button(papaandroid.b_ConfirmPurchase)
        #选择分期
        self.click_button(papaandroid.b_seven)
        self.back()
        self.back()
        self.back()


    def test_buy_above2(self):
        """“订单为待发货状态，且卡内余额等于还款金额，进行还款操作"""''
        self.click_button(papaandroid.b_My)
        self.click_button(papaandroid.b_order_center)
        order_state = self.driver.find_element_by_xpath(papaandroid.thirdorder_state[1]).text
        self.assertEqual(order_state, '待发货')
        print("商品为待发货状态正确")
        myms = sql_normal_csmall.mysql_connect(sql_normal_csmall.db_info)
        myms_csorder = sql_normal_csorder.mysql_connect(sql_normal_csorder.db_info)
        myms_csorder.sql_assign_exec(
            " update cso_repayment_plan set repayment_status=3 where contract_id='CO20180803003959191'")
        myms_csorder.sql_assign_exec(
            "update cso_contract_msg set contract_Status=221 where id='CO20180803003959191' ")
        myms.sql_assign_exec(
            "update csm_order set status=4,contract_status=221 where contract_no ='CO20180803003959191'")
        self.back()
        self.back()
        self.back()
        self.click_button(papaandroid.b_order_center)
        sleep(3)
        order_state = self.driver.find_element_by_xpath(papaandroid.thirdorder_state[1]).text
        self.assertEqual(order_state, '交易完成')
        self.click_button(papaandroid.thirdorder_state)
        self.assertTrue(self.isElement(papaandroid.tx_assertSettlement))
        print("已结清，还款成功状态正确")
        myms_csorder.sql_assign_exec(
            " update cso_repayment_plan set repayment_status=1 where contract_id='CO20180803003959191'")
        myms_csorder.sql_assign_exec(
            "update cso_contract_msg set contract_Status=212 where id='CO20180803003959191' ")
        myms.sql_assign_exec(
            "update csm_order set status=2,contract_status=212 where contract_no ='CO20180803003959191'")
        self.back()
        self.back()


    def test_buy_above3(self):
        """“订单为已发货状态，且卡内余额等于还款金额，进行还款操作"""''
        # 修改待发货到已发货
        # self.click_button(papaandroid.b_My)
        self.click_button(papaandroid.b_order_center)
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
        self.back()
        self.back()
        self.click_button(papaandroid.b_order_center)
        order_state = self.driver.find_element_by_xpath(papaandroid.thirdorder_state[1]).text
        self.assertEqual(order_state, '交易完成')
        self.click_button(papaandroid.thirdorder_state)
        self.assertTrue(self.isElement(papaandroid.tx_assertSettlement))
        print("已结清，还款成功状态正确")
        myms_csorder.sql_assign_exec(
            " update cso_repayment_plan set repayment_status=1 where contract_id='CO20180803003959191'")
        myms_csorder.sql_assign_exec(
            "update cso_contract_msg set contract_Status=212 where id='CO20180803003959191' ")
        myms.sql_assign_exec(
            "update csm_order set status=2,contract_status=212 where contract_no ='CO20180803003959191'")
        self.back()
        self.back()


    def test_buy_above4(self):
        """“订单为已完成状态，且卡内余额等于还款金额，进行还款操作"""''
        # 修改待发货到交易完成
        # self.pop_close()
        # self.click_button(papaandroid.b_My)
        self.click_button(papaandroid.b_order_center)
        myms = sql_normal_csmall.mysql_connect(sql_normal_csmall.db_info)
        myms.sql_assign_exec(
            "update csm_order set status='3' where user_id='2018072411392004050001343390' and id='660' ")
        myms.sql_assign_exec(
            "update csm_order set status='4' where user_id='2018072411392004050001343390' and id='660' ")
        sleep(5)
        order_state = self.driver.find_element_by_xpath(papaandroid.thirdorder_state[1]).text
        self.assertEqual(order_state, '交易完成')
        print("商品为交易完成状态正确")
        myms_csorder = sql_normal_csorder.mysql_connect(sql_normal_csorder.db_info)
        myms_csorder.sql_assign_exec(
            " update cso_repayment_plan set repayment_status=3 where contract_id='CO20180803003959191'")
        myms_csorder.sql_assign_exec(
            "update cso_contract_msg set contract_Status=221 where id='CO20180803003959191' ")
        myms.sql_assign_exec(
            "update csm_order set status=4,contract_status=221 where contract_no ='CO20180803003959191'")
        self.back()
        self.click_button(papaandroid.b_order_center)
        order_state = self.driver.find_element_by_xpath(papaandroid.thirdorder_state[1]).text
        self.assertEqual(order_state, '交易完成')
        self.click_button(papaandroid.thirdorder_state)
        self.assertTrue(self.isElement(papaandroid.tx_assertSettlement))
        print("已结清，还款成功状态正确")





if __name__ == '__main__':
    # main_package.main_package(Case("test_buy_above1"),"/Users/xygjzgs/selenium/")
    # main_package.main_package(Case("test_buy_above2"), "/Users/xygjzgs/selenium/")
    # main_package.main_package(Case("test_buy_above3"), "/Users/xygjzgs/selenium/")
    main_package.main_package(Case("test_buy_above4"), "/Users/xygjzgs/selenium/")

