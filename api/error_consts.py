class ErrorConsts:
    SUCCESS = {'code': 0, 'msg': 'ok'}

    def __init__(self):
        super().__init__()
        self.SUCCESS = {'code': 0, 'msg': 'ok'}
        self.RESULT = {"code": 0, "msg": "ok"}
        self.INSERT_DATA_ERROR = {"code": 40015, "msg": "游客登入失败,请稍后重试!"}
        self.PARAM_DATA_ERROR = {"code": 40014, "msg": "ok"}

        self.ADD_DATA_ERROR = {'msg': "add data wrong", "code": 40001}
        self.Delete_DATA_ERROR = {'msg': "delete data wrong", "code": 40002}
        self.Update_DATA_ERROR = {'msg': "update data wrong", "code": 40003}
        self.Query_No_DATA = {'msg': "query data wrong", "code": 40004, 'data': []}
        # Query_No_DATA = {'msg': "query data wrong", "status": 40004}

        # 业务错误代码
        self.DB_Exists_ERROR = {'msg': "[ERROR]This DATA exists!", "code": 40011}

        self.TICKET_PARAM_ERROR = {'msg': "ticket param is None", "code": 41001}
        self.TICKET_DATA_ERROR = {'msg': "ticket is not val", "code": 41002}