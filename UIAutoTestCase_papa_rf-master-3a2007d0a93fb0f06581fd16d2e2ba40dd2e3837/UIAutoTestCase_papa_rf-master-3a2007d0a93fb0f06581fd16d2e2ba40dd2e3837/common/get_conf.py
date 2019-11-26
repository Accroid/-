# -*- coding: utf-8 -*-

#通过自带的ConfigParser模块，读取邮件发送的配置文件，作为字典返回
#可选择json，xml，txt等数据载体
import configparser,os

def get_conf():
    conf_file = configparser.ConfigParser()

    # conf_file.read(os.path.join(os.getcwd(),'conf.ini'))
    conf_file.read(os.path.join(os.getcwd(),'conf.ini'))

    # print os.path.join(os.getcwd(),'common\conf.ini')
    conf = {}

    conf['sender'] = conf_file.get("email","sender")

    conf['receiver'] = conf_file.get("email","receiver")

    conf['smtpserver'] = conf_file.get("email","smtpserver")

    conf['username'] = conf_file.get("email","username")

    conf['password'] = conf_file.get("email","password")

    return conf
