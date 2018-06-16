# coding=utf8

import urllib
import urllib2


def loadPage(url, filename):

    print("正在下载"+filename)

    heads = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
    request = urllib2.Request(url, headers=heads)
    response = urllib2.urlopen(request)
    return response.read()


def writeFile(html,filename):

    print("正在存储"+filename)
    with open('html/'+filename,'w') as f:
        f.write(html)
    print("存储成功")
    print("-"*20)


def teiBaSpider(url, startPage, endPage):

   for page in range(startPage, endPage+1):
       # 计算出当前实际是第几页
       pn = (page-1)*50

       filename = "第"+str(pn)+"页.html"

       fullUrl = url + "&ie=utf-8&pn=" + str(pn)

       print(fullUrl)

       #下载页面
       html = loadPage(url,filename)
       # 将下载下来的页面保存起来
       writeFile(html,filename)


if __name__ == "__main__":

    kw = raw_input("请输入你要爬取贴吧名字:")
    startPage = int(raw_input("从第几页开始爬取:"))
    endPage = int(raw_input("爬取到第几页结束:"))

    # url:https://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=100
    url = "https://tieba.baidu.com/f"

    # 将用户输入的贴吧名字转化为url编码格式
    key = urllib.urlencode({'kw':kw})
    # url:https://tieba.baidu.com/f?kw=xxxx
    url = url +"?"+ key

    teiBaSpider(url, startPage, endPage)