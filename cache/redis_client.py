import tornadoredis


class RedisClient(tornadoredis.Client):
    def __init__(self, host, port, CONNECTION_POOL):
        super().__init__(host=host, port=port, connection_pool=CONNECTION_POOL)
        print("init redis client success")