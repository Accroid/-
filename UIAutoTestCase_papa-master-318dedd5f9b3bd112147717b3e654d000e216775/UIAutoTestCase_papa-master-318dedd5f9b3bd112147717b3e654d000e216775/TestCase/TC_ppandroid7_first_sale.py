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
    #新用户转卖流程验证
    def test_first_sale1(self):
        """“新用户第一次转卖流程验证，首页点击banner，并选择一个热卖商品点击，点击转卖"""''
        self.pop_close()
        self.click_button(papaandroid.b_good)
        self.click_button(papaandroid.b_hotProduct)
        self.click_button(papaandroid.b_resell)
        # self.assertTrue(self.isElement(papaandroid.b_resell))
        # print("转卖换钱置灰，无法点击正确")
        #校验点击去实名按钮跳转
        self.back()
        self.back()
        self.back()
        self.click_button(papaandroid.b_My)
        if self.isElement(papaandroid.b_go_value) == True:
            self.click_button(papaandroid.b_Realname)
            self.assertTrue(self.isElement(papaandroid.tx_assertRealname))
            print("进入实名认证页面正确")
        else:
            print("用户已实名认证")




if __name__ == '__main__':
    main_package.main_package(Case("test_first_sale1"),"/Users/xygjzgs/selenium/")

