from tornado.web import RequestHandler
from tornado import gen
from server.CourseServer import courseServer
class CourseHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        localcookie,info,term=self.get_argument('cookie','none'),self.get_argument('bjid','none'),self.get_argument('term','none')
        res=courseServer(term,info,localcookie)
        result=yield res
        self.write(result[result.index('['):result.index(']')+1])

class DepartmentHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        print('asd')
class MajorHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        print('asd')