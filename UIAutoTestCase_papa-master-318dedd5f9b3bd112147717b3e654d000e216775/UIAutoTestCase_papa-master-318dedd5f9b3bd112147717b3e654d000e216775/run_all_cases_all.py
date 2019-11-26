# -*- coding:utf-8 -*-
__author__ = 'Eike'
import os
import time
import unittest
import threading
from common import HTMLTestRunner,data
# from common import HTMLTestRunner_cn,data


# 用例路径
# case_path = os.path.join(os.getcwd(), ".")
case_path = data.file+'UIAutoTestCase_papa/TestCase/'
result = data.file+"selenium/"

def Createsuite():
    # 定义单元测试容器
    testunit = unittest.TestSuite()
    # 定搜索用例文件的方法
    discover = unittest.defaultTestLoader.discover(case_path, pattern='TC_ppandroid8_buy_below.py',
                                                   top_level_dir=None)# 将测试用例加入测试容器中
    # discover = unittest.defaultTestLoader.discover(case_path, pattern='TC_1ppandroid9_buy_above.py',
    #                                                top_level_dir=None)  # 将测试用例加入测试容器中
    # discover = unittest.defaultTestLoader.discover(case_path, pattern='TC_1ppandroid10_saling_above.py',
    #                                                top_level_dir=None)  # 将测试用例加入测试容器中
    for test_suite in discover:
        for casename in test_suite:
            testunit.addTest(casename)
            print(casename)
    return testunit
test_case = Createsuite()


# 定义个报告存放路径，支持相对路径
# tdresult = result + day
if os.path.exists(result):
    imestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    filename = result  + "pp_Android.html"
    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='啪啪钱包ndroid自动化回归测试报告', description='用例执行情况：')
    # runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp, title='信用管家android服务模块自动化回归测试报告',
    #                                           description='用例执行情况：',
    #                                           verbosity=2,
    #                                           retry=1)
    # 运行测试用例
    runner.run(test_case)
    fp.close()  # 关闭报告文件
else:
    os.mkdir(result)
    filename = result + "\\" + "pp_Android.html"
    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='啪啪钱包ndroid自动化回归测试报告', description='用例执行情况：')
    # runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp, title='信用管家android服务模块自动化回归测试报告',
    #                                           description='用例执行情况：',
    #                                           verbosity=2,
    #                                           retry=1)
    # 运行测试用例
    runner.run(test_case)
    fp.close()  # 关闭报告文件
