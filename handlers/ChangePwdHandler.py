from tornado.web import RequestHandler 
from tornado import gen
from server import ChangePwdServer
from sql import mysql
class ChangePwdHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        stuid=self.get_argument('stuid','none')
        localcookie,oldpwd=self.get_argument('cookie','none'),self.get_argument('oldpwd','none')
        newpwd,newpwd1=self.get_argument('newpwd','none'),self.get_argument('newpwd1','none')
        if localcookie=='none' or oldpwd=='none' or stuid=='none' or newpwd=='none' or newpwd1=='none':
            self.finish("failure")
        res=ChangePwdServer.change_pwd_server(localcookie,oldpwd,newpwd,newpwd1)
        result=yield res
        if result==None:
            self.finish("reqfailure")
        if result.find('success:true')!=-1:
            # change db data
            try:
                mysql.Sqlutils().updateSelective('userlist',stuid,newpwd)
            except Exception:
                self.finish('success')
            self.finish('success')
        else:
            self.finish('failure')