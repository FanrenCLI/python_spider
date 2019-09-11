from tornado import gen
from utils.json2url import JSON2URL
from tornado.httpclient import AsyncHTTPClient
from utils.IPProxyPool import Random_ProxyIP
AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")

@gen.coroutine
def change_major_server(localcookie,term,info):
    req_url='http://jwgl.ntu.edu.cn/cjcx/Data/SubjectSelectionData.aspx'
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
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    req_body={
        'type': info,
        'xq':term
    }
    ip_proxy,proxy_port=Random_ProxyIP()
    try:
        res = yield AsyncHTTPClient().fetch(req_url,method='POST',body=JSON2URL(req_body),headers=req_header,proxy_host=ip_proxy,proxy_port=proxy_port)
    except Exception:
        try:
            res = yield AsyncHTTPClient().fetch(req_url,method='POST',body=JSON2URL(req_body),headers=req_header)
        except Exception:
            return None
    return res.body.decode('utf-8')

@gen.coroutine
def change_major_grade_server(localcookie,term):
    req_url='http://jwgl.ntu.edu.cn/cjcx/Data/WritenTestQueryData.aspx'
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
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    req_body={
        'xq':term
    }
    ip_proxy,proxy_port=Random_ProxyIP()
    try:
        res = yield AsyncHTTPClient().fetch(req_url,method='POST',body=JSON2URL(req_body),headers=req_header,proxy_host=ip_proxy,proxy_port=proxy_port)
    except Exception:
        try:
            res = yield AsyncHTTPClient().fetch(req_url,method='POST',body=JSON2URL(req_body),headers=req_header)
        except Exception:
            return None
    return res.body.decode('utf-8')