import base64

from model.db_control import db_control

if __name__ ==  '__main__':
    # the_db = db_control("10.22.18.26",3307, "db_attendance","root","cvte2018")
    the_db = db_control("127.0.0.1", 3306, "ai_data", "root", "123456")
    # the_db = db_control("172.17.165.20",3306, "TESTDB","root","admin")
    
    #add result data
    the_db.result_table.clear_data()
    the_db.result_add({"CLASS":"五年一班", "IPADDR":"172.17.17.11", "F_TIME":"2019-05-30 9:00:00", "TOTAL_NUM":"20", "REAL_NUM":"17","PERSONS":"王一,李一,张一" })
    the_db.result_add({"CLASS":"五年一班", "IPADDR":"172.17.17.11", "F_TIME":"2019-05-30 10:00:00", "TOTAL_NUM":"20", "REAL_NUM":"19","PERSONS":"张一" })
    the_db.result_add({"CLASS":"五年一班", "IPADDR":"172.17.17.11", "F_TIME":"2019-05-30 11:00:00", "TOTAL_NUM":"20", "REAL_NUM":"20","PERSONS":"" })
    the_db.result_add({"CLASS":"五年一班", "IPADDR":"172.17.17.11", "F_TIME":"2019-05-31 9:00:00", "TOTAL_NUM":"20", "REAL_NUM":"18","PERSONS":"王一,李一" })
    the_db.result_add({"CLASS":"五年一班", "IPADDR":"172.17.17.11", "F_TIME":"2019-05-31 10:00:00", "TOTAL_NUM":"20", "REAL_NUM":"19","PERSONS":"张一" })
    the_db.result_add({"CLASS":"五年一班", "IPADDR":"172.17.17.11", "F_TIME":"2019-05-31 11:00:00", "TOTAL_NUM":"20", "REAL_NUM":"20","PERSONS":"" })
    the_db.result_add({"CLASS":"五年一班", "IPADDR":"172.17.17.11", "F_TIME":"2019-06-01 9:00:00", "TOTAL_NUM":"20", "REAL_NUM":"18","PERSONS":"王一,李一" })
    the_db.result_add({"CLASS":"五年一班", "IPADDR":"172.17.17.11", "F_TIME":"2019-06-01 10:00:00", "TOTAL_NUM":"20", "REAL_NUM":"19","PERSONS":"张一" })
    the_db.result_add({"CLASS":"五年一班", "IPADDR":"172.17.17.11", "F_TIME":"2019-06-01 11:00:00", "TOTAL_NUM":"20", "REAL_NUM":"20","PERSONS":"" })
    
    the_db.result_add({"CLASS":"五年二班", "IPADDR":"172.17.17.12", "F_TIME":"2019-05-30 9:00:00", "TOTAL_NUM":"20", "REAL_NUM":"18","PERSONS":"王二,李二" })
    the_db.result_add({"CLASS":"五年二班", "IPADDR":"172.17.17.12", "F_TIME":"2019-05-30 10:00:00", "TOTAL_NUM":"20", "REAL_NUM":"19","PERSONS":"张二" })
    the_db.result_add({"CLASS":"五年二班", "IPADDR":"172.17.17.12", "F_TIME":"2019-05-30 11:00:00", "TOTAL_NUM":"20", "REAL_NUM":"20","PERSONS":"" })
    the_db.result_add({"CLASS":"五年二班", "IPADDR":"172.17.17.12", "F_TIME":"2019-05-31 9:00:00", "TOTAL_NUM":"20", "REAL_NUM":"18","PERSONS":"王二,李二" })
    the_db.result_add({"CLASS":"五年二班", "IPADDR":"172.17.17.12", "F_TIME":"2019-05-31 10:00:00", "TOTAL_NUM":"20", "REAL_NUM":"19","PERSONS":"张二" })
    the_db.result_add({"CLASS":"五年二班", "IPADDR":"172.17.17.12", "F_TIME":"2019-05-31 11:00:00", "TOTAL_NUM":"20", "REAL_NUM":"20","PERSONS":"" })
    the_db.result_add({"CLASS":"五年二班", "IPADDR":"172.17.17.12", "F_TIME":"2019-06-01 9:00:00", "TOTAL_NUM":"20", "REAL_NUM":"17","PERSONS":"王二,李二,张二" })
    the_db.result_add({"CLASS":"五年二班", "IPADDR":"172.17.17.12", "F_TIME":"2019-06-01 10:00:00", "TOTAL_NUM":"20", "REAL_NUM":"19","PERSONS":"张二" })
    the_db.result_add({"CLASS":"五年二班", "IPADDR":"172.17.17.12", "F_TIME":"2019-06-01 11:00:00", "TOTAL_NUM":"20", "REAL_NUM":"20","PERSONS":"" })
    
    the_db.result_add({"CLASS":"五年三班", "IPADDR":"172.17.17.13", "F_TIME":"2019-05-30 9:00:00", "TOTAL_NUM":"20", "REAL_NUM":"17","PERSONS":"王三,李三,张三" })
    the_db.result_add({"CLASS":"五年三班", "IPADDR":"172.17.17.13", "F_TIME":"2019-05-30 10:00:00", "TOTAL_NUM":"20", "REAL_NUM":"18","PERSONS":"张三,王三" })
    the_db.result_add({"CLASS":"五年三班", "IPADDR":"172.17.17.13", "F_TIME":"2019-05-30 11:00:00", "TOTAL_NUM":"20", "REAL_NUM":"19","PERSONS":"李三" })
    the_db.result_add({"CLASS":"五年三班", "IPADDR":"172.17.17.13", "F_TIME":"2019-05-31 9:00:00", "TOTAL_NUM":"20", "REAL_NUM":"18","PERSONS":"王三,李三" })
    the_db.result_add({"CLASS":"五年三班", "IPADDR":"172.17.17.13", "F_TIME":"2019-05-31 10:00:00", "TOTAL_NUM":"20", "REAL_NUM":"19","PERSONS":"张三" })
    the_db.result_add({"CLASS":"五年三班", "IPADDR":"172.17.17.13", "F_TIME":"2019-05-31 11:00:00", "TOTAL_NUM":"20", "REAL_NUM":"20","PERSONS":"" })
    the_db.result_add({"CLASS":"五年三班", "IPADDR":"172.17.17.13", "F_TIME":"2019-06-01 9:00:00", "TOTAL_NUM":"20", "REAL_NUM":"18","PERSONS":"王三,李三" })
    the_db.result_add({"CLASS":"五年三班", "IPADDR":"172.17.17.13", "F_TIME":"2019-06-01 10:00:00", "TOTAL_NUM":"20", "REAL_NUM":"19","PERSONS":"张三" })
    the_db.result_add({"CLASS":"五年三班", "IPADDR":"172.17.17.13", "F_TIME":"2019-06-01 11:00:00", "TOTAL_NUM":"20", "REAL_NUM":"20","PERSONS":"" })
    
    #====================
    #class test
    the_db.class_table.clear_data()
    the_db.class_add({"CLASS":"五年一班", "IPADDR":"172.17.17.11", "USER_NAME":"admin", "USER_PSW":"123456"})
    the_db.class_add({"CLASS":"五年二班", "IPADDR":"172.17.17.12", "USER_NAME":"admin", "USER_PSW":"123456"})
    the_db.class_add({"CLASS":"五年三班", "IPADDR":"172.17.17.13", "USER_NAME":"admin", "USER_PSW":"123456"})
        
    print(the_db.class_query())
    #====================
    #person test
    the_db.person_table.clear_data()
    with open("t1.jpg","rb") as f:
        img_base64 = base64.b64encode(f.read())
    the_db.person_add({"CLASS":"五年一班", "NAME":"张一","img_base64":img_base64})
    the_db.person_add({"CLASS":"五年一班", "NAME":"王一","img_base64":img_base64})
    the_db.person_add({"CLASS":"五年一班", "NAME":"李一","img_base64":img_base64})
    the_db.person_add({"CLASS":"五年二班", "NAME":"张二","img_base64":img_base64})
    the_db.person_add({"CLASS":"五年二班", "NAME":"王二","img_base64":img_base64})
    the_db.person_add({"CLASS":"五年二班", "NAME":"李二","img_base64":img_base64})
    the_db.person_add({"CLASS":"五年三班", "NAME":"张三","img_base64":img_base64})
    the_db.person_add({"CLASS":"五年三班", "NAME":"王三","img_base64":img_base64})
    the_db.person_add({"CLASS":"五年三班", "NAME":"李三","img_base64":img_base64})
        
    #================================
    #config test
    the_db.config_init()
    print(the_db.config_query())
    the_db.config_update({"TYPE":"work_day", "CONTENT":"monday"})
    print(the_db.config_query())
    
    
    the_db.close_db()