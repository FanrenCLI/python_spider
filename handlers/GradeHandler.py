from tornado.web import RequestHandler
from server import GradeServer
from tornado import gen
class GradeHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        tempcookie=self.get_argument('cookie','none')
        if tempcookie=='none':
            self.write('cookienone')
        else:
            grade= GradeServer.grade_server(tempcookie)
            backinfo=yield grade
            self.write(backinfo[backinfo.index('['):backinfo.index(']')+1])
class OffsetGradeHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        tempcookie=self.get_argument('cookie','none')
        if tempcookie=='none':
            self.write('cookienone')
        else:
            grade= GradeServer.offset_grade_server(tempcookie)
            backinfo=yield grade
            self.write(backinfo[backinfo.index('['):backinfo.index(']')+1])
