from tornado import gen
from tornado.httpclient import AsyncHTTPClient
from utils.json2url import JSON2URL
@gen.coroutine
def courseServer(term,info,localcookie):
    req_URL='http://jwgl.ntu.edu.cn/cjcx/Data/Table/ClassTableData.aspx'
    course_header={
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
        'X-Requested-With': 'XMLHttpRequest',
    }
    course_body={
        'xq':term,
        'bjid':info
    }
    res= yield AsyncHTTPClient().fetch(req_URL,method='POST',body=JSON2URL(course_body),headers=course_header)
    return res.body.decode('utf-8')