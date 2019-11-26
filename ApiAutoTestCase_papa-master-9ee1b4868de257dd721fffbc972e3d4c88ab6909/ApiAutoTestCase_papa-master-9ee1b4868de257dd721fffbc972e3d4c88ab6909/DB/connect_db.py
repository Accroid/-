#coding=utf-8
import sql_normal_csldata,sql_normal_csmall,sql_normal_csorder,sql_normal_cspown,sql_normal_cscuser


def run_sql_normal_csldata(sql):
    myms = sql_normal_csldata.mysql_connect(sql_normal_csldata.db_info)
    myms.sql_exec(sql)
    myms.close()

def run_sql_normal_csmall(sql):
    myms2 = sql_normal_csmall.mysql_connect(sql_normal_csmall.db_info)
    myms2.sql_exec(sql)
    myms2.close()

def run_sql_normal_csorder(sql):
    myms3 = sql_normal_csorder.mysql_connect(sql_normal_csorder.db_info)
    myms3.sql_exec(sql)
    myms3.close()

def run_sql_normal_cspown(sql):
    myms4 = sql_normal_cspown.mysql_connect(sql_normal_cspown.db_info)
    myms4.sql_exec(sql)
    myms4.close()

def run_sql_normal_cscuser(sql):
    myms5 = sql_normal_cscuser.mysql_connect(sql_normal_cscuser.db_info)
    myms5.sql_exec(sql)
    myms5.close()


if __name__ =='__main__':
    run_sql_normal_csorder("update cso_contract_msg set contractStatus=100 where id in(select a.id from(select id from  cso_contract_msg where gmt_create =(select max(gmt_create)  from  cso_contract_msg))a)")