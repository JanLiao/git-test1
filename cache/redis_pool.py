import redis

from config.config import redis_port, redis_host, redis_max_connections

# 使用单例生成一个Redis连接池
class RedisPool:
    def __init__(self):
        super().__init__()
        self.rdp = self.connect_redis()

    def connect_redis(self):
        print('redis pools init success')
        return redis.ConnectionPool(max_connections=redis_max_connections, host=redis_host, port=redis_port)


redis_pools = RedisPool()
rdp = redis_pools.rdp


def get_redis():
    rdp1 = redis_pools.rdp
    return redis.Redis(connection_pool=rdp1)

# rdc = redis.StrictRedis(connection_pool=rdp)

# print(rdc.hget('3:label:1:1', 'annotation'))