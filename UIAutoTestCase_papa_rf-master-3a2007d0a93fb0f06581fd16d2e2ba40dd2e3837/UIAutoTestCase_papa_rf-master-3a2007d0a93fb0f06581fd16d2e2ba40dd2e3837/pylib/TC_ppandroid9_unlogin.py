# _*_ coding:utf-8 _*_
import sys
import TerminalHandle_TK
import dataprovide,stringHelper,papaandroid

sys.path.append("..")
import unittest
from time import sleep


class TC_ppandroid9_unlogin:
    sc = TerminalHandle_TK.TerminalHandle_TK()
    #进行退出登录
    def test_loginout(self):
        """进行退出登录"""''
        self.sc.initialization()
        self.sc.pop_close()
        self.sc.click_button(papaandroid.b_My)
        self.sc.my_swipe_to_up()
        self.sc.click_button(papaandroid.b_login_out)
        self.sc.click_button(papaandroid.b_login_out_sure)

    def quit(self):
        self.sc.driver.close_app()
        self.sc.driver.quit()



