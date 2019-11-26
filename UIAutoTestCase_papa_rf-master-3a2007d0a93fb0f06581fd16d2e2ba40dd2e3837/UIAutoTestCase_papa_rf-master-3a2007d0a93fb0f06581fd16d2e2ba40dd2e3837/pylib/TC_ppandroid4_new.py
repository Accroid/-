# _*_ coding:utf-8 _*_
import sys

import TerminalHandle_TK
import dataprovide,stringHelper,papaandroid

sys.path.append("..")
import unittest
from time import sleep


class TC_ppandroid4_new:
    sc = TerminalHandle_TK.TerminalHandle_TK()
    #新用户注册验证
    def test_new1(self):
        """“新用户注册验证，在登陆账号框内输入错误的手机号（长度）"""''
        self.sc.initialization()
        self.sc.pop_close()
        self.sc.click_button(papaandroid.b_My)
        self.sc.click_button(papaandroid.b_login)
        td_login = dataprovide.fetchTestData(4, 'login', 0, '1', '')
        for i in range(len(td_login)):
            print('------------------------------')
            self.sc.send_keys(papaandroid.edit_iphone, dataprovide.dict_gen(td_login)[i + 1]['iphone'])
            self.sc.click_button(papaandroid.b_next)
            # self.assertTrue(self.sc.isElement(papaandroid.edit_iphone))
            # print("在登陆账号框内输入错误的手机号（长度），点击下一步，场景正确无法点击下一步正确")
            # result1 =self.sc.isElement(papaandroid.edit_iphone)
            return self.sc.isElement(papaandroid.edit_iphone)

    def test_new2(self):
        """“新用户注册验证，在登陆账号框内输入错误的手机号（字符类型）"""''
        td_login = dataprovide.fetchTestData(4, 'login', 0, '2', '')
        for i in range(len(td_login)):
            print('------------------------------')
            self.sc.send_keys(papaandroid.edit_iphone, dataprovide.dict_gen(td_login)[i + 1]['iphone'])
            self.sc.click_button(papaandroid.b_next)
            # self.assertTrue(self.sc.isElement(papaandroid.edit_iphone))
            # print("在登陆账号框内输入错误的手机号（字符类型），点击下一步，场景正确无法点击下一步正确")
            # result1 = self.sc.isElement(papaandroid.edit_iphone)
            # return result1
            return self.sc.isElement(papaandroid.edit_iphone)

    def test_new3(self):
        """“新用户注册验证，在登陆账号框内输入未注册过的手机号，点击下一步，并在设置密码页面输入不符合密码规则的密码（长度）"""''
        td_login = dataprovide.fetchTestData(4, 'login', 0, '3', '')
        for i in range(len(td_login)):
            print('------------------------------')
            self.sc.send_keys(papaandroid.edit_iphone, dataprovide.dict_gen(td_login)[i + 1]['iphone'])
            self.sc.click_button(papaandroid.b_next)
            sleep(5)
            # self.assertTrue(self.sc.isElement(papaandroid.edit_pwd2))
            # print("进入设置密码页面正确")
            result1 = self.sc.isElement(papaandroid.edit_pwd2)
            self.sc.send_keys(papaandroid.edit_pwd2, dataprovide.dict_gen(td_login)[i + 1]['pwd'])
            self.sc.send_keys(papaandroid.edit_picverification, '111')
            # self.sc.send_keys(papaandroid.edit_verification, '111')
            self.sc.send_keys(papaandroid.edit_verification, '111')
            self.sc.click_button(papaandroid.b_login2)
            result2 = self.sc._find_toast('密码长度为', 10, 0.5, self.sc.driver)
            # self.assertIsNotNone(actResult)
            # print('提示：密码长度应在6-16位之间的场景验证正确')
            # result1 = self.sc.isElement(papaandroid.edit_pwd2)
            return result1,result2



    def quit(self):
        self.sc.driver.close_app()
        self.sc.driver.quit()





