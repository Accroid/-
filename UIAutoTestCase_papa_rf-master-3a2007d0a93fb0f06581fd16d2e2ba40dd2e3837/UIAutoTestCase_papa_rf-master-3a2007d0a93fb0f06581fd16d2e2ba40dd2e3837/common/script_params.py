# -*- coding: utf-8 -*-
"""python命令行参数处理"""
from appium import webdriver
import time
from common import start_appium
import threading

def iOS_driver(devicename,port):
    desired_caps = {
        'platformName': 'iOS',
        'platformVersion': '',
        'deviceName': devicename,
        'bundleId': 'com.quvideo.XiaoYing',
        'app': '',
        'noReset': True,
        # 'automationName': 'XCUITest',
        'udid': 'auto',
        'xcodeOrgId': 'BMP99N9345',
        'xcodeSigningId': 'iPhone Developer',
        'autoLaunch': True,
        # 'wdaLocalPort': wdaport
    }

    remote_url = 'http://localhost:' + str(port) + '/wd/hub'
    time.sleep(5)
    drivers = webdriver.Remote(remote_url, desired_caps)
    return drivers


# device_list = [('6s2050', 8001)]
device_list = [('i62078'),('6s2050')]
start_appium.myserver().create_pools(len(device_list))
port_list = start_appium.myserver().ports

for i in range(len(device_list)):
    dev = device_list[i][0]
    # wdaport = device_list[i][1]
    port = port_list[i]
    print(dev, port)
    time.sleep(10)
    driver = iOS_driver(dev, port)

# 多线程启动
class appiumThread(threading.Thread):
    def __init__(self, dev, port):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.dev = dev
        self.port = port
    def run(self):
        time.sleep(2)
        driver = iOS_driver(self.dev,self.port)
        return driver

def create_threads(device_list):
    thread_instances = []
    if device_list != []:
        for device in device_list:
            dev = device
            # wda_port = wdaport
            print("deviceinfo:",dev,port)
            instance = appiumThread(dev,port)
            thread_instances.append(instance)
        for instance in thread_instances:
            instance.start()
            time.sleep(5)

        for instance in thread_instances:
            instance.join()

device_list = [('6s2050', 8001)]
create_threads(device_list)