# _*_ coding:utf-8 _*_
import logging
import os,time
from common import get_conf
import sys
sys.path.append("..")
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate



def sentmail(file_new):
    file_name = r"D:\BugReport.txt"
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

    server = smtplib.SMTP(smtpserver)
    server.login(username,password) #仅smtp服务器需要验证时

    # 构造MIMEMultipart对象做为根容器
    main_msg = MIMEMultipart()

    # 构造MIMEText对象做为邮件显示内容并附加到根容器
    text_msg = MIMEText("UI自动化测试报告通知,请看附件",_charset="utf-8")
    text_msg["Accept-Language"]="zh-CN"
    text_msg["Accept-Charset"]="ISO-8859-1,utf-8"
    main_msg.attach(text_msg)

    # 构造MIMEBase对象做为文件附件内容并附加到根容器
    contype = 'application/octet-stream'
    maintype, subtype = contype.split('/', 1)

    ## 读入文件内容并格式化 [方式2]－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
    data = open(file_new, 'rb')
    file_msg = MIMEBase(maintype, subtype)
    file_msg.set_payload(data.read())
    data.close( )
    # email.Encoders.encode_base64(file_msg)#把附件编码
    #－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
    ## 设置附件头
    basename = os.path.basename(file_new)
    file_msg.add_header('Content-Disposition','attachment', filename = basename)#修改邮件头
    main_msg.attach(file_msg)

    # 设置根容器属性
    main_msg['From'] = sender
    main_msg['To'] = receiver
    if not isinstance(subject,str):
        subject = str(subject)
    main_msg['Subject'] = subject
    main_msg['Date'] = formatdate( )
    # 得到格式化后的完整文本
    fullText = main_msg.as_string( )
    # 用smtp发送邮件
    try:
        server.sendmail(sender, receiver, fullText)
    finally:
        server.quit()

def sendreport():
    result_dir = 'C:\\selenium'
    lists=os.listdir(result_dir)
    # print lists
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not
    os.path.isdir(result_dir+"\\"+fn) else 0)
    # print (u'最新测试生 成的报告： '+lists[-1])
    #找到最新生成的文件
    file_new = os.path.join(result_dir,lists[-1])
    # print file_new
    #调用发邮件模块
    sentmail(file_new)
