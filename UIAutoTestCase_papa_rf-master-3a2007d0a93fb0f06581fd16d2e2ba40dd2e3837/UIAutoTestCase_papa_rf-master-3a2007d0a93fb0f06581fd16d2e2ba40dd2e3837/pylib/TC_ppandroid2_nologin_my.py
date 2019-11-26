# _*_ coding:utf-8 _*_
import sys

import TerminalHandle_TK
import dataprovide,stringHelper,papaandroid

sys.path.append("..")
import unittest
from time import sleep


class TC_ppandroid2_nologin_my:
    sc = TerminalHandle_TK.TerminalHandle_TK()
    #“我的”页面验证页面要素跳转
    def test_nologin_my(self):
        """“我的”页面验证页面元素跳转"""''
        self.sc.initialization()
        self.sc.pop_close()
        self.sc.click_button(papaandroid.b_My)
        self.sc.click_button(papaandroid.b_login)
        # self.assertTrue(self.sc.isElement(papaandroid.edit_iphone))
        # print("点击登陆按钮，成功进入进入登陆页面")
        result1 =self.sc.isElement(papaandroid.edit_iphone)
        self.sc.back()
        self.sc.click_button(papaandroid.b_goods_address)
        # self.assertTrue(self.sc.isElement(papaandroid.edit_iphone))
        # print("点击收货地址，成功进入进入登陆页面")
        result2 =self.sc.isElement(papaandroid.edit_iphone)
        self.sc.back()
        self.sc.click_button(papaandroid.b_about)
        return result1,result2


    def quit(self):
        self.sc.driver.close_app()
        self.sc.driver.quit()



