# _*_ coding:utf-8 _*_
import sys

import TerminalHandle_TK,sql_normal_csmall
import dataprovide,stringHelper,papaandroid

sys.path.append("..")
import unittest
from time import sleep


class TC_ppandroid8_buy_below:
    sc = TerminalHandle_TK.TerminalHandle_TK()
    # 新用户额度低于商品价格，进行购买商品流程
    # def test_buy_below1(self):
    #     """“商品详情页面点击立即购买，修改处理订单状态  待发货状态-已发货-已完成"""''
    #     self.sc.initialization()
    #     self.sc.pop_close()
    #     # self.login('new')
    #     self.sc.click_button(papaandroid.b_good)
    #     self.sc.click_button(papaandroid.b_hotProduct)
    #     # 点击购买
    #     self.sc.click_button(papaandroid.b_buy)
    #     self.sc.click_button(papaandroid.b_CashPayments)
    #     self.sc.click_button(papaandroid.b_SelectBank1)
    #     self.sc.click_button(papaandroid.b_SelectBank2)
    #     self.sc.back()
    #     self.sc.back()
    #     self.sc.back()
    #     self.sc.click_button(papaandroid.b_My)
    #     self.sc.click_button(papaandroid.b_order_center)
    #     # 修改订单状态
    #     order_state = self.sc.driver.find_element_by_xpath(papaandroid.fourthorder_state[1]).text
    #     result1 =order_state
    #     result2='待发货'
    #     self.sc.back()
    #     self.sc.back()
    #     # 修改待发货到已发货
    #     myms = sql_normal_csmall.mysql_connect(sql_normal_csmall.db_info)
    #     myms.sql_assign_exec(
    #         "update csm_order set status='3' where user_id='2018072411392004050001343390' and id='559' ")
    #     self.sc.click_button(papaandroid.b_order_center)
    #     sleep(5)
    #     order_state2 = self.sc.driver.find_element_by_xpath(papaandroid.fourthorder_state[1]).text
    #     # self.assertEqual(order_state2, '已发货')
    #     # print("商品为已发货状态正确")
    #     result3 = order_state2
    #     result4 = '已发货'
    #     self.sc.back()
    #     self.sc.back()
    #     # 修改已发货到交易完成
    #     myms.sql_assign_exec(
    #         "update csm_order set status='4' where user_id='2018072411392004050001343390' and id='559' ")
    #     sleep(5)
    #     self.sc.click_button(papaandroid.b_order_center)
    #     sleep(5)
    #     order_state3 = self.sc.driver.find_element_by_xpath(papaandroid.fourthorder_state[1]).text
    #     # self.assertEqual(order_state3, '交易完成')
    #     # print("商品为交易完成状态正确")
    #     result5 = order_state3
    #     result6 = '交易完成'
    #     # 验证信用回收
    #     self.sc.click_button(papaandroid.fourthorder_state)
    #     self.sc.back()
    #     self.sc.back()
    #     self.sc.back()
    #     return result1,result2,result3,result4,result5,result6


    # 新用户额度低于商品价格，进行购买商品流程
    def test_buy_below2(self):
        self.sc.initialization()
        self.sc.pop_close()
        self.sc.click_button(papaandroid.b_My)
        """“点击添加收货地址，在编辑地址页面输入各种情况点击保存按钮"""''
        # 确认购买页面选中现金支付，点击确认购买按钮
        self.sc.click_button(papaandroid.b_goods_address)
        # 在编辑地址页面不输入任何数据，点击保存按钮
        self.sc.click_button(papaandroid.b_create_address)
        self.sc.send_keys(papaandroid.edit_consigneename, '')
        self.sc.click_button(papaandroid.b_submit)
        # self.assertTrue(self.sc.isElement(papaandroid.b_submit))
        # print("无法点击保存按钮")
        result1 = self.sc.isElement(papaandroid.b_submit)
        self.sc.send_keys(papaandroid.edit_consigneiphone, '13735865796')
        self.sc.click_button(papaandroid.b_submit)
        # self.assertTrue(self.sc.isElement(papaandroid.b_submit))
        # print("无法点击保存按钮")
        result2= self.sc.isElement(papaandroid.b_submit)
        self.sc.click_button(papaandroid.edit_location)
        self.sc.click_button(papaandroid.b_provice)
        self.sc.click_button(papaandroid.b_city)
        self.sc.click_button(papaandroid.b_district)
        self.sc.click_button(papaandroid.b_sure)
        self.sc.click_button(papaandroid.b_submit)
        # self.sc.assertTrue(self.sc.isElement(papaandroid.b_submit))
        # print("无法点击保存按钮")
        result3= self.sc.isElement(papaandroid.b_submit)
        self.sc.back()
        return result1,result2,result3


    # 新用户额度低于商品价格，进行购买商品流程
    def test_buy_below3(self):
        """“点击添加收货地址完成后，返回点击添加等操作"""''
        # 在编辑地址页面不输入任何数据，点击保存按钮
        self.sc.click_button(papaandroid.b_create_address)
        sleep(8)
        self.sc.send_keys(papaandroid.edit_consigneename, 'wuyuexin')
        self.sc.send_keys(papaandroid.edit_consigneiphone, '13735865796')
        self.sc.click_button(papaandroid.edit_location)
        self.sc.click_button(papaandroid.b_provice)
        self.sc.click_button(papaandroid.b_city)
        self.sc.click_button(papaandroid.b_district)
        self.sc.click_button(papaandroid.b_sure)
        self.sc.send_keys(papaandroid.edit_detail, '13735865796')
        self.sc.click_button(papaandroid.b_submit)
        sleep(6)
        # self.assertEqual(self.sc.driver.find_element_by_id(papaandroid.tx_assertName[1]).text, '吴越欣')
        # print("收货地址为已添加的地址")
        result1 = self.sc.driver.find_element_by_id(papaandroid.tx_assertName[1]).text
        result2 = 'wuyuexin'
        return result1, result2



    def quit(self):
        self.sc.driver.close_app()
        self.sc.driver.quit()


