# _*_ coding:utf-8 _*_
import sys

import TerminalHandle_TK
import dataprovide,stringHelper,papaandroid

sys.path.append("..")
import unittest
from time import sleep


class TC_ppandroid6_saling:
    sc = TerminalHandle_TK.TerminalHandle_TK()
    def test_saling(self):
        """“首次注册用户，已填写资料认证，进行转卖流程"""''
        self.sc.initialization()
        self.sc.pop_close()
        # self.sc.phone_login('13735865796', '123456')
        self.sc.click_button(papaandroid.b_good)
        self.sc.click_button(papaandroid.b_hotProduct)
        self.sc.click_button(papaandroid.b_resell)
        if self.sc.isElement(papaandroid.b_know) == True:
            print("弹出转卖换钱规则解释浮层")
            self.sc.click_button(papaandroid.b_know)
            self.sc.click_button(papaandroid.b_resell)
            result=self.sc.isElement(papaandroid.tx_orderDetails)
            # self.assertTrue(self.sc.isElement(papaandroid.tx_orderDetails))
            # print("无转卖换钱规则解释，进入确认转卖（订单详情）页面")
        else:
            # self.assertTrue(self.sc.isElement(papaandroid.tx_orderDetails))
            # print("无转卖换钱规则解释，进入确认转卖（订单详情）页面")
            result=self.sc.isElement(papaandroid.tx_orderDetails)
        return result


    def quit(self):
        self.sc.driver.close_app()
        self.sc.driver.quit()




