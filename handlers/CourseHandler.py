from tornado.web import RequestHandler
from tornado import gen
from server.CourseServer import courseServer
from tornado.httpclient import AsyncHTTPClient
from utils.json2url import JSON2URL
import json
from models.globaldata import term
from utils.IPProxyPool import Random_ProxyIP
AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")

class CourseHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        localcookie,info=self.get_argument('cookie','none'),self.get_argument('bjid','none')
        if localcookie =='none' or info=='none':
            self.finish("failure")
        res=courseServer(term,info,localcookie)
        result=yield res
        if result==None:
            self.finish("reqfailure")
        result=result[result.index('['):result.rfind(']')+1]
        backinfo=json.loads(result)
        mylist=[{} for i in range(7)]
        index=0
        for i in backinfo:
            index=index+1
            for j in i:
                mylist[int(j[3:])-1][str(index)]=i[j]
        self.finish(json.dumps(mylist))
class DepartmentHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        localcookie=self.get_argument('cookie','none')
        if localcookie =='none':
            self.finish("failure")
        req_url='http://jwgl.ntu.edu.cn/cjcx/Data/Basis/dep.aspx'
        header_req={
            'Accept': '*/*',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': localcookie,
            'Host': 'jwgl.ntu.edu.cn',
            'Referer': 'http://jwgl.ntu.edu.cn/cjcx/Main.aspx',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
            }
        ip_proxy,proxy_port=Random_ProxyIP()
        try:
            res = yield AsyncHTTPClient().fetch(req_url,method='GET',headers=header_req,proxy_host=ip_proxy,proxy_port=proxy_port,request_timeout=0.5)
        except Exception:
            try:
                res = yield AsyncHTTPClient().fetch(req_url,method='GET',headers=header_req)
            except Exception:
                self.finish("reqfailure")
        backinfo=res.body.decode('utf-8')
        self.finish(backinfo[backinfo.index('['):backinfo.rfind(']')+1])
class MajorHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        localcookie,depid=self.get_argument('cookie','none'),self.get_argument('depid','none')
        if localcookie=='none'or depid=='none':
            self.finish("failure")
        req_url='http://jwgl.ntu.edu.cn/cjcx/Data/Basis/class.aspx'
        req_header={
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': localcookie,
            'Host': 'jwgl.ntu.edu.cn',
            'Origin': 'http://jwgl.ntu.edu.cn',
            'Referer': 'http://jwgl.ntu.edu.cn/cjcx/Main.aspx',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        req_body={
            'depId':depid
        }        
        ip_proxy,proxy_port=Random_ProxyIP()
        try:
            res=yield AsyncHTTPClient().fetch(req_url,method='POST',headers=req_header,body=JSON2URL(req_body),proxy_host=ip_proxy,proxy_port=proxy_port,request_timeout=0.5)
        except Exception:
            try:
                res=yield AsyncHTTPClient().fetch(req_url,method='POST',headers=req_header,body=JSON2URL(req_body))
            except Exception:
                self.finish("reqfailure")
        backinfo=res.body.decode('utf-8')
        self.finish(backinfo[backinfo.index('['):backinfo.rfind(']')+1])