import pymysql
from DBUtils.PooledDB import PooledDB

from config.config import *


# 读连接池
class DBReaderManager(object):
    def __init__(self):
        super().__init__()
        self.pool = self.getPool()

    def getPool(self):
        pool = PooledDB(creator=pymysql, mincached=pool_min_cached, maxcached=pool_max_cached, host=host,
                          port=port, user=user_name, password=user_psd, db=db_name, use_unicode=True,
                          charset='utf8', maxshared=pool_max_shared, maxconnections=pool_max_connections,
                          cursorclass=pymysql.cursors.DictCursor)
        print('sql pools connect success')
        return pool

    def getConn(self):
        return self.pool.connection()


_db_reader = DBReaderManager()


# 获取读连接池中的一个数据库连接
def get_read_conn():
    return _db_reader.getConn()
