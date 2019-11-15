# 业务逻辑类
from model.user_dao import UserDao


class UserService:
    def __init__(self):
        super().__init__()
        self.user_dao = self.get_user_dao()

    def get_user_dao(self):
        user_dao = UserDao()
        return user_dao

    def db_query(self, data):
        print("Query Class")
        return self.user_dao.query_data(data)

    def query_resource(self):
        print('all resource')
        return self.user_dao.query_resource()

    def save_visit(self, user_info):
        return self.user_dao.save_visit(user_info)
