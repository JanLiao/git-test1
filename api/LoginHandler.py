import datetime
import json
import time

import redis
import tornado.gen
# import tornadoredis
from tornado.web import RequestHandler

from api.error_consts import ErrorConsts
from cache.redis_pool import get_redis
from config.config import host, port, db_name, user_name, user_psd, expire_time, redis_port, redis_host, rdt_url, \
    url_port
from model.user_service import UserService
# from redis.redis_client import RedisClient
# from redis.redis_config import max_connections, wait_for_available, redis_port, redis_host

# from redis.redis_config import max_connections, wait_for_available

# CONNECTION_POOL = tornadoredis.ConnectionPool(max_connections=max_connections, wait_for_available=wait_for_available)
# CONNECTION_POOL.connection_kwargs['host'] = redis_host
# CONNECTION_POOL.connection_kwargs['port'] = redis_port
# from redis.redis_config import redis_host, redis_port
from utils.DateEncoder import DateEncoderUtil
from utils.TicketID import create_ticket_id
from utils.sessionID import create_session_id
from utils.sql_filter import params_filter
from api.error_code import SUCCESS

# the_db = db_control(host, port, db_name, user_name, user_psd)
user_service = UserService()
# redis_cli = tornadoredis.Client(connection_pool=tornadoredis.ConnectionPool(max_connections=max_connections, wait_for_available=wait_for_available),
#                                 host=redis_host, port=redis_port)

# redis_cli = RedisClient(host=redis_host, port=redis_port, connection_pool=CONNECTION_POOL)

# redis_cli = tornadoredis.Client(selected_db=1, connection_pool=CONNECTION_POOL)
# redis_client = redis.Redis(host='10.22.19.21', port=6379)
# redis_client = redis.Redis(host=redis_host, port=redis_port)
redis_client = get_redis()


class LoginHandler(RequestHandler):
    # @tornado.web.asynchronous
    # @tornado.gen.engine
    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', '*')

    def post(self):
        redirect_url = self.get_argument("redirect", default='')
        if redirect_url == '':
            error_msg = {'code': 10000, 'msg': "非法登录!"}
            self.write(error_msg)
        else:
            print('post login redirect url = ', redirect_url)
            user_name = self.get_argument('user_name', default='')
            password = self.get_argument('password', default='')
            user_name = params_filter(user_name)
            password = params_filter(password)
            body_data = {'user_name': user_name, 'password': password}
            # body_data = json.loads(self.request.body)
            print(body_data)
            # cookie_id = self.get_cookie("sso_id")
            query_result1 = user_service.db_query(body_data)
            print('query result = ', query_result1)
            query_result = {}
            query_result['msg'] = query_result1['msg']
            query_result['code'] = query_result1['code']
            query_result['data'] = query_result1['data']
            if query_result1['code'] == 0:
                resource_data = user_service.query_resource()
                if resource_data['code'] == 0:
                    query_result['resource'] = resource_data['data']
                # print('query resource result data = ', query_result)
                sso_id = create_session_id()
                self.set_cookie(name='sso_id', value=sso_id)
                print('login sso_id = ', sso_id)
                save_user_info = json.dumps(query_result, cls=DateEncoderUtil)
                # print('query result save_user_info = ', save_user_info)
                redis_client.set(name=sso_id, value=save_user_info, px=expire_time)
                ticket = create_ticket_id()
                print('start generate login ticket = ', ticket)
                redis_client.set(name=ticket, value=save_user_info, px=expire_time)
                # self.set_header("Access-Control-Allow-Origin", "*")
                # self.set_header("Access-Control-Allow-Headers", "x-requested-with")
                # self.set_header('Access-Control-Allow-Methods', '*')
                # self.set_header("Access-Control-Allow-Headers",
                #                 "access-control-allow-origin,authorization,content-type")
                err = ErrorConsts()
                err.SUCCESS['url'] = redirect_url + "?ticket=" + ticket
                err.SUCCESS['data'] = ''
                print(err.SUCCESS)
                self.write(err.SUCCESS)
            else:
                self.write({'code': 40004, 'msg': '用户名或密码错误!'})
                # self.write(query_result)

    def get(self):
        redirect_url = self.get_argument("redirect", default='')
        print(redirect_url)
        cookie_id = self.get_cookie("sso_id")
        if cookie_id is not None:
            print("cookie show already login ", cookie_id)
            sso_info = redis_client.get(cookie_id)
            print('sso_info', sso_info)
            if sso_info is not None:
                print("redis show already login ")
                self.set_cookie(name='sso_id', value=create_session_id(), domain="sso.com")
                ticket = create_ticket_id()
                # 刷新
                redis_client.set(name=ticket, value=sso_info, px=expire_time)
                self.redirect(redirect_url + "?ticket=" + ticket)
            else:
                self.render("login.html", redirect_url=redirect_url)
        else:
            self.render("login.html", redirect_url=redirect_url)
        # redirect_url = self.get_argument("redirect")
        # print(redirect_url)
        # self.redirect("https://" + redirect_url, permanent=True, status=302)

class MainHandler(RequestHandler):
    def get(self):
        redirect_url = 'jan_test'
        self.render('login.html', redirect_url=redirect_url)
        # self.write("hello world")


class LogoutHandler(RequestHandler):
    def get(self):
        cookie_id = self.get_argument('sso_id')
        result_code = {'code': 0, 'msg': '登出成功!'}
        if cookie_id is not None:
            sso_info = redis_client.get(cookie_id)
            print('sso_info', sso_info)
            if sso_info is not None:
                redis_client.delete(cookie_id)
                self.write(result_code)
            else:
                result_code['msg'] = 'Redis不存在数据,登出成功!'
                self.write(result_code)
        else:
            result_code['msg'] = 'cookie不存在,登出成功!'
            self.write(result_code)

class VisitIndexHandler(RequestHandler):
    def get(self):
        redirect_url = self.get_argument("redirect", default='')
        if redirect_url == '':
            ticket = create_ticket_id()
            self.save_to_redis(ticket)
            error_msg = {'code': 0, 'msg': "ok", 'url': rdt_url + ":" + str(url_port)}
            self.write(error_msg)
        else:
            ticket = create_ticket_id()
            self.save_to_redis(ticket)
            err = ErrorConsts()
            err.SUCCESS['url'] = redirect_url + "?ticket=" + ticket
            err.SUCCESS['data'] = ''
            print(err.SUCCESS)
            self.write(err.SUCCESS)

    def save_to_redis(self, ticket):
        data = []
        user_info = {
            "user_name": "游客_" + str(int(time.time())),
            "regist_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "role_id": 2
        }
        id_result = user_service.save_visit(user_info)
        user_info['id'] = id_result['id']
        data.append(user_info)
        save_user_info = {
            "code": 0,
            "msg": "游客访问",
            "data": data
        }
        resource_data = user_service.query_resource()
        if resource_data['code'] == 0:
            save_user_info['resource'] = resource_data['data']
        save_user_info = json.dumps(save_user_info, cls=DateEncoderUtil)
        sso_id = create_session_id()
        self.set_cookie(name='sso_id', value=sso_id)
        print('login sso_id = ', sso_id)
        # print('query result save_user_info = ', save_user_info)
        redis_client.set(name=sso_id, value=save_user_info, px=expire_time)
        print('start generate login ticket = ', ticket)
        redis_client.set(name=ticket, value=save_user_info, px=expire_time)
