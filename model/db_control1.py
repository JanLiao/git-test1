#coding:utf8

import base64
import os
import shutil
import sys
sys.path.append('../')
from api.error_code import *
import pymysql
import pandas as pd
import numpy as np

from model.operate_table import *

def get_date(ori_date):
    real_date = ori_date.split(' ')[0]
    return real_date

class db_control():
    def __init__(self, host,port,db_name, user_name, user_psd):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.user_name = user_name
        self.user_psd = user_psd
        
        self.db = self.connect_db()

        self.db_table = operate_table(self.db, "user")
        # self.db_table = operate_table(self.db,"flow_test",{"TYPE":20,"ID":20,"APPID":20, "VERSION":20, "IPADDR":20, "DATE":100,"TIME":100,"TEXT1":20, "TEXT2":255, "TEXT3":255, "TEXT4":255, "TEXT5":255, "TEXT6":255, "TEXT7":255, "TEXT8":255,"TEXT9":255,"TEXT10":255,"TEXT11":255,"TEXT12":255,"TEXT13":255,"TEXT14":255,"TEXT15":255,"TEXT16":255,"TEXT17":255,"TEXT18":255,"TEXT19":255,"TEXT20":255,"COMMENT":255})
        
    def connect_db(self):
        try: #connect to database
            db = pymysql.connect(host=self.host,port=self.port,user=self.user_name, passwd=self.user_psd, db=self.db_name, charset='utf8' ,cursorclass = pymysql.cursors.DictCursor)
            print("[OK]Connect database %s Succeed! " % self.db_name)
        except Exception as err:
            print(err)
            print("[ERROR]Connect database %s ERROR! " % self.db_name)
        return db
            
    def close_db(self):
        self.db.close()

    def conn_test(self):
        try:
            print('conn_test ping------>')
            self.db.ping(reconnect=True)
        except:
            print('connect closed------')
            self.connect_db()
    
         
    #------------------CLASS---------------------        
    def db_query(self, data={}):
        # return all class for default
        print("Query Class")
        return self.db_table.query_data(data)

    def query_resource(self):
        print('query resource')
        return self.db_table.query_resource()
       
    def db_add(self, data):
        # data is a dict, ex:
        # {"CLASS":"class3,grade2", "IPADDR":"172.17.15.12"})
        print(self.db_query(data))
        
        if self.db_query(data) != Query_No_DATA:
            return DB_Exists_ERROR

        self.db_table.add_data(data)
        return SUCCESS
        
    def db_delete(self,data):
        # delete all data fit the filter
        return self.db_table.delete_data(data)
        
    def db_update(self,data):
        # change other attribute according class
        data_ori = {"ID": data["ID"],"TYPE":data["TYPE"]}
        return self.db_table.update_data(data_ori, data)
        