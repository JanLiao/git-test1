from api.ValidationHandler import ValidationHandler
from api.LoginHandler import *
from api.LoginHandler import MainHandler
from api.route import *

#路径匹配
routeList = [(r"/login", LoginHandler),
             (r'/logout', LogoutHandler),
             (r"/test", MainHandler),
             (r"/valticket", ValidationHandler),
             (r'/visit/index', VisitIndexHandler),
            ]