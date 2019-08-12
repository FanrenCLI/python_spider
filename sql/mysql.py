import pymysql
from models.globaldata import *

class Sqlutils():
    def __init__(self):
        self.conn=None
        self.cur=None
    def connection(self):
        self.conn=pymysql.Connect(host=host,port=port,user=userid,password=pwd,db=db)
        self.cur=self.conn.cursor()
    def insert(self,tablelist,UserModel):
        self.connection()
        cur=self.cur
        cur.execute("insert into "+tablelist+"(stuid,idcard,pwd,openid) values('%s','%s','%s','%s')"%(UserModel.stuid,UserModel.idcard,UserModel.pwd,UserModel.openid))
        self.conn.commit()
        cur.close()
        self.conn.close()
        return True
    def selectByOpenid(self,tablelist,openid):
        self.connection()
        cur=self.cur
        sqlstr="select * from " +tablelist+" where openid="
        cur.execute(sqlstr+"%s",(openid))
        result=cur.fetchall()
        cur.close()
        self.conn.close()
        return result
    def updateSelective(self,tablelist,stuid,pwd):
        self.connection()
        cur=self.cur
        sqlstr="update "+tablelist+" set pwd='%s' where stuid='%s'"
        cur.execute(sqlstr % (pwd,stuid))
        self.conn.commit()
        cur.close()
        self.conn.close()
################################################## 
    def selectAll(self,tablelist):
        self.connection()
        cur=self.cur
        sqlstr="select * from "+tablelist
        result=cur.execute(sqlstr).fetchall()
        cur.close()
        self.conn.close()
        return result

    def selectByAccountPwd(self,tablelist,stuid,userpwd):
        self.connection()
        cur=self.cur
        sqlstr="select * from "+tablelist+" where stuid="
        cur.execute(sqlstr+"%s",(stuid))
        result=cur.fetchall()
        cur.close()
        self.conn.close()
        return result

# 班级课表sql语句
    def selectByClassName(self,tablelist,classname):
        self.connection()
        cur=self.cur
        sqlstr="select * from "+tablelist+" where bjmc="
        cur.execute(sqlstr+"%s",(classname))
        result=cur.fetchall()
        cur.close()
        self.conn.close()
        return result
    def insertManyinfo(self,tablelist,insertinfo):
        self.connection()
        cur=self.cur
        for i in insertinfo:
            cur.execute("insert into "+tablelist+"(kcmc,zhouci,xqj,jieci,skdd,bjmc,skjs) values('%s','%s','%s','%s','%s','%s','%s')"%(i['kcmc'],i["zhouci"],i["xqj"],i["jieci"],i["skdd"],i["bjmc"],i["skjs"]))
            self.conn.commit()
        cur.close()
        self.conn.close()
        return True