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


class Case(TK_papaandroid.Task, TK_TerminalHandle.TerminalHandle, unittest.TestCase):
    #商品详情 验证各个模块点击跳转
    def test_nologin_product(self):
        """ 商品详情 验证各个模块点击跳转 """''
        self.pop_close()
        self.click_button(papaandroid.b_good)
        self.click_button(papaandroid.b_hotProduct)
        self.assertTrue(self.isElement(papaandroid.tx_sku1))
        self.assertTrue(self.isElement(papaandroid.tx_sku2))
        self.assertTrue(self.isElement(papaandroid.tx_kefus))
        self.assertTrue(self.isElement(papaandroid.b_resell))
        self.assertTrue(self.isElement(papaandroid.b_buy))
        print("展示商品信息页面正确")
        self.click_button(papaandroid.tx_kefus)
        self.assertTrue(self.isElement(papaandroid.tx_assertHelp))
        print("进入帮助中心页面")
        self.back()
        self.click_button(papaandroid.b_resell)
        self.assertTrue(self.isElement(papaandroid.b_tologin))
        print("点击转卖换钱按钮，进入登陆页面")
        self.back()
        self.click_button(papaandroid.b_buy)
        self.assertTrue(self.isElement(papaandroid.b_tologin))
        print("点击立即购买按钮，进入登陆页面")
        self.back()
        self.back()
        # 验证排序
        first_price = stringHelper.goods_num_split(
            self.driver.find_element_by_xpath(papaandroid.tx_firstprice[1]).text)
        sec_price = stringHelper.goods_num_split(
            self.driver.find_element_by_xpath(papaandroid.tx_secondprice[1]).text)
        self.assertTrue(float(first_price)<float(sec_price))
        print("默认按价格降序排序正确")
        self.click_button(papaandroid.b_price)
        sleep(6)
        first_price = stringHelper.goods_num_split(
            self.driver.find_element_by_xpath(papaandroid.tx_firstprice[1]).text)
        sec_price = stringHelper.goods_num_split(
            self.driver.find_element_by_xpath(papaandroid.tx_secondprice[1]).text)
        self.assertTrue(float(first_price) > float(sec_price))
        print("点击后，商品正序排序正确")




if __name__ == '__main__':
    main_package.main_package(Case("test_nologin_product"),"/Users/xygjzgs/selenium/")
