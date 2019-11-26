# _*_ coding:utf-8 _*_
from . import sql_dict,sql_normal,sql_normal2
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

def runSql2(sql_com):
    # if(sql_com.)
    # sql = sql_normal.mysql_connect(sql_normal.db_info).sql_exec_normal("SELECT Spu_Id from auto_test.td_klmwap_singlesku where id=1")
    # sql_com=sql_com去掉小括号部分+"("+sql+")"
    # 数据库数据处理
    return sql_normal2.mysql_connect(sql_normal2.db_info).sql_exec_normal(sql_com)


#需要拼接的sql
#sku数据，名称，价格，图片
spu_name="SELECT spu_name from gzseed_vancelle_goods.gss_weidian_goods where spu_id="
sku_name="SELECT sku_name from gzseed_vancelle_goods.gss_weidian_goods where spu_id="
original_price="SELECT original_price from  gzseed_vancelle_goods.gss_weidian_goods where spu_id ="
vip_price="SELECT vip_price from  gzseed_vancelle_goods.gss_weidian_goods where spu_id="
cover_pic="SELECT cover_pic from  gzseed_vancelle_goods.gss_weidian_goods where spu_id ="
pic="SELECT pic from  gzseed_vancelle_goods.gss_weidian_goods where spu_id ="
#昵称
nick_name="SELECT nick_name from gzseed_vancelle_user.gss_profiles where user_id in (SELECT  user_id from gzseed_vancelle_system.gss_users where user_mobile ="
#真实姓名，手机
consignee="SELECT consignee from gzseed_vancelle_user.gss_address where user_id in (SELECT  user_id from gzseed_vancelle_system.gss_users where user_mobile="
mobile="SELECT mobile from gzseed_vancelle_user.gss_address where user_id in (SELECT  user_id from gzseed_vancelle_system.gss_users where user_mobile="
#省，市，区，地址
province_name="SELECT province_name from gzseed_vancelle_user.gss_address where user_id in (SELECT  user_id from gzseed_vancelle_system.gss_users where user_mobile="
city_name="SELECT city_name from gzseed_vancelle_user.gss_address where user_id in (SELECT  user_id from gzseed_vancelle_system.gss_users where user_mobile="
district_name="SELECT district_name from gzseed_vancelle_user.gss_address where user_id in (SELECT  user_id from gzseed_vancelle_system.gss_users where user_mobile="
address="SELECT address from gzseed_vancelle_user.gss_address where user_id in (SELECT  user_id from gzseed_vancelle_system.gss_users where user_mobile="

#默认搜索
default_search="SELECT  word FROM gzseed_vancelle_goods.gss_weidian_search_hotword WHERE word_type = 1"
hot_search="select word from gzseed_vancelle_goods.gss_weidian_search_hotword"

#按条件搜索的名字，图片，vip价格
SearchName="SELECT sku_name from gzseed_vancelle_goods.gss_weidian_goods where sku_name like"
SearchPic="SELECT cover_pic from gzseed_vancelle_goods.gss_weidian_goods where sku_name like"
SearchVipprice="SELECT vip_price from gzseed_vancelle_goods.gss_weidian_goods where sku_name like"


