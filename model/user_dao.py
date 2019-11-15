import pymysql

from api.error_consts import ErrorConsts
from model.db_read_manager import get_read_conn
from model.db_write_manager import get_write_conn

# Version v1.0

class UserDao:
    def __init__(self):
        super().__init__()

    def query_data(self, data):
        conn = get_read_conn()
        cursor = conn.cursor()
        err = ErrorConsts()
        table_name = "user"
        sql = "select * from " + table_name + " where user_name = '" + \
            data['user_name'] + " and password = '" + data['password'] + "'"
        sql = "select * from " + table_name + " where user_name = %s and password = %s"
        print('sql = ', sql)
        print('user = {0}, psw = {1}'.format(data['user_name'], data['password']))
        try:
            count = cursor.execute(sql, (data['user_name'], data['password']))
            if count > 0:
                result = cursor.fetchall()
                # conn.commit()
                print('result = ', result)
                err.SUCCESS['data'] = result
                return err.SUCCESS
            else:
                err.Query_No_DATA['msg'] = "用户名或密码错误"
                return err.Query_No_DATA
        except:
            err.Query_No_DATA['msg'] = "服务器查询SQL错误,请稍候重试"
            return err.Query_No_DATA
        finally:
            if cursor is not None:
                cursor.close()
            # 不是真关闭,而是将连接放进池子
            conn.close()

    def query_resource(self):
        conn = get_read_conn()
        cursor = conn.cursor()
        rse = ErrorConsts()
        table_name = "resource"
        sql = "select * from " + table_name + " where status_id = 1"
        try:
            count = cursor.execute(sql)
            if count > 0:
                result = cursor.fetchall()
                # conn.commit()
                rse.SUCCESS['data'] = result
                return rse.SUCCESS
            else:
                rse.Query_No_DATA['msg'] = "无数据"
                return rse.Query_No_DATA
        except:
            rse.Query_No_DATA['msg'] = "查询异常"
            return rse.Query_No_DATA
        finally:
            if cursor is not None:
                cursor.close()
            # 不是真关闭,而是将连接放进池子
            conn.close()

    def save_visit(self, user_info):
        conn = get_write_conn()
        cursor = conn.cursor()
        err = ErrorConsts()
        table_name = "user"
        sql = "insert into " + table_name + "(user_name, regist_time, role_id) values (%s, %s, %s)"
        try:
            cursor.execute(sql, (user_info['user_name'], user_info['regist_time'], user_info['role_id']))
            cursor.execute('SELECT last_insert_id() as id')
            user_id = cursor.fetchone()
            user_id = user_id['id']
            conn.commit()
            err.SUCCESS['id'] = user_id
            return err.SUCCESS
        except:
            conn.rollback()
            return err.INSERT_DATA_ERROR
        finally:
            if cursor is not None:
                cursor.close()
            conn.close()
