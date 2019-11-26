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
    #新用户估值额度高于商品价格进行信用支付转卖商品流程
    def test_saling_above1(self):
        """“单期转卖成功，还款，银行卡余额等于还款金额"""''
        self.pop_close()
        self.click_button(papaandroid.b_good)
        self.click_button(papaandroid.b_hotProduct)
        self.click_button(papaandroid.b_resell)
        self.click_button(papaandroid.b_seven)
        self.back()
        self.back()
        self.click_button(papaandroid.b_My)
        self.click_button(papaandroid.b_order_center)
        myms = sql_normal_csmall.mysql_connect(sql_normal_csmall.db_info)
        myms_csorder = sql_normal_csorder.mysql_connect(sql_normal_csorder.db_info)
        myms_csorder.sql_assign_exec(
            " update cso_repayment_plan set repayment_status=3 where contract_id='CO20180803004175620'")
        myms_csorder.sql_assign_exec(
            "update cso_contract_msg set contract_Status=221 where id='CO20180803004175620' ")
        myms.sql_assign_exec(
            "update csm_order set status=4,contract_status=221 where contract_no ='CO20180803004175620'")
        self.back()
        self.back()
        self.click_button(papaandroid.b_order_center)
        order_state = self.driver.find_element_by_xpath(papaandroid.secondorder_state[1]).text
        self.assertEqual(order_state, '已结清')
        print("已结清，还款成功状态正确")
        myms_csorder.sql_assign_exec(
            " update cso_repayment_plan set repayment_status=1 where contract_id='CO20180803004175620'")
        myms_csorder.sql_assign_exec(
            "update cso_contract_msg set contract_Status=212 where id='CO20180803004175620' ")
        myms.sql_assign_exec(
            "update csm_order set status=1,contract_status=212 where contract_no ='CO20180803004175620'")
        self.back()
        self.back()

    def test_saling_above2(self):
        """“转卖选择多期，提前结清，点击查看还款计划"""''
        self.click_button(papaandroid.b_order_center)
        myms = sql_normal_csmall.mysql_connect(sql_normal_csmall.db_info)
        myms_csorder = sql_normal_csorder.mysql_connect(sql_normal_csorder.db_info)
        myms_csorder.sql_assign_exec(
            " update cso_repayment_plan set repayment_status=3 where contract_id='CO20180803004188670'")
        myms_csorder.sql_assign_exec(
            "update cso_contract_msg set contract_Status=221 where id='CO20180803004188670' ")
        myms.sql_assign_exec(
            "update csm_order set status=4,contract_status=221 where contract_no ='CO20180803004188670'")
        self.back()
        self.back()
        self.click_button(papaandroid.b_order_center)
        order_state = self.driver.find_element_by_xpath(papaandroid.tx_firstorder_state[1]).text
        self.assertEqual(order_state, '已结清')
        print("已结清，还款成功状态正确")
        myms_csorder.sql_assign_exec(
            " update cso_repayment_plan set repayment_status=1 where contract_id='CO20180803004188670'")
        myms_csorder.sql_assign_exec(
            "update cso_contract_msg set contract_Status=212 where id='CO20180803004188670' ")
        myms.sql_assign_exec(
            "update csm_order set status=1,contract_status=212 where contract_no ='CO20180803004188670'")
        self.back()
        self.back()


    def test_saling_above3(self):
        """“多期转卖成功，已存在逾期，点击查看还款计划"""''
        self.click_button(papaandroid.b_order_center)
        myms = sql_normal_csmall.mysql_connect(sql_normal_csmall.db_info)
        myms_csorder = sql_normal_csorder.mysql_connect(sql_normal_csorder.db_info)
        myms_csorder.sql_assign_exec(
            " update cso_repayment_plan set repayment_status=4 where contract_id='CO20180803004188670'")
        myms_csorder.sql_assign_exec(
            "update cso_contract_msg set contract_Status=230 where id='CO20180803004188670' ")
        myms.sql_assign_exec(
            "update csm_order set contract_status=230 where contract_no ='CO20180803004188670'")
        self.back()
        self.back()
        self.click_button(papaandroid.b_order_center)
        order_state = self.driver.find_element_by_xpath(papaandroid.tx_firstorder_state[1]).text
        self.assertEqual(order_state, '已逾期')
        print("已逾期状态正确")
        myms_csorder.sql_assign_exec(
            " update cso_repayment_plan set repayment_status=1 where contract_id='CO20180803004188670'")
        myms_csorder.sql_assign_exec(
            "update cso_contract_msg set contract_Status=212 where id='CO20180803004188670' ")
        myms.sql_assign_exec(
            "update csm_order set status=1,contract_status=212 where contract_no ='CO20180803004188670'")
        #
        myms.sql_assign_exec(
            "update csm_order set status='2' where user_id='2018072411392004050001343390' and id='559'")
        #
        myms_csorder.sql_assign_exec(
            " update cso_repayment_plan set repayment_status=1 where contract_id='CO20180803003959191'")
        myms_csorder.sql_assign_exec(
            "update cso_contract_msg set contract_Status=212 where id='CO20180803003959191' ")
        myms.sql_assign_exec(
            "update csm_order set status=2,contract_status=212 where contract_no ='CO20180803003959191'")
        myms.conn_close()
        myms.cur_close()


if __name__ == '__main__':
    # main_package.main_package(Case("test_saling_above1"),"/Users/xygjzgs/selenium/")
    # main_package.main_package(Case("test_saling_above2"), "/Users/xygjzgs/selenium/")
    # main_package.main_package(Case("test_saling_above3"), "/Users/xygjzgs/selenium/")
    main_package.main_package(Case("test_saling_above4"), "/Users/xygjzgs/selenium/")
