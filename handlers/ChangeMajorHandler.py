from tornado.web import RequestHandler
from tornado import gen
from server import ChangeMajorServer
from models.globaldata import term
# autoid: "1205"
# byzszymc: "汉语言文学"
# xq: "2018-2019-2"
# yxsmc: "文学院"
# zrrs: "-"
# zydm: "050101"
# zyid: "457"
# zymc: "汉语言文学(师范)"
class ChangeMajorHandler(RequestHandler):
    @gen.coroutine    
    def post(self):
        localcookie=self.get_argument('cookie','none')
        if localcookie =='none':
            self.finish("failure")
        res=ChangeMajorServer.change_major_server(localcookie,term,'zy')
        backinfo= yield res
        if backinfo ==None:
            self.finish("reqfailure")
        self.finish(backinfo[backinfo.index('['):backinfo.rfind(']')+1])

# autoid: "9772"
# byzszymc: "口腔医学"
# lxdh: "18021673008"
# pc: "1"
# sqly: "比起当前专业更喜欢医学 希望通过所学知识帮助他人"
# xq: "2018-2019-2"
# yxsmc: "医学院（护理学院）"
# zrrs: "30"
# zydm: "100301K"
# zyid: "383"
# zymc: "口腔医学"
class YBMajorHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        localcookie=self.get_argument('cookie','none')
        if localcookie =='none':
            self.finish("failure")
        res=ChangeMajorServer.change_major_server(localcookie,term,'ybzy')
        backinfo= yield res
        if backinfo==None:
            self.finish("reqfailure")
        self.finish(backinfo[backinfo.index('['):backinfo.rfind(']')+1])

# autoid: "9772"
# byzszymc: "口腔医学"
# pc: "1"
# xq: "2018-2019-2"
# yxsmc: "医学院（护理学院）"
# zcj: "88.44"
# zrnj: "2019"
# zydm: "100301K"
# zymc: "口腔医学"
class ChangeMajorGradeHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        localcookie=self.get_argument('cookie','none')
        if localcookie =='none':
            self.finish("failure")
        res=ChangeMajorServer.change_major_grade_server(localcookie,term)
        backinfo=yield res
        if backinfo==None:
            self.finish("reqfailure")
        self.finish(backinfo[backinfo.index('['):backinfo.rfind(']')+1])