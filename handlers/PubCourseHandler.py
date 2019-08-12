from tornado.web import RequestHandler
from tornado import gen
from server import PubCourseServer

class PubCourseHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        localcookie,term=self.get_argument('cookie','none'),self.get_argument('term','none')
        if localcookie =='none' or term=='none':
            self.write("failure")
        res = PubCourseServer.gxk_server(term,localcookie,'gxk')
        backinfo= yield res
        self.write(backinfo[backinfo.index('['):backinfo.rfind(']')+1])
# {bj:'',bz:'',jsxm:'',kch:'',kcmc:'',oid:'',sksj:'',xf:'',xs:'',xxrs:'',xxtj:''}
class YBPubCourseHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        localcookie,term=self.get_argument('cookie','none'),self.get_argument('term','none')
        if localcookie =='none' or term=='none':
            self.write("failure")
        res = PubCourseServer.gxk_server(term,localcookie,'ybgxk')
        backinfo= yield res
        self.write(backinfo[backinfo.index('['):backinfo.rfind(']')+1])
class SubmitPubCourseHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        jxrwid,term=self.get_argument('jxrwid','none'),self.get_argument('term','none')
        localcookie=self.get_argument('cookie','none')
        if jxrwid=='none'or term=='none':
            self.write("failure")
        res=PubCourseServer.submit_gxk_server(localcookie,jxrwid,term)
        backinfo=yield res
        if backinfo.find('success:true')!=-1:
            self.write('success')
        else:
            self.write('failure')
class DeletePubCourseHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        oid,localcookie=self.get_argument('oid','none'),self.get_argument('cookie','none')
        if oid=='none' or localcookie=='none':
            self.write("failure")
        res=PubCourseServer.delete_gxk_server(localcookie,oid)
        backinfo= yield res
        if backinfo.find('success:true')!=-1:
            self.write('success')
        else:
            self.write('failure')