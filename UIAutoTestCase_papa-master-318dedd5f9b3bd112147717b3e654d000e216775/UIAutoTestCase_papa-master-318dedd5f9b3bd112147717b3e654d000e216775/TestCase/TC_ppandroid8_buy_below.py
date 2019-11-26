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
from common import sql_normal_csmall

class Case(TK_papaandroid.Task, TK_TerminalHandle.TerminalHandle, unittest.TestCase):
    #新用户额度低于商品价格，进行购买商品流程
    def test_buy_below1(self):
        """“商品详情页面点击立即购买，修改处理订单状态  待发货状态-已发货-已完成"""''
        self.pop_close()
        # self.login('new')
        self.click_button(papaandroid.b_good)
        self.click_button(papaandroid.b_hotProduct)
        #点击购买
        self.click_button(papaandroid.b_buy)
        self.click_button(papaandroid.b_CashPayments)
        self.click_button(papaandroid.b_SelectBank1)
        self.click_button(papaandroid.b_SelectBank2)
        # self.click_button(papaandroid.b_ConfirmPurchase)
        # self.assertTrue(self.isElement(papaandroid.b_add_bank))
        # print("进入选择银行卡界面")
        # sleep(5)
        # self.back()
        self.back()
        self.back()
        self.back()
        self.click_button(papaandroid.b_My)
        self.click_button(papaandroid.b_order_center)
        #修改订单状态
        order_state=self.driver.find_element_by_xpath(papaandroid.fourthorder_state[1]).text
        self.assertEqual(order_state,'待发货')
        print("商品为待发货状态正确")
        self.back()
        self.back()
        #修改待发货到已发货
        myms = sql_normal_csmall.mysql_connect(sql_normal_csmall.db_info)
        myms.sql_assign_exec("update csm_order set status='3' where user_id='2018072411392004050001343390' and id='559' ")
        self.click_button(papaandroid.b_order_center)
        order_state = self.driver.find_element_by_xpath(papaandroid.fourthorder_state[1]).text
        self.assertEqual(order_state, '已发货')
        print("商品为已发货状态正确")
        self.back()
        self.back()
        # 修改已发货到交易完成
        myms.sql_assign_exec("update csm_order set status='4' where user_id='2018072411392004050001343390' and id='559' ")
        sleep(5)
        self.click_button(papaandroid.b_order_center)
        order_state = self.driver.find_element_by_xpath(papaandroid.fourthorder_state[1]).text
        self.assertEqual(order_state, '交易完成')
        print("商品为交易完成状态正确")
        # 验证信用回收
        self.click_button(papaandroid.fourthorder_state)
        self.click_button(papaandroid.b_credit_recycling2)
        # self.assertTrue(self.isElement(papaandroid.tx_credit_recycling))
        # print("订单详情页点击信用回收按钮，跳转正确")
        # self.back()
        self.back()
        self.back()
        self.back()


    # 新用户额度低于商品价格，进行购买商品流程
    def test_buy_below2(self):
        """“点击添加收货地址，在编辑地址页面输入各种情况点击保存按钮"""''
        #确认购买页面选中现金支付，点击确认购买按钮
        self.click_button(papaandroid.b_goods_address)
        # 在编辑地址页面不输入任何数据，点击保存按钮
        self.click_button(papaandroid.b_create_address)
        self.send_keys(papaandroid.edit_consigneename, '')
        self.click_button(papaandroid.b_submit)
        self.assertTrue(self.isElement(papaandroid.b_submit))
        print("无法点击保存按钮")
        self.send_keys(papaandroid.edit_consigneiphone, '13735865796')
        self.click_button(papaandroid.b_submit)
        self.assertTrue(self.isElement(papaandroid.b_submit))
        print("无法点击保存按钮")
        self.click_button(papaandroid.edit_location)
        self.click_button(papaandroid.b_provice)
        self.click_button(papaandroid.b_city)
        self.click_button(papaandroid.b_district)
        self.click_button(papaandroid.b_sure)
        self.click_button(papaandroid.b_submit)
        self.assertTrue(self.isElement(papaandroid.b_submit))
        print("无法点击保存按钮")
        self.back()


    # 新用户额度低于商品价格，进行购买商品流程
    def test_buy_below3(self):
        """“点击添加收货地址完成后，返回点击添加等操作"""''
        # 在编辑地址页面不输入任何数据，点击保存按钮
        self.click_button(papaandroid.b_create_address)
        self.send_keys(papaandroid.edit_consigneename, '吴越欣')
        self.send_keys(papaandroid.edit_consigneiphone, '13735865796')
        self.click_button(papaandroid.edit_location)
        self.click_button(papaandroid.b_provice)
        self.click_button(papaandroid.b_city)
        self.click_button(papaandroid.b_district)
        self.click_button(papaandroid.b_sure)
        self.send_keys(papaandroid.edit_detail, '13735865796')
        self.click_button(papaandroid.b_submit)
        sleep(6)
        self.assertEqual(self.driver.find_element_by_id(papaandroid.tx_assertName[1]).text,'吴越欣')
        print("收货地址为已添加的地址")



if __name__ == '__main__':
    # main_package.main_package(Case("test_buy_below1"),"/Users/xygjzgs/selenium/")
    main_package.main_package(Case("test_buy_below2"), "/Users/xygjzgs/selenium/")
    # main_package.main_package(Case("test_buy_below3"), "/Users/xygjzgs/selenium/")

