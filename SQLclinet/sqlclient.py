#coding=utf-8
import MySQLdb
import os
import csv
import time

conn = MySQLdb.connect(
host="192.168.1.185",	#连接地址
user="root",			#数据库账号
password="newpassword",	#数据库密码
port=3306,				#数据库端口号，非Mysql数据库需要修改
db='orders',			#要插数据的库名
charset="utf8")

#创建游标对象
c = conn.cursor()	#不用管这行是干嘛的
#读取csv文件内容
print("=============================================>>\n开始读取文件")
f = csv.reader(open("C:\\Users\\Accroid\\Desktop\\test11.csv"))		#先给excel文件转成csv后给路径放里面
time_start = time.time()
try:
    for row in f:
        id=row[0]	#数据库表内第一个字段，有多少字段加多少行代码 
        name=row[1]	#数据库表内第二个字段，有多少字段加多少行代码
        des=row[2]
        display_idx=row[3]
        print("取出数据为: "+id,name,des,display_idx)	#对应上面的表内字段，不需要也可以注释掉
        #这段sql是重点，insert into的具体SQL，values值查看表设计，非字符（int）串类型需要加''
        sql='''INSERT INTO sq_course(id, name, des, display_idx) VALUES (%s,'%s','%s','%s');'''%(id,name,des,display_idx)
        c.execute(sql)
        conn.commit()
    time_end = time.time()
    print("本次操作一共花费：", round(time_end - time_start,2),'s')
except BaseException as msg:
    print("error!插入失败，执行回滚操作，失败原因：",msg)
    conn.rollback()

# #查询tabname表
# c.execute("select * from tabname")
# #一次读取所有数据
# row = c.fetchall()
# print("当前库内所有数据：",row)