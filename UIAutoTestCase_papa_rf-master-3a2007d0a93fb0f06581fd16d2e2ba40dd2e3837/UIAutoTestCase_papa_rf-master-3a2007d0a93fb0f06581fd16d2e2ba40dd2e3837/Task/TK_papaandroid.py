# _*_ coding:utf-8 _*_
# import urllib.request, urllib.error, urllib.parse
# import urllib.request, urllib.parse, urllib.error
import sys

from Task import TK_TerminalHandle
from common import dataprovide, sql_normal,stringHelper
from element_locator import papaandroid
import imp
import requests
sys.path.append("..")
import unittest,time
from time import sleep
from selenium.webdriver.common.by import By
import random

# imp.reload(sys)
# sys.setdefaultencoding('utf-8')

class Task(TK_TerminalHandle.TerminalHandle,unittest.TestCase):

    #弹出框关闭
    def pop_close(self):
        sleep(15)
        if self.isElement(papaandroid.b_Pop) == True:
            self.click_button(papaandroid.b_Pop_close)
        sleep(3)

    #用户登录
    def login(self,casekey):
        self.click_button(papaandroid.b_My)
        x=self.get_login_number(casekey)
        user=dataprovide.fetchTestData(4,'login',0,x,'')
        if self.isElement(papaandroid.b_login)==False:
            print('用户已登录')
            self.driver.back()
        else:
            self.click_button(papaandroid.b_login)
            self.send_keys(papaandroid.edit_iphone, dataprovide.dict_gen(user)[1]['iphone'])
            self.click_button(papaandroid.b_next)
            self.send_keys(papaandroid.edit_pwd, dataprovide.dict_gen(user)[1]['pwd'])
            sleep(3)
            self.click_button(papaandroid.b_loginsure)
            if self.isElement(papaandroid.tx_papa)==True:
                print('用户登录成功，跳转页面正确')
                sleep(3)
            else:
                self.back()

    #退出登录
    def loginout(self):
        self.click_button(papaandroid.b_WoDe)
        if self.isElement(papaandroid.b_DengLu_ZhuCe) == False:
            sleep(3)
            self.click_button(papaandroid.b_More)
            self.click_button(papaandroid.b_loginout)
            sleep(2)
            self.click_button(papaandroid.b_loginout_sure)
            print ("退出登录成功")
            sleep(1)
        else:
            self.back()


    #点击排序：默认
    def orderby_default(self):
        self.click_button((By.XPATH, papaandroid.b_MoRen[1]))


    def get_login_number(self,casekey):
        list1=[]
        for i in range(len(dataprovide.fetchTestData(3,'login',0))):
            if casekey==dataprovide.fetchTestData(3,'login',0)[i]['Casekey']:
                list1.append(i+1)
            else:
                pass
        return  list1[0]

    def user(self,casekey):
        x=self.get_login_number(casekey)
        return dataprovide.fetchTestData(4,'login',0,x,'')

        # 支付回调
    def order(self, ordernum):
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        a = random.randint(0, 999999)
            # 模拟回调代码
        params = "service=alipay.wap.trade.create.direct&v=1.0&sec_id=MD5&notify_data=<notify><payment_type>1</payment_type><subject>" \
                     + "[寿全斋]红糖姜冲泡茶纸盒装12g*10条/盒" + "</subject><trade_no>" + "2016030821001004360263" + str(a) + "\
                </trade_no><buyer_email>13738171756</buyer_email><gmt_create>" \
                     + now + "</gmt_create><notify_type>trade_status_sync</notify_type><quantity>1</quantity><out_trade_no>" + str(
                ordernum) + \
                     "</out_trade_no><notify_time>" + now + \
                     "</notify_time><seller_id>2088021886187623</seller_id><trade_status>TRADE_SUCCESS</trade_status>\
                     <is_total_fee_adjust>N</is_total_fee_adjust><total_fee>" \
                     + str(0.01) + "</total_fee><gmt_payment>" \
                     + now + "</gmt_payment><seller_email>zhuzhu@wansecheng.com</seller_email><price>" + str(0.01) \
                     + "</price><buyer_id>" + "2088122051790362" + "</buyer_id><notify_id></notify_id><use_coupon>N</use_coupon></notify>"
        secid = "3ieev5tm0zfma78up2kp9gaz1dln1kmb"
        sign = self.md5(params + secid)
        # 将参数post到指定接口
        url = 'http://tt5.ewanse.com/pay-callback/alipay'
        payload = {'service': 'alipay.wap.trade.create.direct', 'v': '1.0', 'sec_id': 'MD5', 'sign': sign,
                       'notify_data': \
                           "<notify><payment_type>1</payment_type><subject>" \
                           + "[寿全斋]红糖姜冲泡茶纸盒装12g*10条/盒" + "</subject><trade_no>2016030821001004360263" + str(a) + "</trade_no>\
                <buyer_email>13738171756</buyer_email><gmt_create>" + \
                           now + "</gmt_create><notify_type>trade_status_sync</notify_type><quantity>1</quantity><out_trade_no>" + \
                           str(ordernum) + "</out_trade_no><notify_time>" + \
                           now + "</notify_time><seller_id>2088021886187623</seller_id><trade_status>TRADE_SUCCESS</trade_status>\
                <is_total_fee_adjust>N</is_total_fee_adjust><total_fee>" \
                           + str(
                               0.01) + "</total_fee><gmt_payment>" + now + "</gmt_payment><seller_email>zhuzhu@wansecheng.com</seller_email><price>" \
                           + str(
                               0.01) + "</price><buyer_id>2088122051790362</buyer_id><notify_id></notify_id><use_coupon>N</use_coupon></notify>"}
        test_data_urlencode = urllib.parse.urlencode(payload)
        r = urllib.request.Request(url=url, data=test_data_urlencode)
        res_data = urllib.request.urlopen(r)
        res = res_data.read()
        print(res, res_data)

        # 获取订单号并支付
        def get_order_num(self):
            sleep(6)
            self.my_swipe_to_down()
            sleep(4)
            status1 = self.driver.find_element_by_id(papaandroid.tx_DingdanZhuangTai[1]).text
            status2 = status1[5:]
            status3 = status1.encode(encoding='UTF-8')
            self.assertEqual(status3, papaandroid.wait_pay)
            print("等待买家支付状态正确")
            self.my_swipe_to_up()
            self.my_swipe_to_up()
            sleep(6)
            order_num = self.driver.find_element_by_id(papaandroid.tx_DingDanHao[1]).text
            myms = sql_normal.mysql_connect(sql_normal.db_info)
            myms.sql_assign_exec("update gzseed_vancelle_order.gss_weidian_order set order_amount=0.01 where order_sn='" \
                                 + order_num + "'")
            order_amount_num = myms.sql_assign_exec("SELECT  gzseed_vancelle_order.gss_weidian_order.order_amount\
             FROM gzseed_vancelle_order.gss_weidian_order where order_sn='" + order_num + "'")
            order_amount = str(myms.fetchone())
            order_id_num = myms.sql_assign_exec("SELECT  gzseed_vancelle_order.gss_weidian_order.order_id \
            FROM gzseed_vancelle_order.gss_weidian_order where order_sn ='" + order_num + "'")
            order_id = str(myms.fetchone())
            self.order(order_num)
            myms.sql_assign_exec("update gzseed_vancelle_order.gss_packages set notify_time=UNIX_TIMESTAMP(NOW()) \
                    where bill_id in (SELECT order_id from gzseed_vancelle_order.gss_order_info where order_sn='" + order_num + "')")
            r = requests.get(papaandroid.payment)
            # 修改备货中状态修改为已发货
            myms.sql_assign_exec("update gzseed_vancelle_order.gss_packages set delivery_time=UNIX_TIMESTAMP(NOW()) , \
                    shipping_status=50 where bill_id in (SELECT order_id from gzseed_vancelle_order.gss_order_info where order_sn='" \
                                 + order_num + "')")
            r = requests.get(papaandroid.delivered)
            sleep(3)
            print(r)
            # self.click_button(klmandroid.b_FuKuan)
            # self.assertTrue(self.isElement(By.XPATH,(klmandroid.order_fail)[1]))
            print("通过接口付款成功")
            # self.click_button(klmandroid.order_sure)
            # self.driver.get(klmandroid.rebate)
            # rebate=myms.sql_exec_normal_all("select amount FROM gzseed_vancelle_user.gss_weidian_rebates WHERE order_sn='" \
            #                                 +order_num+"'")[0][0]
            # self.assertTrue(rebate!=0)
            # print '有返利数据，正确'