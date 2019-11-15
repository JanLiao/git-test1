import tornado.web
import json
# from model.db_control import db_control
from config.config import *
from api.error_code import *
import time
import datetime
import copy
import os,sys

# the_db = db_control(host, port, db_name, user_name, user_psd)

class PostDataHandler(tornado.web.RequestHandler):
    def post(self):
        body = json.loads(self.request.body)   #解析数据
        
        if body['TYPE'] == "REGISTER":  #处理登记报
            self.handle_register(body)
        elif body['TYPE'] == "COMMAND": #处理命令报
            self.handle_command(body)
        elif body['TYPE'] == "DATA":    #处理数据报
            self.handle_data(body)        

        return self.write("OK")

    def handle_command(self, reg_data):  #处理登记报
        #增加日期
        current_time = datetime.datetime.now()
        t = copy.deepcopy(reg_data)
        t["DATE"] = current_time.strftime("%Y-%m-%d")      

        #增加时间
        t["TIME"] = current_time.strftime("%H:%M")        

        #写入数据库
        # the_db.db_add(t)

    def handle_data(self, data):
        return 1
        