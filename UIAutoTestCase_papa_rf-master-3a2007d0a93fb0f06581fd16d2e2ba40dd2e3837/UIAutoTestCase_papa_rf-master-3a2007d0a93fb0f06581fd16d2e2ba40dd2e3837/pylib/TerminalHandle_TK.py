# _*_ coding:utf-8 _*_
import dataprovide
# from PIL import Image
import math
import operator,re
from functools import reduce

__author__ = 'Eddie'

# import re, hashlib, urllib.request, urllib.parse, urllib.error,urllib.request,urllib.error,urllib.parse
import os,time, unittest
from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import smtplib
from email.mime.text import MIMEText
from xml.dom.minidom import parse
from selenium.webdriver.common.action_chains import ActionChains
from email.header import Header
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import logging
import logging.config
# from common import script_ultils
import papaandroid

class TerminalHandle_TK:
    timeout=30
    # def __init__(self, methodName='runTest'):
    #     super(TerminalHandle, self).__init__(methodName)
    #
    # def setUp(self):
    #     # 每次执行测试用例之前调用。无参数，无返回值。该方法抛出的异常都视为error，
    #     # 而不是测试不通过。没有默认的实现。
    #     log.picpath = []
    #     log.pics = []
    #     self.verificationErrors = []
    #
    #
    # def tearDown(self):
    #     # 每次执行测试用例之后调用。无参数，无返回值。
    #     # 测试方法抛出异常，该方法也正常调用，该方法抛出的异常都视为error，而不是测试不通过。
    #     # 只用setUp()调用成功，该方法才会被调用。没有默认的实现
    #     self.assertEqual([], self.verificationErrors)
    #     #"Hook method for deconstructing the test fixture after testing it."
    #     # self.driver.quit()

    # @classmethod
    # def setUpClass(cls):
    #     # 一个类方法在单个类测试之前运行。
    #     # setUpClass作为唯一的参数被调用时,必须使用classmethod()作为装饰器
    #     desired_caps = {}
    #     desired_caps['platformName'] = 'Android'
    #     desired_caps['platformVersion'] = '7.1'
    #     desired_caps['automationName'] = 'UiAutomator2'
    #     desired_caps['deviceName'] = '05157df523fab611'
    #     desired_caps['udid'] = '0815f821df8c2804'
    #     # 啪啪钱包的活动名及包名
    #     desired_caps['appPackage'] = 'com.xncredit.dxb'
    #     desired_caps['appActivity'] = 'ui.activity.SplashActivity'
    #     # desired_caps['appPackage'] = 'com.greate.myapplication'
    #     # desired_caps['appActivity'] = '.views.activities.XnMainActivity'
    #     # desired_caps['unicodeKeyboard'] = 'True'
    #     desired_caps['resetKeyboard'] = 'True'
    #     desired_caps['noReset'] = 'True'
    #     desired_caps['chromeOptions']: {
    #         'androidProcess': 'com.tencent.mm:tools'
    #     }
    #
    #     cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def initialization(self):

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['deviceName'] = '0815f821df8c2804'
        desired_caps['udid'] = '0815f821df8c2804'
        # 啪啪钱包的活动名及包名
        desired_caps['appPackage'] = 'com.xncredit.dxb'
        desired_caps['appActivity'] = 'ui.activity.SplashActivity'
        # desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['noReset'] = 'True'
        desired_caps['chromeOptions']={'androidProcess': 'com.tencent.mm:tools'}

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # @classmethod
    # def tearDownClass(cls):
    #     # 一个类方法在单个类测试之后运行。
    #     # setUpClass作为唯一的参数被调用时,必须使用classmethod()作为装饰器
    #     "Hook method for deconstructing the class fixture after running all tests in the class."
    #     cls.driver.quit()

    # 弹出框关闭
    def pop_close(self):
        sleep(15)
        if self.isElement(papaandroid.b_Pop) == True:
            self.click_button(papaandroid.b_Pop_close)
        sleep(3)

    # 用户登录
    def phone_login(self,phone,password):
        self.click_button(papaandroid.b_My)
        if self.isElement(papaandroid.b_login) == False:
            print('用户已登录')
            self.driver.back()
        else:
            self.click_button(papaandroid.b_login)
            self.send_keys(papaandroid.edit_iphone, phone)
            self.click_button(papaandroid.b_next)
            self.send_keys(papaandroid.edit_pwd, password)
            sleep(3)
            self.click_button(papaandroid.b_loginsure)



    def find(self,loc):
        # 查找元素
        '''
        find element.
        Usage:
        driver.find((By.XPATH,"//a"))
        '''
        try:
            WebDriverWait(self.driver,self.timeout).until(lambda drive:drive.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except NoSuchElementException as e:
            # log.screenshot(self)
            # log.creathtml(log.creathtml(log.pics))
            print("%s 页面中超时%ds未能找到 %s 元素%s" %(self,self.timeout,loc,e))
        except TimeoutException:
            return False


    def find_elements(self,loc):
        # 查找元素集合
        '''
        find elements.
        Usage:
        driver.find_elements((By.XPATH,"//a"))
        '''
        try:
            WebDriverWait(self.driver,self.timeout).until(lambda drive:drive.find_elements(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except Exception as e:
            # log.screenshot(self)
            # log.creathtml(log.creathtml(log.pics))
            print("%s 页面中超时%ds未能找到 %s 元素%s" %(self,self.timeout,loc,e))

    def click_keys(self,loc):
        # 找到元素后进行点击
        '''
        click keys
        Usage:
        driver.click_keys((By.XPATH,"//a"))
        '''
        self.find(loc).click()

    def clear_keys(self,loc):
        # 找到元素后进行清理
        '''
        clear keys
        Usage:
        driver.clear_keys((By.XPATH,"//a"))
        '''
        self.find(loc).clear()

    def send_keys(self,loc,value):
        # # 找到元素后进行输入
        '''
        send keys
        Usage:
        send_keys((By.XPATH,"//a"),'a')
        '''
        # sleep(4)
        self.clear_keys(loc)
        # self.find(loc).click()
        # context=self.find(loc).get_attribute('text')
        # self.driver.keyevent(123)
        # for i in range(0,len(context)):
        #     self.driver.keyevent(67)
        # sleep(3)
        self.find(loc).send_keys(value)

    def click_button(self,loc):
        # # 找到元素后进行点击
        '''
        click button
        Usage:
        click_button((By.XPATH,"//a"))
        '''
        sleep(3)
        self.find(loc).click()
        # sleep(2)

    def switch_to_context(self):
        contexts = self.driver.contexts
        # 切换到webview
        print (self.driver.contexts)
        self.driver.switch_to.context(contexts[1])
        # 获取当前的环境，看是否切换成功
        now = self.driver.current_context
        print (now)


    def switch_to_native(self):
        self.driver.switch_to.context("NATIVE_APP")

    def geturl(self):
        return self.get_current_url(),self.driver.current_context()

    def switch_to_window_handle(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])

    def script(self,src):
        # 调用其他脚本
        '''
        execute_script
        Usage:
        script(src)
        '''
        sleep(3)
        return self.driver.execute_script(src)

    def wait(self, secs):
        #隐式等待, 此处的隐式等待是针对Driver 每次执行命令的 最长执行时间也可以理解为超时时间
        #一些人对此处有误解，认为是让Driver等一段时间，  确实某些时候能让Driver等一段时间
        # 但是影响是全局的，每次Driver执行 找不到元素都会等待此处设置的时间
        # 假设某处将此值设置的太长，必须在执行完成之后还原回来
        # 否则判断一个元素是否存在的时候，就会遇到很坑爹的问题。
        '''
        Implicitly wait.All elements on the page.
        Usage:
        driver.wait(10)
        '''
        self.driver.implicitly_wait(secs)

    def set_window(self, wide, high):
        # 设置浏览器窗口宽高。
        '''
        Set browser window wide and high.
        Usage:
        driver.set_window(wide,high)
        '''
        self.driver.set_window_size(wide, high)

    def right_click(self, loc):
        #右键单击元素
        '''
        Right click element.
        Usage:
        driver.right_click((By.XPATH,"//a"))
        '''
        el = self.find(loc)
        ActionChains(self.driver).context_click(el).perform()

    def move_to_element(self, loc):
        # 移动鼠标
        '''
        Mouse over the element.
        Usage:
        driver.move_to_element((By.XPATH,"//a"))
        '''
        el = self.find(loc)
        ActionChains(self.driver).move_to_element(el).perform()

    def double_click(self, loc):
        # 双击
        '''
        Double click element.
        Usage:
        driver.double_click((By.XPATH,"//a"))
        '''
        el = self.find(loc)
        ActionChains(self.driver).double_click(el).perform()

    def drag_and_drop(self, loc1, loc2):
        #拖动一个元素到一定的位置，然后把它放下。
        '''
        Drags an element a certain distance and then drops it.
        Usage:
        driver.drag_and_drop((By.XPATH,"//a"),(By.XPATH,"//b"))
        '''
        element  = self.find(loc1)
        target  = self.find(loc2)
        ActionChains(self.driver).drag_and_drop(element , target).perform()

    def get_display(self, loc):
        #得到显示的元素，返回结果为真或假。
        '''
        Gets the element to display,The return result is true or false.
        Usage:
        driver.get_display(By.XPATH,"//a")
        '''
        el = self.find(loc)
        return el.is_displayed()

    def get_current_url(self):
        return self.driver.current_url

    def back(self):
        # 返回
        sleep(2)
        self.back()
        sleep(2)

    def isElement(self,loc):
        # 判断元素是否存在
        '''
        Determine whether elements exist
        Usage:
        isElement(By.XPATH,"//a")
        '''
        sleep(1)
        flag=None
        try:
            if loc[0] == "id":
                #self.driver.implicitly_wait(60)
                self.driver.find_element_by_id(loc[1])
            elif loc[0] == "xpath":
                #self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath(loc[1])
            elif loc[0] == "class":
                self.driver.find_element_by_class_name(loc[1])
            elif loc[0] == "link text":
                self.driver.find_element_by_link_text(loc[1])
            elif loc[0] == "partial link text":
                self.driver.find_element_by_partial_link_text(loc[1])
            elif loc[0] == "name":
                self.driver.find_element_by_name(loc[1])
            elif loc[0] == "tag name":
                self.driver.find_element_by_tag_name(loc[1])
            elif loc[0] == "css selector":
                self.driver.find_element_by_css_selector(loc[1])
            flag = True
        except NoSuchElementException as e:
            flag = False
        finally:
            return flag

    def isElement_Exist(self,loc):
        # 判断元素是否存在
        '''
        Determine whether elements exist
        Usage:
        isElement_Exist(By.XPATH,"//a")
        '''
        sleep(1)
        flag=None
        try:
            self.find(loc)
            flag = True
        except NoSuchElementException as e:
            flag = False
        finally:
            return flag

    def click_by_adb(self,x, y):
        # 利用adb指令进行点击
        print("Start tap anypoint point")
        # cmd = "adb shell input tap"+" "+str(x)+" "+str(y)
        cmd = 'adb shell input tap {} {}'.format(x, y)
        # print ('excute command >>>{}'.format(cmd))
        os.popen(cmd)

    def screenshot(self):
        # 截图
        path = "C:\\"
        tx_BiaoTi = "selenium_test_result"
        timestr = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
        new_path = os.path.join(path, tx_BiaoTi)
        if not os.path.isdir(new_path):
            os.makedirs(new_path)
            self.driver.get_screenshot_as_file(new_path+"\\"+"result_" + timestr + ".png")
        else:
            self.driver.get_screenshot_as_file(new_path+"\\"+"result_" + timestr + ".png")

    def refresh(self):
        # 刷新网页
        '''
        refresh  page
        Usage:
        driver.refresh
        '''
        self.driver.implicitly_wait(10)
        self.driver.refresh()

    def list_to_str(self,string):
        #转到unicode字符串
        '''
        string to unicode
        Usage:
        list_to_str(str)
        '''
        str_symptom = str(string).replace('u\'','\'')
        return str_symptom.decode("unicode-escape")

    def get_text(self,loc):
        # 获取文本

        '''
        get text
        Usage:
        get_text(By.XPATH,"//a")
        '''
        sleep(3)
        return self.find(loc).text

    def get_url(self,url):

        '''
        get url
        Usage:
        get_url(url)
        '''
        sleep(3)
        return self.driver.get(url)

    def get_title(self,url):
        # 获取标题
        '''
        get tx_BiaoTi
        Usage:
        get_tx_BiaoTi(url):
        '''
        self.driver.get(url)
        return self.driver.title

    def _find_toast(self,message,timeout,poll_frequency,driver):
        message = '//*[contains(@text,\'{}\')]'.format(message)
        element = WebDriverWait(driver,timeout,poll_frequency).until(expected_conditions.presence_of_element_located((By.XPATH,message)))
        return element

    def verify_stock(self,stocknum):
        # 根据数量验证商品库存状态
        if stocknum>0 and stocknum<=10:
            stock_state='(仅剩'+str(stocknum)+'件)'
        elif stocknum>1 and stocknum<=100:
            stock_state='库存紧张'
        else:
            stock_state='库存充足'
        return stock_state

    def read_xml(self):
        xml_file_path = 'E:\\klmandroidnew\\common\\test-data.xml'
        xml = open(xml_file_path, 'rb')
        tree = parse(file=xml)
        collection = tree.documentElement
        return collection.getElementsByTagName('case')

    def IsListSorted_guess(self,lst):
        # 排序
        listLen = len(lst)
        if listLen <= 1:
            return True
            #由首个元素和末尾元素猜测可能的排序规则
        if lst[0] == lst[-1]: #列表元素相同
            for elem in lst:
                if elem != lst[0]: return False
        elif float(lst[0]) < float(lst[-1]): #列表元素升序
            for i, elem in enumerate(lst[1:]):
                if elem < lst[i]: return 1
        else: #列表元素降序
            for i, elem in enumerate(lst[1:]):
                if elem > lst[i]: return 2


    #搜索页价格显示处理
    def price_deal(self,string):
        return string.split('￥')[1].split('VIP')[0]

    #地址以：做分割处理
    def address_deal(self,string):
        return string.split("：")[1]

    #计算税费
    def taxes(self,num):
        return "%.1f" %float(num*0.7*0.17)

    def get_window_size(self):
        """
        get current windows size mnn
        :return:windowSize
        """
        global windowSize
        windowSize = self.driver.get_window_size()
        return windowSize

    def get_size(self):
        """获取屏幕分辨率."""
        rect = self.driver.get_window_size()
        return rect['width'], rect['height']

    # 获取整个屏幕大小
    def my_swipe_to_up(self,during=None):
        # 向上滑动
        """
        swipe UP
        :param during:
        :return:
        """
        # if windowSize == None:
        sleep(3)
        window_size = self.get_window_size()

        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width/2, height*3/4, width/2, height/4, during)

    # 获取整个屏幕大小
    def my_swipe_to_up2(self,during=None):
        """
        swipe UP
        :param during:
        :return:
        """
        # if windowSize == None:
        sleep(3)
        window_size = self.get_window_size()

        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width/2, height*3/4, width/2, height/2, during)

    # 获取整个屏幕大小
    def my_swipe_to_down(self,during=None):
        # 向下滑动
        """
        swipe down
        :param during:
        :return:
        """
        window_size = self.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width/2, height/4, width/2, height*3/4, 1000)

    # 获取整个屏幕大小
    def my_swipe_to_left(self,during=None):
        # 向左滑动
        """
        swipe left
        :param during:
        :return:
        """
        window_size = self.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width/4, height/2, width*3/4, height/2, during)

    # 获取整个屏幕大小
    def my_swipe_to_right(self,during=None):
        # 向右滑动
        """
        swipe right
        :param during:
        :return:
        """
        window_size = self.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width*4/5, height/2, width/5, height/2, during)

    # path_lists = test_init(self)
    # logger = logger_init(self)

    def swipe_by_ratio(self,start_x, start_y, direction, ratio, duration=None):
        """
        按照屏幕比例的滑动.

        :param start_x: 起始横坐标
        :param start_y: 起始纵坐标
        :param direction: 滑动方向，只支持'up'、'down'、'left'、'right'四种方向参数
        :param ratio: 滑动距离与屏幕的比例，范围0到1
        :param duration: 滑动时间，单位ms
        :return:

        demo：sc.swipe_by_ratio(start_x, start_bottom, 'right', 0.5, 500)

        demo：选择某个元素进行滑动操作
        el_collage = sc.driver.find_element_by_name("画中画")
        coord_x = el_collage.location.get('x')
        coord_y = el_collage.location.get('y')
        sc.swipe_by_ratio(coord_x, coord_y, 'left', 0.6, 800)
        """
        direction_list = ['up', 'down', 'left', 'right']
        if direction not in direction_list:
            script_ultils.logger.error(u'滑动方向%s不支持', direction)

        width, height = self.get_size()

        def swipe_up():
            """上滑."""
            end_y = start_y - ratio * height
            if end_y < 0:
                script_ultils.logger.warning(u'上滑距离过大')
                return False
            else:
                self.driver.swipe(start_x, start_y, start_x, end_y, duration)
            return True

        def swipe_down():
            """下滑."""
            end_y = start_y + ratio * height
            if end_y > height:
                script_ultils.logger.warning(u'下滑距离过大')
                return False
            else:
                self.driver.swipe(start_x, start_y, start_x, end_y, duration)
            return True

        def swipe_left():
            """左滑."""
            end_x = start_x - ratio * width
            if end_x < 0:
                script_ultils.logger.warning(u'左滑距离过大')
                return False
            else:
                self.driver.swipe(start_x, start_y, end_x, start_y, duration)
            return True

        def swipe_right():
            """右滑."""
            end_x = start_x + ratio * width
            if end_x > width:
                script_ultils.logger.warning(u'右滑距离过大')
                return False
            else:
                self.driver.swipe(start_x, start_y, end_x, start_y, duration)
            return True

        swipe_dict = {'up': swipe_up, 'down': swipe_down, 'left': swipe_left,
                      'right': swipe_right}
        return swipe_dict[direction]()

    def capture_screen(self,fun, path):
        """用appium client截屏."""
        if path.endswith('/') or path.endswith('\\'):
            # 考虑到截图操作可能很多，为了效率，所以使用列表拼接字符串
            script_ultils.mkdir(path)
            local_time = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
            name_list = [local_time, fun, '.png']

            capture_name = '_'.join(name_list)
            path_name = path + capture_name

            self.driver.get_screenshot_as_file(path_name)
            script_ultils.logger.info(u'保存截图%s', capture_name)
        else:
            script_ultils.logger.error(u'截图路径请使用"\\"或者"/"结尾')
            return False
        return True

    def find_by_classes(self,classname, fun, path):
        """遍历classname，分步点击截图."""
        element_list = self.driver.find_elements_by_class_name(classname)

        for element_em in element_list:
            element_em.click()
            time.sleep(.500)
            self.capture_screen(fun, path)
        return True

    def find_by_ids(self,resource_id, fun, path):
        """遍历id，分步点击截图."""
        element_list = self.driver.find_elements_by_id(resource_id)

        for element_em in element_list:
            element_em.click()
            time.sleep(.500)
            self.capture_screen(fun, path)
        return True

    def view_by_ids(self,resource_id, fun, path):
        """遍历id，分步点击、截图、退出."""
        element_list = self.driver.find_elements_by_id(resource_id)

        for element_em in element_list:
            element_em.click()
            time.sleep(.300)
            self.capture_screen(fun, path)
            self.driver.press_keycode(4)
        return True

    def back(self):
        # os.popen("adb shell input keyevent 4")
        self.driver.back()
        sleep(2)


    def sentmail(self,file_new):
        mail_info = get_conf.get_conf()
        #发送邮箱
        sender = mail_info['sender']
        #接收邮箱
        receiver = mail_info['receiver']
        #发送邮件主题
        subject = '[AutomationTest]UI自动化测试报告通知'
        #发送邮箱服务器
        smtpserver = mail_info['smtpserver']
        #发送邮箱用户/密码
        username = mail_info['username']
        password = mail_info['password']
        f = open(file_new, 'rb')
        mail_body = f.read()
        f.close()
        #中文需参数'utf-8'
        msg = MIMEText(mail_body,'html','utf-8')
        msg['Subject'] =  Header(subject, 'utf-8')
        msg['From'] = sender
        msg['To'] = ''.join(receiver)
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print('email has send out !')

    def sendreport(self):
        result_dir = 'D:\\selenium_python\\report'
        lists=os.listdir(result_dir)
        lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not
        os.path.isdir(result_dir+"\\"+fn) else 0)
        print(('最新测试生成的报告： '+lists[-1]))
        #找到最新生成的文件
        file_new = os.path.join(result_dir,lists[-1])
        print(file_new)
        #调用发邮件模块
        self.sentmail(file_new)

    def fetch_coord(self,location,size):
        #'''location:{'y':1050,'x':'100'}
        #   size:{'weidth':100,'heigth':100'''
        start_x = location['x']
        start_y = location['y']
        average_x = size['width'] / 3.0
        average_y = size['height'] / 4.0
        coord_list = []
        for i in range(4):
            _y = int(start_y + average_y * i + average_y / 2)
            for j in range(3):
                _x = int(start_x + average_x * j + average_x / 2)
                coord_list.append([(_x,_y)])
        return coord_list

    #修改图片大小
    def modify_pic_size(self):
        js="var el=document.getElementsByClassName('attr_img')[0];el.style.height='10px';el.style.width='10px'"
        self.script(js)

    #检测是否安装某应用,如果安装输出路径,否则执行安装
    def get_path(self):
        print("Start get app path...")
        # 列出所有的安装包
        packages = os.popen("adb shell pm list packages").read()
        # 本地包路径
        path = "/Users/huajie/Desktop/txt_test.apk"
        if packages.find("com.pingan.wetalk") != -1:
            # 输出包路径信息
            findurl = os.popen("adb shell pm path com.pingan.wetalk").read()
            # 截取包路径
            print(findurl.split(':')[1].strip())
            # os.popen("adb uninstall com.pingan.wetalk")
        else:
            print("Install first")
            os.popen("adb install"+" "+path)
            os.popen("adb shell input keyevent 3")
            path = os.popen("adb shell pm path com.pingan.wetalk").read()
            print(path.split(':')[1].strip())
            # print "Then uninstall"
            # os.popen("adb uninstall com.pingan.wetalk")
        print("Install successed.")

    # 实现自动获取当前连接电脑的设备ID
    def get_deviceID(self):
        print("start get deviceid")
        deviceID = os.popen("adb devices").read()
        print("The attached deviceid is "+deviceID.split()[4])


    #实现如果存在则启动app,按home键,杀进程,如果不存在先安装再启动
    def launch(self):
        print("start lanuch...")
        packages = os.popen("adb shell pm list packages ").read()
        path = "/Users/huajie/Desktop/txt_test.apk"
        if packages.find("com.pingan.wetalk") != -1:
            print("Just launch it.")
            # 启动app
            os.popen("adb shell am start -n com.pingan.wetalk/com.pingan.wetalk.module.splash.activity.SplashActivity")
            # android应用启动很慢,等一等才能看到效果
            time.sleep(30)
            os.popen("adb shell input keyevent 3")
            os.popen("adb shell am force-stop com.pingan.wetalk")
        else:
            print("Install first")
            os.popen("adb install"+" "+path)
            time.sleep(5)
            # 安装后需要点击确定安装(使用坐标，如下坐标基于三星S6 Edge)
            os.popen("adb shell input tap 720 2480")
            print("Then launch it.")
            # 启动app
            os.popen("adb shell am start -n com.pingan.wetalk/com.pingan.wetalk.module.splash.activity.SplashActivity")
            # os.popen("adb shell input keyevent 3")
            # os.popen("adb shell am force-stop com.pingan.wetalk")


    #使用adb完成一张截图并保存
    def screenshot_adb(self):
        print("Start get the screenshot...")
        os.popen("adb shell /system/bin/screencap -p /sdcard/screenshot.png")

    # 通过aapt解析指定apk包，并且得到该apk包的包名与LauchActivity名，并输出
    def get_apkinfo(self):
        print("start get the apkinfo by aapt")
        path = "/Users/huajie/Desktop/txt_test.apk"
        # 列出包所有信息并按包名过滤
        apkinfo_name = os.popen("aapt dump badging "+path+"|grep package").read()
        # 按'分割字符串取第二即可
        package_name = apkinfo_name.split("'")[1]
        # 列出包所有信息并按启动activity过滤
        apkinfo_activity = os.popen("aapt dump badging "+path+"|grep launchable-activity").read()
        # 按'分割字符串取第二即可
        launch_activity = apkinfo_activity.split("'")[1]
        print("The package name is "+package_name)
        print("The lanuch activity is "+launch_activity)

    #手机相关信息输出,并截图
    def phonemessage(self):
        #版本
        version=os.popen("adb shell grep ro.build.version.release /system/build.prop").read()
        version1=re.search("(?<==).*", version)
        print('手机版本:'+version1.group(0))
        # 型号
        model =os.popen("adb shell grep ro.product.model /system/build.prop").read()
        model1 =re.search("(?<==).*", model )
        print('手机型号:'+model1.group(0))
        #系统版本
        brand =os.popen("adb shell grep ro.product.brand /system/build.prop").read()
        brand1 =re.search("(?<==).*", brand )
        print('手机系统版本:'+brand1.group(0))
        # a="D:\\appium\\appiumresult\\result_"+ model1.group(0) + timestr + ".jpg"
        # a = model1.group(0).split()
        # b = "".join(a)
        # sleep(2)
        # self.driver.get_screenshot_as_file("D:\\appium\\appiumresult\\result_"+b+ timestr + ".jpg")

    #当你的电脑连接着两台设备时，自动获取第一台设备，使用adb进行安装卸载操作
    def get_first_device(self):
        print("start install apk to the appointed device")
        path = "/Users/huajie/Desktop/txt_test.apk"
        # 列出所有的device
        devices = os.popen("adb devices").read()
        # 根据空格分割取出第一个device id
        first_device_id = devices.split()[4]
        # 指定id设备上进行安装和卸载
        os.popen("adb -s "+first_device_id+" install "+path)
        time.sleep(5)
        # 进行device的操作也需要-s指定设备
        os.popen("adb -s "+first_device_id+" shell input keyevent 3")
        time.sleep(3)
        # 卸载
        os.popen("adb -s "+first_device_id+" uninstall com.pingan.wetalk")
        time.sleep(3)



