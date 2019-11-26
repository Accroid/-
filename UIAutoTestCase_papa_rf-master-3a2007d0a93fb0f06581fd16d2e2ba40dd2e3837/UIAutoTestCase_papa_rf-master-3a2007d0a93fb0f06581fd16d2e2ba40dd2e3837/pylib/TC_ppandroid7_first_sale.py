# _*_ coding:utf-8 _*_
import sys

import TerminalHandle_TK
import dataprovide,stringHelper,papaandroid

sys.path.append("..")
import unittest
from time import sleep


class TC_ppandroid7_first_sale:
    sc = TerminalHandle_TK.TerminalHandle_TK()
    #新用户转卖流程验证
    def test_first_sale1(self):
        """“新用户第一次转卖流程验证，首页点击banner，并选择一个热卖商品点击，点击转卖"""''
        self.sc.initialization()
        self.sc.pop_close()
        self.sc.click_button(papaandroid.b_good)
        self.sc.click_button(papaandroid.b_hotProduct)
        self.sc.click_button(papaandroid.b_resell)
        # self.assertTrue(self.isElement(papaandroid.b_resell))
        # print("转卖换钱置灰，无法点击正确")
        #校验点击去实名按钮跳转
        self.sc.back()
        self.sc.back()
        self.sc.back()
        self.sc.click_button(papaandroid.b_My)
        if self.sc.isElement(papaandroid.b_go_value) == True:
            self.sc.click_button(papaandroid.b_Realname)
            # self.assertTrue(self.sc.isElement(papaandroid.tx_assertRealname))
            # print("进入实名认证页面正确")
            result = self.sc.isElement(papaandroid.tx_assertRealname)
            return result
        else:
            print("用户已实名认证")



    def quit(self):
        self.sc.driver.close_app()
        self.sc.driver.quit()



