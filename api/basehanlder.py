from tornado.web import RequestHandler

class BaseHandler(RequestHandler):
    def get(self):
        pass