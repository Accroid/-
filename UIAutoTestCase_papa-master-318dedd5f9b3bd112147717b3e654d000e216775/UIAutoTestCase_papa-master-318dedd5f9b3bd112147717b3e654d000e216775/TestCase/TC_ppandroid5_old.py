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
    #老用户登陆验证
    def test_old1(self):
        """“在登陆账号框内输入错误的手机号（字符类型）"""''
        self.pop_close()
        self.click_button(papaandroid.b_My)
        self.click_button(papaandroid.b_login)
        td_login = dataprovide.fetchTestData(4, 'login', 0, '5', '')
        for i in range(len(td_login)):
            print('------------------------------')
            self.send_keys(papaandroid.edit_iphone, dataprovide.dict_gen(td_login)[i + 1]['iphone'])
            self.click_button(papaandroid.b_next)
            self.assertTrue(self.isElement(papaandroid.edit_iphone))
            print("在登陆账号框内输入错误的手机号（长度），点击下一步，场景正确，无法点击下一步正确")


    def test_old2(self):
        """“老用户登陆验证，输入已注册的手机号，点击下一步按钮，点击忘记密码按钮"""''
        td_login = dataprovide.fetchTestData(4, 'login', 0, '6', '')
        for i in range(len(td_login)):
            print('------------------------------')
            self.send_keys(papaandroid.edit_iphone, dataprovide.dict_gen(td_login)[i + 1]['iphone'])
            self.click_button(papaandroid.b_next)
            self.click_button(papaandroid.b_forgetpwd)
            self.assertTrue(self.isElement(papaandroid.tx_assertforgetpwd))
            print("进入找回密码页面正确")
            self.back()


    def test_old3(self):
        """“老用户登陆验证，在找回密码页面不输入任何数据，点击完成"""''
        td_login = dataprovide.fetchTestData(4, 'login', 0, '7', '')
        for i in range(len(td_login)):
            self.send_keys(papaandroid.edit_iphone, dataprovide.dict_gen(td_login)[i + 1]['iphone'])
            self.click_button(papaandroid.b_next)
            self.click_button(papaandroid.b_forgetpwd)
            self.click_button(papaandroid.b_finish)
            self.assertTrue(self.isElement(papaandroid.tx_assertforgetpwd))
            print("无法点击完成按钮正确")
            self.back()


    def test_old4(self):
        """“在找回密码页面输入错误的密码（长度错误），点击完成"""''
        td_login = dataprovide.fetchTestData(4, 'login', 0, '8', '')
        for i in range(len(td_login)):
            print('------------------------------')
            self.send_keys(papaandroid.edit_iphone, dataprovide.dict_gen(td_login)[i + 1]['iphone'])
            self.click_button(papaandroid.b_next)
            self.click_button(papaandroid.b_forgetpwd)
            self.send_keys(papaandroid.tx_assertforgetpwd, '11')
            self.click_button(papaandroid.b_finish)
            self.assertTrue(self.isElement(papaandroid.tx_assertforgetpwd))
            print("无法点击完成按钮正确")
            self.back()


    def test_old5(self):
        """“在找回密码页面输入密码，验证码，图形验证码，点击完成"""''
        td_login = dataprovide.fetchTestData(4, 'login', 0, '6', '')
        for i in range(len(td_login)):
            print('------------------------------')
            self.send_keys(papaandroid.edit_iphone, dataprovide.dict_gen(td_login)[i + 1]['iphone'])
            self.click_button(papaandroid.b_next)
            self.click_button(papaandroid.b_forgetpwd)
            self.send_keys(papaandroid.edit_register_cet_pwd,'123456')
            self.send_keys(papaandroid.edit_register_cet_img_code,'1' )
            self.send_keys(papaandroid.edit_register_cet__code2, '1')
            self.click_button(papaandroid.b_finish)
            self.assertTrue(self.isElement(papaandroid.tx_papa))
            print("无法点击完成按钮正确")



if __name__ == '__main__':
    main_package.main_package(Case("test_old1"),"/Users/xygjzgs/selenium/")
    # main_package.main_package(Case("test_old2"), "/Users/xygjzgs/selenium/")
    # main_package.main_package(Case("test_old3"), "/Users/xygjzgs/selenium/")
    # main_package.main_package(Case("test_old4"), "/Users/xygjzgs/selenium/")
    # main_package.main_package(Case("test_old5"), "/Users/xygjzgs/selenium/")

