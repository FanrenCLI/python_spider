from tornado.web import RequestHandler
from tornado import gen
from server import PubCourseServer
from models.globaldata import term
class PubCourseHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        localcookie=self.get_argument('cookie','none')
        if localcookie =='none' :
            self.finish("failure")
        res = PubCourseServer.gxk_server(term,localcookie,'gxk')
        backinfo= yield res
        if backinfo==None:
            self.finish("reqfailure")
        self.finish(backinfo[backinfo.index('['):backinfo.rfind(']')+1])
class YBPubCourseHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        localcookie=self.get_argument('cookie','none')
        if localcookie =='none':
            self.finish("failure")
        res = PubCourseServer.gxk_server(term,localcookie,'ybgxk')
        backinfo= yield res
        if backinfo==None:
            self.finish("reqfailure")
        self.finish(backinfo[backinfo.index('['):backinfo.rfind(']')+1])
class SubmitPubCourseHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        jxrwid,localcookie=self.get_argument('jxrwid','none'),self.get_argument('cookie','none')
        if jxrwid=='none' or localcookie=='none':
            self.finish("failure")
        res=PubCourseServer.submit_gxk_server(localcookie,jxrwid,term)
        backinfo=yield res
        if backinfo==None:
            self.finish("reqfailure")
        if backinfo.find('success:true')!=-1:
            self.finish('success')
        else:
            self.finish('failure')
class DeletePubCourseHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        oid,localcookie=self.get_argument('oid','none'),self.get_argument('cookie','none')
        if oid=='none' or localcookie=='none':
            self.finish("failure")
        res=PubCourseServer.delete_gxk_server(localcookie,oid)
        backinfo= yield res
        if backinfo==None:
            self.finish("reqfailure")
        if backinfo.find('success:true')!=-1:
            self.finish('success')
        else:
            self.finish('failure')