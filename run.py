from tornado.web import Application
from os.path import sys,dirname,abspath
import tornado.ioloop
import time
import sys
from handlers.LoginHandler import LoginHandler
from handlers.LoginHandler import LoginWXHander
from handlers.GradeHandler import GradeHandler
# 添加系统路径变量
dirpath=dirname(abspath(__file__))
sys.path.append(dirpath)
if __name__ == "__main__":
    app = tornado.web.Application([(r'/login',LoginHandler),
                                    (r'/login_wx',LoginWXHander),
                                    (r'/grade',GradeHandler)])
    #绑定一个监听端口
    app.listen(8080)
    #启动web程序，开始监听端口的连接
    tornado.ioloop.IOLoop.current().start()
# 注意json.dumps(),这个不能够正确给出body