# _*_ coding:utf-8 _*_
import sys

from Task import TK_papaandroid, TK_TerminalHandle
from common import dataprovide, main_package,stringHelper
from element_locator import papaandroid

sys.path.append("..")
import unittest
from time import sleep



class Case(TK_papaandroid.Task, TK_TerminalHandle.TerminalHandle, unittest.TestCase):
    #首页-有好货页面页面要素验证
    def test_nologin_firstpage(self):
        """“首页-有好货页面页面元素验证"""''
        self.pop_close()
        self.assertTrue(self.isElement(papaandroid.tx_papa))
        self.assertTrue(self.isElement(papaandroid.b_Havegood))
        self.assertTrue(self.isElement(papaandroid.b_good))
        self.assertTrue(self.isElement(papaandroid.b_My))
        print("进入有好货页面，顶部显示啪啪钱包，页面下方显示三个有好货、商品、“我的”三个页签正确")
        # self.click_button(papaandroid.tab_firstpage)
        # self.assertTrue(self.isElement(papaandroid.tx_assertFirstpage))
        # print("进入banner对应的页面正确")



if __name__ == '__main__':
    main_package.main_package(Case("test_nologin_firstpage"),"/Users/xygjzgs/selenium/")

