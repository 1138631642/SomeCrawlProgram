# coding=utf8

import urllib2
from selenium import webdriver
from lxml import etree



if __name__ == "__main__":
    url = "http://www.douyu.com/directory/all"
    driver = webdriver.Firefox()
    driver.get(url)
    while True:


        html = driver.page_source

        content = etree.HTML(html)

        node_list = content.xpath('//div[@class="mes"]//p')

        print len(node_list)

        for item in node_list:
            name = item.xpath('./span[@class="dy-name ellipsis fl"]')
            num = item.xpath('./span[@class="dy-num fr"]')

            # print name[0].text
            if len(num)>0:
                n = num[0].text
            else:
                n = '0'
            username = name[0].text

            print username + "-" + n
            # print u"直播名："+username + u"\t观看人数：" + n

            if driver.page_source.find("shark-pager-disable-next") != -1:
                break

            driver.find_element_by_class_name("shark-pager-next").click()


    # print html
    driver.quit()

    # 名字
    # //div[@class="mes"]//span[@class="dy-name ellipsis fl"]

    # 观众人数
    # //div[@class="mes"]//span[@class="dy-num fr"]

    # 无下一页按钮
    # shark - pager - next
    # shark - pager - disable
    # shark - pager - disable - next

    # 有下一页按钮
    # shark - pager - next