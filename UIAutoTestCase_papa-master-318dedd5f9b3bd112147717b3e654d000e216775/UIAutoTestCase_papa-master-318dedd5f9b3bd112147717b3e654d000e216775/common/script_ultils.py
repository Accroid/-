# -*- coding: utf-8 -*-
"""脚本里用到的一些方法."""
import os
import time
import logging
import logging.config


def get_logcat():
    path_log = "/Users/zhulixin/Desktop/UI_VivaVideo/Log/"
    run_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    # 手机日志(logcat)
    logcat_log = path_log + run_time + "logcat.log"
    logcat = "adb" + " logcat -v time > %s" % (logcat_log)
    os.popen(logcat)
    print("logcat 命令:", logcat)

def mkdir(path):
    """自定义的创建文件夹方法."""
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip('\\')
    path = path.rstrip('/')

    # 判断路径是否存在
    if os.path.exists(path):
        # 如果目录存在则不创建，并提示目录已存在
        logging.debug(u'%s目录已存在', path)
    else:
        # 如果不存在则创建目录
        os.makedirs(path)

        logging.info(u'%s创建成功', path)
        return True
    return False


def test_init():
    """测试初始化."""
    print('Test init begin!!!')
    local_time = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
    path_list = ['./Report/', local_time, '/']

    capture_list = path_list + ['screenshots/']
    log_list = path_list + ['logs/']
    report_list = path_list + ['reports/']

    capture_dir = ''.join(capture_list)
    log_dir = ''.join(log_list)
    report_dir = ''.join(report_list)

    mkdir(capture_dir)
    mkdir(log_dir)
    mkdir(report_dir)

    return capture_dir, log_dir, report_dir


# 日志格式
def logger_init():
    """logger初始化方法."""
    log_config = {
        'version': 1,
        'formatters': {
            'simple': {
                'format': u'%(asctime)s-%(levelname)s: %(message)s',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'DEBUG',
                'formatter': 'simple'
            },
            'file': {
                'class': 'logging.FileHandler',
                'filename': path_lists[1] + 'logging.log',
                'level': 'DEBUG',
                'formatter': 'simple',
                'encoding': 'utf-8'
            },
        },
        'loggers': {
            'root': {
                'handlers': ['console'],
                'level': 'DEBUG',
            },
            'simple': {
                'handlers': ['console', 'file'],
                'level': 'INFO',
            }
        }
    }
    logging.config.dictConfig(log_config)
    loggers = logging.getLogger('simple')
    return loggers


path_lists = test_init()
logger = logger_init()
