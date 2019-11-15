#coding:utf8
import json

import pymysql

from api.error_code import *

def dict2list(indata):
    key_list = []
    data_list = []
    for every_key in indata:      
        if indata[every_key] != "":    #remove undefined data 
            key_list.append(str(every_key))
            data_list.append(str(indata[every_key]))
    return key_list, data_list
        
class operate_table():
    def __init__(self,db,table_name):
        self.db = db
        self.cursor = db.cursor()
        self.table = table_name
        # table_i,table_d = dict2list(table_info)
        #
        # sql = "CREATE TABLE " + table_name + "("
        #
        # for i in range(len(table_i)):
        #     sql += table_i[i] + " CHAR(" + str(table_d[i]) + ")"
        #     if i < len(table_i)-1:
        #         sql += ','
        #
        # sql += ")"
        #
        # try:  #create table result
        #     self.cursor.execute(sql)
        #     print("[OK]Create table %s Succeed! " % table_name)
        # except:
        #     print("[INFO]Table %s already exist OR paramter is invalid ! " % table_name)
    

    
    def add_data(self,data):
    # insert data to database
    # input: dict
        key_list, data_list = dict2list(data)
        sql = "INSERT INTO " + self.table + "(" + ','.join(key_list) + ") VALUES ('" + "','".join(data_list) + "')" 
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return SUCCESS
        except:
            print("add data wrong")
            self.db.rollback()
            return ADD_DATA_ERROR

    def delete_data(self,data):
        key_list, data_list = dict2list(data)
        sql = "DELETE FROM " + self.table + " WHERE " 
        for i in range(len(key_list)):
            sql += key_list[i] + "='" + data_list[i] + "'"
            if i < len(key_list) - 1:
                sql += " and "
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return SUCCESS
        except:
            print("delete data wrong")
            self.db.rollback()
            return Delete_DATA_ERROR

    def query_resource(self):
        sql = "select * from resource where status_id = 1"
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            # print('rr=', results)
            if len(results) != 0:
                SUCCESS.update({"data": results})
                return SUCCESS
            return Query_No_DATA
        except:
            self.db.rollback()
            return Query_No_DATA
    
    def query_data(self, data):
        key_list, data_list = dict2list(data)
        sql = "SELECT * FROM " + self.table

        if len(key_list) > 0:
            sql += " WHERE "
            for i in range(len(key_list)):
                sql += key_list[i] + "='" + data_list[i] + "'"
                if i < len(key_list) - 1:
                    sql += " and "
        print('sql = ', sql)
        self.db.ping(reconnect=True)
        # self.conn_test()
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            self.db.commit()
            print('results = ', results)
            if len(results) != 0:
                SUCCESS.update({"data": results})
                return SUCCESS
            return Query_No_DATA
        except:
            self.db.rollback()
            return Query_No_DATA
            
    def update_data(self, data_ori, data_upd):
        key_list_ori, data_list_ori = dict2list(data_ori)
        key_list_upd, data_list_upd = dict2list(data_upd)
        sql = "UPDATE " + self.table + " SET "
        for i in range(len(key_list_upd)):
            sql += key_list_upd[i] + "='" + data_list_upd[i] + "'"
            if i < len(key_list_upd) - 1:
                sql += ","
        sql += " WHERE "
        for i in range(len(key_list_ori)):
            sql += key_list_ori[i] + "='" + data_list_ori[i] + "'"
            if i < len(key_list_ori) - 1:
                sql += " and "
        #print (sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return SUCCESS
        except:
            self.db.rollback()
            return Update_DATA_ERROR
            
    def clear_data(self):
        sql = "DELETE FROM " + self.table
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return 1
        except:
            self.db.rollback()
            return 0
  
if __name__ == "__main__":
    db = pymysql.connect("localhost", "root", "123456", "ai_data", charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    print(db)

    op_table_result = operate_table(db, "RESULT", {"CLASS": 20, "IPADDR": 20, "F_TIME": 40, "TOTAL_NUM": 20, "REAL_NUM": 20, "PERSONS": 255})
    
    op_table_result.clear_data()

    u = {"class": '三年五班', "IPADDR": "172.17.17.12", "F_TIME": "2019-05-30 18:30:24", "TOTAL_NUM": "20", "REAL_NUM": "10","PERSONS": "AAA,BBB" }
    op_table_result.add_data(u)
    print(op_table_result.query_data(u))
    
    data_ori = {"class": "class2,grade5", "IPADDR": "172.17.17.12"}
    data_upd = {"IPADDR": "172.17.17.222", "TOTAL_NUM": "55"}
    op_table_result.update_data(data_ori, data_upd)
    print(op_table_result.query_data(u))
    print(op_table_result.query_data(u))
    
    op_table_result.delete_data({"class": "class2,grade5"})
    print(op_table_result.query_data(u))

    db.close()
    print("over")
