import json

import redis
from tornado.web import RequestHandler
# from api.error_code import TICKET_DATA_ERROR, TICKET_PARAM_ERROR
# redis_client = redis.Redis(host='10.22.19.21', port=6379)
from api.error_consts import ErrorConsts
from cache.redis_pool import get_redis, rdp

# from config.config import redis_port, redis_host

# redis_client = redis.Redis(host=redis_host, port=redis_port)
redis_client = get_redis()
# redis_client = redis.StrictRedis(connection_pool=rdp)

class ValidationHandler(RequestHandler):
    def get(self):
        ticket = self.get_argument('ticket', default='')
        print('login ticket = ', ticket)
        err = ErrorConsts()
        if ticket != '':
            user_info = redis_client.get(ticket)
            if user_info is not None:
                print("get user_info msg = ", user_info)
                # 查询到就删除该ticket
                redis_client.delete(ticket)
                user_dict = json.loads(user_info)
                # print('user_dict', user_dict)
                self.write(user_dict)
            else:
                self.write(err.TICKET_DATA_ERROR)
        else:
            self.write(err.TICKET_PARAM_ERROR)