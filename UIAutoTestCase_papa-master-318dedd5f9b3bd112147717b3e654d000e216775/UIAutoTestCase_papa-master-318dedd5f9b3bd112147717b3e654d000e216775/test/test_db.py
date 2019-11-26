from common import sql_normal_csldata,sql_normal_csmall,sql_normal_csorder,sql_normal_cspown,sql_normal_cscuser
myms = sql_normal_csldata.mysql_connect(sql_normal_csldata.db_info)
myms2 = sql_normal_csmall.mysql_connect(sql_normal_csmall.db_info)
myms3 = sql_normal_csorder.mysql_connect(sql_normal_csorder.db_info)
myms4 = sql_normal_cspown.mysql_connect(sql_normal_cspown.db_info)

myms5 = sql_normal_cscuser.mysql_connect(sql_normal_cscuser.db_info)


b=myms.sql_exec_normal("select data_id from csl_data_bank_card_00 where app_user_id='191134'")
print (b)
b2=myms2.sql_exec_normal("INSERT INTO csm_user_address (user_id, name,phone,province,city)"
                         " VALUES ('2018072411392004050001343390', '吴越欣','RsxeVNONBDbnk63cH2p3hgA7SjTJ8EGl2lzvnOR51U87aK1imH/btOy6OQ0fNA3+k3v/Nh1qevvw\nN2mUAa3rszWRBs0nlJY4aTIsEXHV6vPy60Knwa0oFiLXlRDZwHA0xFBrsPn+qoWDdHY5cIQnJ9E0\nRYMz9hc0HQGkuXR2MO8=','湖北省','仙桃市')")
print (b2)
b3=myms3.sql_exec_normal("select id from cso_audit_log where audit_result='301'")
print (b3)
b4=myms4.sql_exec_normal("select  product_icon from csp_product where quota_min='1000'")
print (b4)

b5=myms5.sql_exec_normal("select  app_user_id from csc_user_msg where phone='8izDsmjveBr/IQMfWmzmvg=='")
print (b5)
# order_amount_num=myms.sql_assign_exec("")
# print(myms)