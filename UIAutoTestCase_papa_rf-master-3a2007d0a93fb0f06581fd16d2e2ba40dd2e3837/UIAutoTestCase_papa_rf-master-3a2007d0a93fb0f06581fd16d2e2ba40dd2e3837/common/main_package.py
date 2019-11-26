# _*_ coding:utf-8 _*_
import unittest,time
from common import HTMLTestRunner
# from common import HTMLTestRunner_cn

#测试主函数的封装
def main_package(case,path):
    suite = unittest.TestSuite()
    suite.addTest(case)
    first='信用卡android自动化回归_'
    timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    filename =path+ first+str(case).split('(')[0] + '_'+timestr + ".html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='测试结果',
        description='测试报告'
    )
    # runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp, title='测试结果',
    #                                           description='用例执行情况：',
    #                                           verbosity=2,
    #                                           retry=1)
    runner.run(suite)
    #测试报告关闭
    fp.close()
    # send_mail.sendreport()

