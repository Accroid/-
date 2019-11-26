# _*_ coding:utf-8 _*_
import sys

import TerminalHandle_TK
import dataprovide,stringHelper,papaandroid

sys.path.append("..")
import unittest
from time import sleep


class TC_ppandroid5_old:
    sc = TerminalHandle_TK.TerminalHandle_TK()
    #老用户登陆验证
    def test_old1(self):
        """“在登陆账号框内输入错误的手机号（字符类型）"""''
        self.sc.initialization()
        self.sc.pop_close()
        self.sc.click_button(papaandroid.b_My)
        self.sc.click_button(papaandroid.b_login)
        td_login = dataprovide.fetchTestData(4, 'login', 0, '5', '')
        for i in range(len(td_login)):
            print('------------------------------')
            self.sc.send_keys(papaandroid.edit_iphone, dataprovide.dict_gen(td_login)[i + 1]['iphone'])
            self.sc.click_button(papaandroid.b_next)
            # self.assertTrue(self.sc.isElement(papaandroid.edit_iphone))
            # print("在登陆账号框内输入错误的手机号（长度），点击下一步，场景正确，无法点击下一步正确")
            # result1 = self.sc.isElement(papaandroid.edit_iphone)
            # return result1
            return self.sc.isElement(papaandroid.edit_iphone)


    def test_old2(self):
        """“老用户登陆验证，输入已注册的手机号，点击下一步按钮，点击忘记密码按钮"""''
        td_login = dataprovide.fetchTestData(4, 'login', 0, '6', '')
        for i in range(len(td_login)):
            print('------------------------------')
            self.sc.send_keys(papaandroid.edit_iphone, dataprovide.dict_gen(td_login)[i + 1]['iphone'])
            self.sc.click_button(papaandroid.b_next)
            self.sc.click_button(papaandroid.b_forgetpwd)
            # self.assertTrue(self.sc.isElement(papaandroid.tx_assertforgetpwd))
            # print("进入找回密码页面正确")
            # result1 = self.sc.isElement(papaandroid.tx_assertforgetpwd)
            # self.sc.back()
            # return result1
            return self.sc.isElement(papaandroid.tx_assertforgetpwd)


    def test_old3(self):
        """“老用户登陆验证，在找回密码页面不输入任何数据，点击完成"""''
        td_login = dataprovide.fetchTestData(4, 'login', 0, '7', '')
        for i in range(len(td_login)):
            # self.sc.send_keys(papaandroid.edit_iphone, dataprovide.dict_gen(td_login)[i + 1]['iphone'])
            # self.sc.click_button(papaandroid.b_next)
            # self.sc.click_button(papaandroid.b_forgetpwd)
            self.sc.click_button(papaandroid.b_finish)
            # self.assertTrue(self.sc.isElement(papaandroid.tx_assertforgetpwd))
            # print("无法点击完成按钮正确")
            # result1 = self.sc.isElement(papaandroid.edit_iphone)
            self.sc.back()
            # return result1
            return self.sc.isElement(papaandroid.edit_iphone)


    def test_old4(self):
        """“在找回密码页面输入错误的密码（长度错误），点击完成"""''
        td_login = dataprovide.fetchTestData(4, 'login', 0, '8', '')
        for i in range(len(td_login)):
            print('------------------------------')
            self.sc.send_keys(papaandroid.edit_iphone, dataprovide.dict_gen(td_login)[i + 1]['iphone'])
            self.sc.click_button(papaandroid.b_next)
            self.sc.click_button(papaandroid.b_forgetpwd)
            self.sc.send_keys(papaandroid.tx_assertforgetpwd, '11')
            self.sc.click_button(papaandroid.b_finish)
            # self.assertTrue(self.sc.isElement(papaandroid.tx_assertforgetpwd))
            # print("无法点击完成按钮正确")
            # result1 = self.sc.isElement(papaandroid.edit_iphone)
            self.sc.back()
            # return result1
            return self.sc.isElement(papaandroid.edit_iphone)


    def test_old5(self):
        """“在找回密码页面输入密码，验证码，图形验证码，点击完成"""''
        td_login = dataprovide.fetchTestData(4, 'login', 0, '6', '')
        for i in range(len(td_login)):
            print('------------------------------')
            self.sc.send_keys(papaandroid.edit_iphone, dataprovide.dict_gen(td_login)[i + 1]['iphone'])
            self.sc.click_button(papaandroid.b_next)
            self.sc.click_button(papaandroid.b_forgetpwd)
            self.sc.send_keys(papaandroid.edit_register_cet_pwd,'123456')
            self.sc.send_keys(papaandroid.edit_register_cet_img_code,'1' )
            self.sc.send_keys(papaandroid.edit_register_cet__code2, '1')
            self.sc.click_button(papaandroid.b_finish)
            # self.assertTrue(self.sc.isElement(papaandroid.tx_papa))
            # print("无法点击完成按钮正确")
            # result1 = self.sc.isElement(papaandroid.edit_iphone)
            # return result1
            # return self.sc.isElement(papaandroid.tx_papa)


    def quit(self):
        self.sc.driver.close_app()
        self.sc.driver.quit()


