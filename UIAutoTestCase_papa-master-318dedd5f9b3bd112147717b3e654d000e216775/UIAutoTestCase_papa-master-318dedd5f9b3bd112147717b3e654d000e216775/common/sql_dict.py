# _*_ coding:utf-8 _*_
import re,sys,pymysql

db_info = {'user': 'autotest',
                        'pwd': 'autotest@2017',
                        'host': '192.168.0.58',
                        'db': 'auto_test',
                        'port': 3306,
                        'charset':'utf8'}

class mysql_connect:
    def __init__(self, db_info):
        self.db_user = db_info['user']
        self.db_pw = db_info['pwd']
        self.db_host = db_info['host']
        self.db = db_info['db']
        self.port = db_info['port']
        self.charset = db_info['charset']
        self.conn = pymysql.connect(host=self.db_host,user=self.db_user, passwd=self.db_pw,  db=self.db,port=self.port,charset=self.charset)
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def fetchone(self):
        return self.cursor.fetchall()[0]

    def sql_exec(self, sql_com, need_return=0):
        if need_return == 1:
            try:
                self.cursor.execute(sql_com)
                return self.cursor
            except pymysql.Error as err:
                pass
                # print ("Error: {}".format(err.message))
                # sys.exit()
            finally:
                self.conn.commit()
        elif need_return == 0:
            try:
                self.cursor.execute(sql_com)
            except pymysql.Error as err:
                pass
            finally:
                self.conn.commit()

    def sql_assign_exec(self, sql_com,):
        value = 'not find'
        for i in self.sql_exec(sql_com, 1):
            value=i[0]
        return value

    def sqlexec(self, sql_com, need_return=0,num=0):
        if need_return == 1:
            try:
                self.cursor.execute(sql_com)
                result = self.cursor.fetchall()[0]
                return result
            except pymysql.Error as err:
                pass
            finally:
                self.conn.commit()
        elif need_return == 2:
            try:
                self.cursor.execute(sql_com)
                return self.cursor.fetchmany(num)
            except pymysql.Error as err:
                pass
        elif need_return == 3:
            try:
                self.cursor.execute(sql_com)
                return self.cursor.fetchall()
            except pymysql.Error as err:
                pass
            finally:
                self.conn.commit()

    def conn_close(self):
        return self.conn.close()
        pass

    def cur_close(self):
        return self.cursor.close()
        pass