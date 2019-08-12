from tornado import gen
from tornado.httpclient import AsyncHTTPClient
from utils.json2url import JSON2URL

AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")

@gen.coroutine
def change_pwd_server(localcookie,oldpwd,newpwd,newpwd1):
    req_url='http://jwgl.ntu.edu.cn/cjcx/actions/AlterPasswordAction.aspx'
    req_header={
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': localcookie,
        'Host': 'jwgl.ntu.edu.cn',
        'Origin': 'http://jwgl.ntu.edu.cn',
        'Referer':' http://jwgl.ntu.edu.cn/cjcx/Main.aspx',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    req_body={
        'oldPwd': oldpwd,
        'newPwd': newpwd,
        'newPwd1': newpwd1
    }
    backinfo = yield AsyncHTTPClient().fetch(req_url,method='POST',body=JSON2URL(req_body),headers=req_header)
    return backinfo.body.decode('utf-8')