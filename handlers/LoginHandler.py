from tornado.web import RequestHandler
from server import LoginServer
from tornado import gen
from models.user import User
from sql import mysql
class LoginHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        username,idcard,pwd,code=self.get_argument('stuid','none'),self.get_argument('idcard','none'),self.get_argument('pwd','none'),self.get_argument('code','none')
        # 获取用户openid
        openid=LoginServer.get_user_info(code)
        # 查询openid是否已经绑定
        sqlresult = mysql.Sqlutils().selectByOpenid('userlist',openid)
        # 对于openid是否绑定进行操作判断
        if sqlresult:
            UserModel=User(username,idcard,pwd,None)
        else:
            UserModel=User(username,idcard,pwd,openid)
        # 判断输入信息是否完整
        if username and idcard and pwd:
            # 根据用户信息进行模拟登陆
            result= LoginServer.login_server(username,idcard,pwd)
            loginstate=yield result
            # 登录成功则返回cookie
            if loginstate!=0:
                # 若openid未绑定账号，则进行数据库存储操作
                if UserModel.openid:
                    try:
                        mysql.Sqlutils().insert('userlist',UserModel)
                    except Exception:
                        self.write('0')
                self.write(loginstate)
            else:
                self.write('0')
        else:
            self.write('0')

class LoginWXHander(RequestHandler):
    @gen.coroutine
    def post(self):
        openid= LoginServer.get_user_info(self.get_argument('code','none'))
        # 根据openid查询是否存在用户
        sqlresult=mysql.Sqlutils().selectByOpenid('userlist',openid)
        if sqlresult:
            result= LoginServer.login_server(sqlresult[0][1],sqlresult[0][2],sqlresult[0][3])
            loginstate=yield result
            if loginstate!=0:
                self.write(loginstate)
            else:
                self.write('0')
        else:
            self.write('0')