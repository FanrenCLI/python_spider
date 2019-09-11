from tornado.web import Application
from os.path import sys,dirname,abspath
import threading
import tornado.ioloop
import time
import sys
from utils.IPProxyPool import loop1,loop2
from models.globaldata import ip_proxy_list
from handlers.LoginHandler import *
from handlers.GradeHandler import *
from handlers.CourseHandler import *
from handlers.ChangePwdHandler import *
from handlers.PubCourseHandler import *
from handlers.ChangeMajorHandler import *
# 添加系统路径变量
dirpath=dirname(abspath(__file__))
sys.path.append(dirpath)
class test(tornado.web.RequestHandler):
    def get(self):
        self.finish(str(ip_proxy_list))
if __name__ == "__main__":
    threading.Thread(target=loop1).start()
    threading.Thread(target=loop2).start()
    app = Application([(r'/login',LoginHandler),(r'/login_wx',LoginWXHander),
                        (r'/grade',GradeHandler),(r'/course',CourseHandler),
                        (r'/depart',DepartmentHandler),(r'/major',MajorHandler),
                        (r'/offsetgrade',OffsetGradeHandler),(r'/changepwd',ChangePwdHandler),
                        (r'/gxk',PubCourseHandler),(r'/ybgxk',YBPubCourseHandler),
                        (r'/deletegxk',DeletePubCourseHandler),(r'/submitgxk',SubmitPubCourseHandler),
                        (r'/changemajor',ChangeMajorHandler),(r'/ybmajor',YBMajorHandler),
                        (r'/changemajorgrade',ChangeMajorGradeHandler),(r'/test',test)])
    #绑定一个监听端口
    app.listen(8080)
    #启动web程序，开始监听端口的连接
    tornado.ioloop.IOLoop.current().start()