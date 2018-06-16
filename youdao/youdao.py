# coding=utf8

import urllib
import urllib2
import random
import time
import hashlib
import json

kw = raw_input("请输入你要翻译的中文/英文:")

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

u = 'fanyideskweb'
d = kw
f = str(int(time.time()*1000) + random.randint(1,10))
c = 'rY0D^0\'nM0}g5Mm1z%1G4'

sign = hashlib.md5((u + d + f + c)).hexdigest()


# 自定义data数据
formdata = {
    "from":"AUTO",
    "i":kw,
    "to":"AUTO",
    'salt':f,#"1526717108769",
    "sign":sign,#"2d72a814d3b2ab3e16d0fdf7925fb3f9",
    "client":"fanyideskweb",
    "smartresult":"dict",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "ue":"UTF-8",
    "action":"FY_BY_ENTER",
    "typoResult":"true"
}

# 将字典字符串转化为url编码
data = urllib.urlencode(formdata)

request = urllib2.Request(url,data=data,headers=headers)

response = urllib2.urlopen(request)

print(response.read())

