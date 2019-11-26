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
    #新用户注册验证
    def test_new1(self):
        """“新用户注册验证，在登陆账号框内输入错误的手机号（长度）"""''
        self.pop_close()
        self.click_button(papaandroid.b_My)
        self.click_button(papaandroid.b_login)
        td_login = dataprovide.fetchTestData(4, 'login', 0, '1', '')
        for i in range(len(td_login)):
            print('------------------------------')
            self.send_keys(papaandroid.edit_iphone, dataprovide.dict_gen(td_login)[i + 1]['iphone'])
            self.click_button(papaandroid.b_next)
            self.assertTrue(self.isElement(papaandroid.edit_iphone))
            print("在登陆账号框内输入错误的手机号（长度），点击下一步，场景正确无法点击下一步正确")


    def test_new2(self):
        """“新用户注册验证，在登陆账号框内输入错误的手机号（字符类型）"""''
        td_login = dataprovide.fetchTestData(4, 'login', 0, '2', '')
        for i in range(len(td_login)):
            print('------------------------------')
            self.send_keys(papaandroid.edit_iphone, dataprovide.dict_gen(td_login)[i + 1]['iphone'])
            self.click_button(papaandroid.b_next)
            self.assertTrue(self.isElement(papaandroid.edit_iphone))
            print("在登陆账号框内输入错误的手机号（字符类型），点击下一步，场景正确无法点击下一步正确")


    def test_new3(self):
        """“新用户注册验证，在登陆账号框内输入未注册过的手机号，点击下一步，并在设置密码页面输入不符合密码规则的密码（长度）"""''
        td_login = dataprovide.fetchTestData(4, 'login', 0, '3', '')
        for i in range(len(td_login)):
            print('------------------------------')
            self.send_keys(papaandroid.edit_iphone, dataprovide.dict_gen(td_login)[i + 1]['iphone'])
            self.click_button(papaandroid.b_next)
            sleep(5)
            self.assertTrue(self.isElement(papaandroid.edit_pwd2))
            print("进入设置密码页面正确")
            self.send_keys(papaandroid.edit_pwd2, dataprovide.dict_gen(td_login)[i + 1]['pwd'])
            self.send_keys(papaandroid.edit_picverification, '111')
            self.send_keys(papaandroid.edit_verification, '111')
            self.click_button(papaandroid.b_login2)
            actResult = self._find_toast('密码长度为', 10, 0.5, self.driver)
            self.assertIsNotNone(actResult)
            print('提示：密码长度应在6-16位之间的场景验证正确')




if __name__ == '__main__':
    # main_package.main_package(Case("test_new1"),"/Users/xygjzgs/selenium/")
    # main_package.main_package(Case("test_new2"), "/Users/xygjzgs/selenium/")
    main_package.main_package(Case("test_new3"), "/Users/xygjzgs/selenium/")


