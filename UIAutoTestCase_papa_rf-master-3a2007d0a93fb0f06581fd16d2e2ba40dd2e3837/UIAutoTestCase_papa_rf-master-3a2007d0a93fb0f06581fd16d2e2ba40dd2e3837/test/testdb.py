# _*_ coding:utf-8 _*_
from pylib import dataprovide,stringHelper,papaandroid,sql_normal_csmall,sql_normal_csorder

myms = sql_normal_csmall.mysql_connect(sql_normal_csmall.db_info)
myms_csorder = sql_normal_csorder.mysql_connect(sql_normal_csorder.db_info)

myms_csorder.sql_assign_exec(
            " update cso_repayment_plan set repayment_status=1 where contract_id='CO20180803004188670'")
myms_csorder.sql_assign_exec(
            "update cso_contract_msg set contract_Status=212 where id='CO20180803004188670' ")
myms.sql_assign_exec(
            "update csm_order set status=1,contract_status=212 where contract_no ='CO20180803004188670'")
#
myms.sql_assign_exec(
            "update csm_order set status='2' where user_id='2018072411392004050001343390' and id='559'")
    #
myms_csorder.sql_assign_exec(
            " update cso_repayment_plan set repayment_status=1 where contract_id='CO20180803003959191'")
myms_csorder.sql_assign_exec(
            "update cso_contract_msg set contract_Status=212 where id='CO20180803003959191' ")
myms.sql_assign_exec(
            "update csm_order set status=2,contract_status=212 where contract_no ='CO20180803003959191'")
myms.conn_close()
myms.cur_close()