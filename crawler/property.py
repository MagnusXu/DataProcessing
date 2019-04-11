#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:01:32 2019

@author: lordxuzhiyu
"""

import requests
import re
import datetime
import random
import time
from random import randint, choice
import threading
from bs4 import BeautifulSoup as bs

url = "http://www.xicidaili.com/nn"

headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6,nl;q=0.5",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }

uas = [
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0; Baiduspider-ads) Gecko/17.0 Firefox/17.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9b4) Gecko/2008030317 Firefox/3.0b4",
    "Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; BIDUBrowser 7.6)",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; LCJB; rv:11.0) like Gecko",
    ]

def get_ip(url):
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    data = soup.table.find_all("td")
    ip_compile = re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')
    port_compile = re.compile(r'<td>(\d+)</td>')
    ip = re.find_all(ip_compile, str(data))
    port = re.find_all(port_compile, str(data))
    return [":".join(i) for i in zip(ip, port)]

def get_url(code = 0, ips = []):
    try:
        ip = choice(ips)
    except:
        return False
    else:
        proxies = {
                "http":ip,
        }
        headers2 = {
                "Accept":"",
                "Accept-Encoding":"",
                "Accept-Language":"",
                "Referer":"",
                "User-Agent":choice(uas),
        }
        
    try:
        num = random.uniform(0, 1)
        url = "https://www.xicidaili.com/nn" % num
        r = requests.get(url, headers = headers2, proxies = proxies)
    except requests.exceptions.ConnectionError:
        print("Connect Error")
        if not ips:
            print("not ip")
        if ip in ips:
            ips.remove(ip)
        get_url(code, ips)
    else:
        date = datetime.datetime.now().strtime('%H:%M:%S')
        print(code, date)
        
ips = []
for i in range(6000):
    if i % 1000 == 0:
        ips.extend(get_ip(url))
    t1 = threading.Thread(target = get_url, args = (i, ips))
    t1.start()
    time.sleep(randint(10, 30))