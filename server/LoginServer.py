import requests
from tornado import httpclient
import re
import io
import json
from tornado import gen
from PIL import Image
from bs4 import BeautifulSoup
from CNN import keras_model
from utils.json2url import JSON2URL
req_url='http://jwgl.ntu.edu.cn/cjcx/checkImage.aspx'
req_url_login="http://jwgl.ntu.edu.cn/cjcx/Default.aspx"
UserAgent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
get__VIEWSTATE=''
localCookie=''
get__VIEWSTATEGENERATOR=''

def BeforeLogin():
    req_Header={
        'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'jwgl.ntu.edu.cn',
        'Referer': 'http://jwgl.ntu.edu.cn/cjcx/',
        'User-Agent': UserAgent
    }
    global get__VIEWSTATE
    global localCookie
    global get__VIEWSTATEGENERATOR
    res=requests.post(req_url,headers=req_Header)
    # 获取VIEWSTATE用户登录相关信息
    BSresult = BeautifulSoup(res.text,'lxml')
    BSInput = BSresult.select('input')
    get__VIEWSTATE = BSInput[0]['value']
    get__VIEWSTATEGENERATOR=BSInput[1]['value']
    # 获取cookie
    localCookie = re.sub(r';.*$', '',res.headers['Set-Cookie'])
    image_data = io.BytesIO(res.content)
    image = Image.open(image_data)
    return keras_model.mainCode(image)
@gen.coroutine
def LoginMain(img_val,username,idcard,pwd):
    global localCookie
    global get__VIEWSTATE
    global get__VIEWSTATEGENERATOR
    login_Header={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': localCookie,
        'Host': 'jwgl.ntu.edu.cn',
        'Origin': 'http://jwgl.ntu.edu.cn',
        'Referer': 'http://jwgl.ntu.edu.cn/cjcx/Default.aspx',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent':UserAgent
    }
    login_data={
        '__VIEWSTATE': get__VIEWSTATE.replace('/','%2F').replace('=','%3D'),
        '__VIEWSTATEGENERATOR': get__VIEWSTATEGENERATOR,
        'xh': username,
        'sfzh': idcard,
        'kl': pwd,
        'yzm': img_val
    }

    res= yield  httpclient.AsyncHTTPClient().fetch(req_url_login,method='POST',body=JSON2URL(login_data),headers=login_Header)
    loginBackBody = BeautifulSoup(res.body.decode('utf-8'),'lxml')
    BackBodyBS = loginBackBody.select('#stuInfo')
    if len(BackBodyBS)!=0:
        return BackBodyBS[0].get_text()
    else:
        return False
@gen.coroutine
def login_server(username,idcard,pwd):
    Img_val = BeforeLogin()
    while True:
        # 判断图片识别是否正确
        if Img_val!=0:
            # 发送登录请求
            login_states =  LoginMain(Img_val,username,idcard,pwd)
            backinfo =yield login_states
            # 判断登录是否成功
            if backinfo:
                return localCookie
            else:
                return 0
        Img_val = BeforeLogin()
# 微信登录功能,获取openid功能
def get_user_info(js_code):
    req_params = {
        "appid": 'wx3563eb654dd6f231',  # 小程序的 ID
        "secret": '7d4484b369bcf3cc301bb9f7884c6a4a',  # 小程序的 secret
        "js_code": js_code,
        "grant_type": 'authorization_code'
    }
    req_result = requests.get('https://api.weixin.qq.com/sns/jscode2session', 
                              params=req_params, timeout=3, verify=False)
    return req_result.json()['openid']