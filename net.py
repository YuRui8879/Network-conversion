from bs4 import BeautifulSoup
import re
import requests
import json

def check_stage(net_type = 4):
    if net_type == 4:
        url = 'https://lgn.bjut.edu.cn/'
    else:
        url = 'https://lgn6.bjut.edu.cn/'
    strhtml = requests.get(url)
    soup = BeautifulSoup(strhtml.text, features='lxml')
    title = soup.title.text
    if '北京工业大学上网信息窗' in title:
        return 1
    else:
        return 0

def deconnect(net_type = 4):
    if net_type == 4:
        url = 'https://lgn.bjut.edu.cn/F.html'
    else:
        url = 'https://lgn6.bjut.edu.cn/F.html'
    strhtml = requests.get(url)
    soup = BeautifulSoup(strhtml.text,features='lxml')
    title = soup.title.text
    if '信息返回窗' in title:
        return 1
    else:
        return 0

def post_v4(name,password):
    url = 'https://lgn.bjut.edu.cn/'
    header = {
        'Host':'lgn.bjut.edu.cn',
        'Connection':'keep-alive',
        'Content-Length':'77',
        'Cache-Control':'max-age=0',
        'Upgrade-Insecure-Requests':'1',
        'Origin':'https://lgn.bjut.edu.cn',
        'Content-Type':'application/x-www-form-urlencoded',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site':'same-site',
        'Sec-Fetch-Mode':'navigate',
        'Sec-Fetch-User':'?1',
        'Sec-Fetch-Dest':'document',
        'Referer':'https://lgn.bjut.edu.cn/',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-platform': "Windows"
    }
    post_data = {
        'DDDDD':str(name),
        'upass':str(password),
        'v46s':'1',
        'v6ip':'',
        'f4serip':'172.30.201.10',
        '0MKKey':''
    }
    strhtml = requests.post(url,data=post_data,headers=header)
    soup = BeautifulSoup(strhtml.text,features='lxml')
    title = soup.title.text
    if '登录成功窗' in title:
        return 1
    else:
        return 0

def post_v6(name,password):
    url = 'https://lgn6.bjut.edu.cn/'
    header = {
        'Host':'lgn6.bjut.edu.cn',
        'Connection':'keep-alive',
        'Content-Length':'77',
        'Cache-Control':'max-age=0',
        'Upgrade-Insecure-Requests':'1',
        'Origin':'https://lgn.bjut.edu.cn',
        'Content-Type':'application/x-www-form-urlencoded',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site':'same-site',
        'Sec-Fetch-Mode':'navigate',
        'Sec-Fetch-User':'?1',
        'Sec-Fetch-Dest':'document',
        'Referer':'https://lgn.bjut.edu.cn/',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Upgrade-Insecure-Requests': '1',
        'sec-ch-ua-platform': "Windows",
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"'
    }
    post_data = {
        'DDDDD':str(name),
        'upass':str(password),
        'v46s':'2',
        'v6ip':'',
        'f4serip':'172.30.201.2',
        '0MKKey':''
    }
    strhtml = requests.post(url,data=post_data,headers=header)
    soup = BeautifulSoup(strhtml.text,features='lxml')
    title = soup.title.text
    if '登录成功窗' in title:
        return 1
    else:
        return 0

def load_json(path):
    with open(path,'r') as f:
        load_dict = json.load(f)
    ids = load_dict['id']
    password = load_dict['password']
    return ids,password

def connect_v4():
    ids,password = load_json(r'.\config.json')
    if check_stage(net_type = 6) == 1:
        deconnect(net_type = 6)
    flag = post_v4(ids,password)
    if flag == 1:
        print('连接ipv4成功')
    else:
        print('连接ipv4失败')

def connect_v6():
    ids,password = load_json(r'.\config.json')
    if check_stage(net_type = 4) == 1:
        deconnect(net_type = 4)
    flag = post_v6(ids,password)
    if flag == 1:
        print('连接ipv6成功')
    else:
        print('连接ipv6失败')