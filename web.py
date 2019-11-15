import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from api import *
define("port", default=8889, help="run on the given port", type=int)
current_path = os.path.dirname(__file__)    # 上一层目录

def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application(routeList,
                                          template_path=os.path.join(current_path, 'templates'),
                                          static_path=os.path.join(current_path, 'static'),
                                          debug=True,)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()