# _*_ coding:utf-8 _*_
import sys

import TerminalHandle_TK
import dataprovide,stringHelper,papaandroid

sys.path.append("..")
from time import sleep



class TC_ppandroid1_nologin_firstpage:
    sc = TerminalHandle_TK.TerminalHandle_TK()
    #首页-有好货页面页面要素验证
    def test_nologin_firstpage(self):
        """“首页-有好货页面页面元素验证"""''
        self.sc.initialization()
        self.sc.pop_close()
        sleep(5)
        result1 =self.sc.isElement(papaandroid.tx_papa)
        result2 =self.sc.isElement(papaandroid.b_Havegood)
        result3 =self.sc.isElement(papaandroid.b_good)
        result4 =self.sc.isElement(papaandroid.b_My)
        return result1,result2,result3,result4


    def quit(self):
        self.sc.driver.close_app()
        self.sc.driver.quit()



