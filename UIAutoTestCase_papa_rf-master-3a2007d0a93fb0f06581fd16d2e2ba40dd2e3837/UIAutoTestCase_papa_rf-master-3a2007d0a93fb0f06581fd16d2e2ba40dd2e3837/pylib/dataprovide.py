# _*_ coding:utf-8 _*_
import sql_dict,sql_normal
# from test import test_pymysql,test_pymysql_dict
#普通数据库数据读取以及字典数据库数据读取
myms = sql_dict.mysql_connect(sql_dict.db_info)
myms2=sql_normal.mysql_connect(sql_dict.db_info)


def fetchTestData(choose, table, num, *args):
    # 第一种 接收返回结果行的默认第一个
    # 第二种 接收num条返回结果行.如写2，则运行数据库指定表的前两条记录
    # 第三种 接收全部的返回结果行
    # 第四种 接收指定的返回结果行，如写3，5，则运行数据库指定表的第三条跟第五条记录。写3，4，6，则运行数据库指定表的第三条，第四条，第六条记录
    sql1="SELECT * from auto_test.td_papaandroid_"
    if choose == 1:
        return (myms.sqlexec(sql1+table,1,0),)
    elif choose==2:
        return myms.sqlexec(sql1+table,2,num)
    elif choose==3:
        return myms.sqlexec(sql1+table,3,0)
    elif choose==4:
        sql_init2=" where id in"
        return myms.sqlexec((sql1+table+sql_init2+str(args)),3,0)


def dict_gen(tuple1):
    result={}
    for i,v in enumerate(tuple1):
        result[i+1]=v
    return result


def runSql(sql_com):
    # 数据库数据处理
    return sql_normal.mysql_connect(sql_normal.db_info).sql_exec_normal(sql_com)





