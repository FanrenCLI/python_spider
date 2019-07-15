def for_get_cookies(getuserid,getpassword):

    from bs4 import BeautifulSoup
    import requests
    import re
    from PIL import Image
    import keras
    from keras import backend as K
    import io
    import numpy as np

    model_file_path = r"D:/jiaowu/tr1199.h5"
    mainhost = '10.10.8.68'
    mainurl = 'http://'+mainhost+'/'
    useragent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
    fromurl_for_getusername = mainurl+'default2.aspx'

    headers_for_getcoolie = {
        'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
        'Accept-Language': 'zh-CN',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'Keep-Alive',
        'Host': mainhost,
        'User-Agent': useragent
    }

    global getcookie

    gc = requests.get(fromurl_for_getusername, headers=headers_for_getcoolie)
    getcookie = re.sub(r';.*$', '',gc.headers['Set-Cookie'])
    vssoup = BeautifulSoup(gc.text,'lxml')
    vstext = vssoup.select('input')
    get__VIEWSTATE = vstext[0]['value']

    #获取cookie-end

    #请求和识别验证码-start

    img_rows, img_cols = 12, 22
    code_url = mainurl+'CheckCode.aspx'

    if K.image_data_format() == 'channels_first':
        input_shape = (1, img_rows, img_cols)
    else:
        input_shape = (img_rows, img_cols, 1)

    import string

    CHRS = string.ascii_lowercase + string.digits

    model = keras.models.load_model(model_file_path)

    headers_for_getcode = {
    'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
    'Accept-Encoding' : 'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie' : getcookie,
    'Host' : mainhost,
    'Referer' : mainurl,
    'User-Agent' : useragent
    }

    def getImg():
        pic = requests.get(code_url,headers=headers_for_getcode)
        image_data = io.BytesIO(pic.content)
        image = Image.open(image_data)
        return image
        
    def handle_split_image(image):
        
        im = image.point(lambda i: i != 43, mode='1')
        y_min, y_max = 0, 22
        split_lines = [5, 17, 29, 41, 53]
        ims = [im.crop([u, y_min, v, y_max]) for u, v in zip(split_lines[:-1], split_lines[1:])]
        return ims

    def predict_image(images):
        Y = []
        for i in range(4):
            im = images[i]
            test_input = np.array(im)
            test_input = test_input.reshape(1, *input_shape)
            y_probs = model.predict(test_input)
            y = CHRS[y_probs[0].argmax(-1)]
            Y.append(y)
        return ''.join(Y)

    getcode = predict_image(handle_split_image(getImg()))
    K.clear_session()

    #请求和识别验证码-end

    #模拟登陆-start

    headers_for_login = {
    'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': fromurl_for_getusername,
    'Accept-Language': 'zh-CN',
    'Cache-Control': 'no-cache',
    'Connection': 'Keep-Alive',
    'Cookie': getcookie,
    'Host': mainhost,
    'User-Agent': useragent
    }

    data_for_login = {
        '__VIEWSTATE': get__VIEWSTATE,
        'txtUserName': getuserid,
        'Textbox1': getuserid,
        'TextBox2':getpassword,
        'txtSecretCode': getcode,
        'RadioButtonList1': "学生",
        'Button1':'',
        'lbLanguage':'',
        'hidPdrs':'',
        'hidsc':''
    }

    requests.post(fromurl_for_getusername,data=data_for_login,headers=headers_for_login)

    #模拟登陆-end

    #查询-start
    
    def get_name():
        fromurl_for_query = mainurl+'xs_main.aspx?xh='+getuserid
        getname = requests.get(fromurl_for_query,headers=headers_for_login)
        soup_name = BeautifulSoup(getname.text, 'lxml')
        try:
            name = soup_name.find('span', attrs={'id': 'xhxm'}).text
        except AttributeError:
            return 0
        else:
            username = re.sub('同学','',name)
            return username
    #查询-end
    if get_name()==0:
        return 0
    else:
        return "#"+getcookie+"##"+get_name()+"###"+mainhost


#print(for_get_cookies("",''))
    