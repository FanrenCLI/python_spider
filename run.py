from tornado.web import Application
from os.path import sys,dirname,abspath
import threading
import tornado.ioloop
import time
import sys
from handlers.LoginHandler import *
from handlers.GradeHandler import *
from handlers.CourseHandler import *
from handlers.ChangePwdHandler import *
from handlers.PubCourseHandler import *
from handlers.ChangeMajorHandler import *
# 添加系统路径变量
dirpath=dirname(abspath(__file__))
sys.path.append(dirpath)
if __name__ == "__main__":
    app = Application([(r'/login',LoginHandler),(r'/login_wx',LoginWXHander),
                        (r'/grade',GradeHandler),(r'/course',CourseHandler),
                        (r'/depart',DepartmentHandler),(r'/major',MajorHandler),
                        (r'/offsetgrade',OffsetGradeHandler),(r'/changepwd',ChangePwdHandler),
                        (r'/gxk',PubCourseHandler),(r'/ybgxk',YBPubCourseHandler),
                        (r'/deletegxk',DeletePubCourseHandler),(r'/submitgxk',SubmitPubCourseHandler),
                        (r'/changemajor',ChangeMajorHandler),(r'/ybmajor',YBMajorHandler),
                        (r'/changemajorgrade',ChangeMajorGradeHandler)])
    #绑定一个监听端口
    app.listen(8080)
    #启动web程序，开始监听端口的连接
    tornado.ioloop.IOLoop.current().start()