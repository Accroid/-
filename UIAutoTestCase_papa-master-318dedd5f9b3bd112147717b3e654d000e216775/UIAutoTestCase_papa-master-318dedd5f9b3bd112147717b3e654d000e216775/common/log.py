# _*_ coding:utf-8 _*_
import logging
import os,time
import sys
sys.path.append("..")

mypath=''

# utf-8转gbk输出a
def utf2gbk(s):
    s = s.decode('utf-8').encode('gbk')
    return s

pics = []

##################################
#  日志
# 0: debug
# 1：info
# 2：warning
# 3：error
# 4: critical
###################################
def mylogger(msg, flag=1):
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='mylog.log',
                    filemode='w')
    # 创建一个handler，用于写入日志文件
    # fh = logging.FileHandler('/tmp/test.log')
    # 再创建一个handler，用于输出到控制台
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    # fh.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    if flag == 0:
        logging.debug(msg)
    elif flag == 1:
        logging.info(msg)
    elif flag == 2:
        logging.warning(msg)
    elif flag == 3:
        logging.error(msg)
    elif flag == 4:
        logging.critical(msg)
    logging.getLogger('').removeHandler(console)

#windows截屏
def screenshot(self):
    path = "C:\\"
    title = "selenium_test_result"
    timestr = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    new_path = os.path.join(path, title)
    pic = timestr + ".png"
    if not os.path.isdir(new_path):
        os.makedirs(new_path)
        self.driver.get_screenshot_as_file(new_path+"\\"+"result_" + timestr + ".png")
    else:
        self.driver.get_screenshot_as_file(new_path+"\\"+"result_" + timestr + ".png")
    mylogger("截图为：" + new_path+"\\"+"result_"+pic,2)
    pic= 'file:///'+new_path+"\\"+"result_"+pic
    pics.append(pic)

#  andriod截屏方法
def screenshot():
    myDate=time.localtime(time.time())
    dirname = mypath+('\\list_out\\screenshot')
    os.popen("adb wait-for-device")
    os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
    if not os.path.isdir(dirname):
        os.makedirs(dirname)
    pic = myDate.timestampname() + ".png"
    path = dirname + "/" + pic
    os.popen("adb pull /data/local/tmp/tmp.png " + path)
    os.popen("adb shell rm /data/local/tmp/tmp.png")
    mylogger("截图为：" + pic)
    pics.append(pic)


def creathtml(pic):
    # path1 = mypath+('\\list_out\\screenshot')
    # path2 = 'ftp:\\\\10.1.180.221\\screenshot'
    # path = path1
    print(pic)
    html = ''
    if list(range(len(pic))) > 0:
        for i in range(len(pic)):
            if i == 0:
                html = '<a href='  + pic[i] + ' target="_blank">' + pic[i] + '</a>'
            else:
                html = html + '<br /><a href=' + pic[i] + ' target="_blank">' + pic[i]+ '</a>'
    else:
        html = ''
    htmls = 'htmlbegin<td>' + html + '</td>htmlend'
    return htmls
