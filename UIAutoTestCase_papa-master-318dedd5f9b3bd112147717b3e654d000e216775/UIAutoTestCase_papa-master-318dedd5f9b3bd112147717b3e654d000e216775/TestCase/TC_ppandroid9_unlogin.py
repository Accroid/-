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
    #进行退出登录
    def test_loginout(self):
        """进行退出登录"""''
        self.pop_close()
        self.click_button(papaandroid.b_My)
        self.my_swipe_to_up()
        self.click_button(papaandroid.b_login_out)
        self.click_button(papaandroid.b_login_out_sure)





if __name__ == '__main__':
    main_package.main_package(Case("test_loginout"),"/Users/xygjzgs/selenium/")
