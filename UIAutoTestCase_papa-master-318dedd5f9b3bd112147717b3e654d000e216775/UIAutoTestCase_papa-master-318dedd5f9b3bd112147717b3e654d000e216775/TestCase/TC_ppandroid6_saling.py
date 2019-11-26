# _*_ coding:utf-8 _*_
import sys

from Task import TK_papaandroid, TK_TerminalHandle
from common import dataprovide, main_package,stringHelper
from element_locator import papaandroid

sys.path.append("..")
import unittest
from time import sleep



class Case(TK_papaandroid.Task, TK_TerminalHandle.TerminalHandle, unittest.TestCase):
    #首次注册用户，已填写资料认证，进行转卖流程
    def test_saling(self):
        """“首次注册用户，已填写资料认证，进行转卖流程"""''
        self.pop_close()
        self.login('new')
        self.click_button(papaandroid.b_good)
        self.click_button(papaandroid.b_hotProduct)
        self.click_button(papaandroid.b_resell)
        if self.isElement(papaandroid.b_know) == True:
            print("弹出转卖换钱规则解释浮层")
            self.click_button(papaandroid.b_know)
            self.click_button(papaandroid.b_resell)
            self.assertTrue(self.isElement(papaandroid.tx_orderDetails))
            print("无转卖换钱规则解释，进入确认转卖（订单详情）页面")
        else:
            self.assertTrue(self.isElement(papaandroid.tx_orderDetails))
            print("无转卖换钱规则解释，进入确认转卖（订单详情）页面")




if __name__ == '__main__':
    main_package.main_package(Case("test_saling"),"/Users/xygjzgs/selenium/")

