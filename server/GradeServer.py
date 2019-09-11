from tornado import gen
from tornado.httpclient import AsyncHTTPClient
from utils.json2url import JSON2URL
from utils.IPProxyPool import Random_ProxyIP
AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")

@gen.coroutine
def grade_server(localcookie):
    req_url_login='http://jwgl.ntu.edu.cn/cjcx/Data/ScoreAllData.aspx'
    grade_header={
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '19',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': localcookie,
        'Host': 'jwgl.ntu.edu.cn',
        'Origin': 'http://jwgl.ntu.edu.cn',
        'Referer': 'http://jwgl.ntu.edu.cn/cjcx/Main.aspx',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    grade_body={
        'start':'0',
        'pageSize':'99'
    }
    ip_proxy,proxy_port=Random_ProxyIP()
    try:
        res= yield AsyncHTTPClient().fetch(req_url_login,method='POST',body=JSON2URL(grade_body),headers=grade_header,proxy_host=ip_proxy,proxy_port=proxy_port)
    except Exception:
        try:
            res= yield AsyncHTTPClient().fetch(req_url_login,method='POST',body=JSON2URL(grade_body),headers=grade_header)
        except Exception:
            return None
    return res.body.decode('utf-8')

@gen.coroutine
def offset_grade_server(localcookie):
    req_url_login='http://jwgl.ntu.edu.cn/cjcx/Data/ScoreOffsetData.aspx'
    grade_header={
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '19',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': localcookie,
        'Host': 'jwgl.ntu.edu.cn',
        'Origin': 'http://jwgl.ntu.edu.cn',
        'Referer': 'http://jwgl.ntu.edu.cn/cjcx/Main.aspx',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    grade_body={
        'start':'0',
        'pageSize':'99'
    }
    ip_proxy,proxy_port=Random_ProxyIP()
    try:
        res= yield AsyncHTTPClient().fetch(req_url_login,method='POST',body=JSON2URL(grade_body),headers=grade_header,proxy_host=ip_proxy,proxy_port=proxy_port)
    except Exception:
        try:
            res= yield AsyncHTTPClient().fetch(req_url_login,method='POST',body=JSON2URL(grade_body),headers=grade_header)
        except Exception:
            return None
    return res.body.decode('utf-8')