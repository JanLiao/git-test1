#coding=utf8


#以下是错误代码。

# 成功处理统一，SUCCESS.update({"data":di_result})
SUCCESS = {"code": 0, "msg": "ok"}


#通用数据库错误
ADD_DATA_ERROR = {'msg': "add data wrong", "code": 40001}
Delete_DATA_ERROR = {'msg': "delete data wrong", "code": 40002}
Update_DATA_ERROR = {'msg': "update data wrong", "code": 40003}
Query_No_DATA = {'msg': "query data wrong", "code": 40004,'data':[]}
#Query_No_DATA = {'msg': "query data wrong", "status": 40004}

#业务错误代码
DB_Exists_ERROR = {'msg': "[ERROR]This DATA exists!", "code": 40011}

TICKET_PARAM_ERROR = {'msg': "ticket param is None", "code": 41001}
TICKET_DATA_ERROR = {'msg': "ticket is not val", "code": 41002}