from tornado.web import RequestHandler
from server import GradeServer
from tornado import gen
class GradeHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        tempcookie=self.get_argument('cookie','none')
        if tempcookie=='none':
            self.finish('cookienone')
        else:
            grade= GradeServer.grade_server(tempcookie)
            backinfo=yield grade
            if backinfo==None:
                self.finish("reqfailure")
            self.finish(backinfo[backinfo.index('['):backinfo.index(']')+1])
class OffsetGradeHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        tempcookie=self.get_argument('cookie','none')
        if tempcookie=='none':
            self.finish('cookienone')
        else:
            grade= GradeServer.offset_grade_server(tempcookie)
            backinfo=yield grade
            if backinfo==None:
                self.finish("reqfailure")
            self.finish(backinfo[backinfo.index('['):backinfo.index(']')+1])
