# coding=utf8

import urllib
import urllib2

url = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=40"

headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

frmData =  {
    "start":"40",
    "sort":"T"
}

data = urllib.urlencode(frmData)

request = urllib2.Request(url, data=data, headers=headers)

response = urllib2.urlopen(request)

data = response.read()
w = open('data/move.json','w')
w.write(data)
print("ok")