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
    #“我的”页面验证页面要素跳转
    def test_nologin_my(self):
        """“我的”页面验证页面元素跳转"""''
        self.pop_close()
        self.click_button(papaandroid.b_My)
        self.click_button(papaandroid.b_login)
        self.assertTrue(self.isElement(papaandroid.edit_iphone))
        print("点击登陆按钮，成功进入进入登陆页面")
        self.back()
        self.click_button(papaandroid.b_goods_address)
        self.assertTrue(self.isElement(papaandroid.edit_iphone))
        print("点击收货地址，成功进入进入登陆页面")
        self.back()
        self.click_button(papaandroid.b_credit_recycling)
        # self.assertTrue(self.isElement(papaandroid.edit_iphone))
        print("点击信用回收，成功进入进入登陆页面")
        self.back()
        self.click_button(papaandroid.b_about)
        self.assertTrue(self.isElement(papaandroid.tx_assertAbout))
        print("点击关于我们，成功进入关于我们页面")





if __name__ == '__main__':
    main_package.main_package(Case("test_nologin_my"),"/Users/xygjzgs/selenium/")
