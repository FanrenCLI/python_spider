import requests
from bs4 import BeautifulSoup
import threading
from time import sleep
from models.globaldata import ip_proxy_list
import  time
import random
import bs4
def loop1():
    pageindex=0
    while True:
        pageindex=pageindex+1
        # 保证ip代理池中ip数量不少于60个
        if len(ip_proxy_list)<60:
            print('doing===')      
            s = requests.session()
            header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
            }
            rs = s.get(url="http://www.xicidaili.com/nn/"+str(pageindex), headers=header)
            soup = BeautifulSoup(rs.text, "lxml")
            ip_list_all = []
            ip_list = soup.select_one("#ip_list").select("tr")
            ip_info_list_key = ["ip", "port", "address", "hidden", "type", "speed", "conn_time", "survival_time", "verify_time"]

            for item in ip_list[1:]:
                ip_info_list_value = []
                ip_info = item.select("td")
                for info in ip_info[1:]:
                    if info.select_one(".bar"):
                        ip_info_list_value.append(info.select_one(".bar")["title"])
                    else:
                        ip_info_list_value.append(info.get_text().strip())
                ip_list_all.append(dict(zip(ip_info_list_key, ip_info_list_value)))

            for i  in ip_list_all:
                if i['type']=='HTTP':
                    try:
                        res1=requests.get(url='https://www.baidu.com',proxies={'http':"http://"+i['ip']+':'+i['port']},timeout=0.5)
                        if res1.status_code==200:
                            ip_proxy_list.append(i['ip']+":"+i["port"])
                    except Exception:
                        pass
            print("doing...")
        else:
            pageindex=0
            print('begin sleep')
            time.sleep(3600)
            print('end sleep')
            continue
def loop2():
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    requrl='http://www.66ip.cn/mo.php?sxb=&tqsl=100&port=&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea='
    res=requests.get(url=requrl,headers=header)
    bs=bs4.BeautifulSoup(res.content,'lxml')
    temp=str(bs.select('p')[0]).split()
    result=[]
    for i in temp:
        if i.find('<br/>')!=-1:
            result.append(i.split('<br/>')[0])
    for i in result:
        try:
            res1=requests.get(url='https://www.baidu.com',proxies={'http':"http://"+i},timeout=0.5)
            if res1.status_code==200:
                ip_proxy_list.append(i)
        except Exception:
            pass
def Random_ProxyIP():
    num=random.randint(0,len(ip_proxy_list)-1)
    i=ip_proxy_list[num]
    ip_proxy_list.remove(i)
    arr=i.split(':')
    return arr[0],int(arr[1])