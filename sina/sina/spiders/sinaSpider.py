# -*- coding: utf-8 -*-
import scrapy
import os
from sina.items import SinaItem

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class SinaspiderSpider(scrapy.Spider):
    name = "sina"
    allowed_domains = ["news.sina.com.cn"]
    start_urls = (
        'http://news.sina.com.cn/guide/',
    )

    def parse(self, response):
        items = []

        # 所有大类的url 和 标题
        parentUrls = response.xpath('//div[@id="tab01"]/div/h3/a/@href').extract()
        parentTitle = response.xpath('//div[@id="tab01"]/div/h3/a/text()').extract()

        # 所有小类的ur 和 标题
        subUrls = response.xpath('//div[@id="tab01"]/div/ul/li/a/@href').extract()
        subTitle = response.xpath('//div[@id="tab01"]/div/ul/li/a/text()').extract()

        # 爬取所有的大类
        for i in range(0,len(parentTitle)):
            # 指定大类路径和目录名
            parentFileName = './Data/'+parentTitle[i]

            # 判断该大类的目录是否存在,如果不存在就创建该目录
            if(not os.path.exists(parentFileName)):
                os.mkdir(parentFileName)

            # 爬取该大类下的所有小类
            for j in range(0, len(subUrls)):
                item = SinaItem()

                # 保存大类的title和url
                item['parentTitle'] = parentTitle[i]
                item['parentUrls'] = parentUrls[i]

                # 检查小类的url是否以同类别大类url开头，如果是返回True (sports.sina.com.cn 和 sports.sina.com.cn/nba)
                if_before = subUrls[j].startswith(item['parentUrls'])

                # 如果属于本大类，将存储目录放在本大类目录下
                if if_before:
                    # 拼接小类路径和目录名
                    subFileName = parentFileName+'/'+subTitle[j]

                    # 判断该小类目录是否存在,如果不存在就创建该目录
                    if not os.path.exists(subFileName):
                        os.mkdir(subFileName)

                    # 存储 小类url、title和filename字段数据
                    item['subUrls'] = subUrls[j]
                    item['subTitle'] = subTitle[j]
                    item['subFileName'] = subFileName

                    items.append(item)

            # 发送每个小类url的Request请求，得到Response连同包含meta数据 一同交给回调函数 second_parse 方法处理
            for item in items:
                yield scrapy.Request(url=item['subUrls'],meta={'meta_1':item}, callback=self.second_parse)

    # 对于返回的小类的url，再进行递归请求
    def second_parse(self, response):
        # 提取每次Response的meta值
        meta_1 = response.meta["meta_1"]

        # 取出所有小类中的子链接
        sonUrls = response.xpath('//a/@href').extract()

        items = []

        for i in range(0, len(sonUrls)):
            # 检查每个链接是否以大类url开头、以.shtml结尾，如果是返回True
            if_belong = sonUrls[i].endswith('.shtml') and sonUrls[i].startswith(meta_1['parentUrls'])

            # 如果属于本大类，获取字段值放在同一个item下便于传输
            if if_belong:
                item = SinaItem()
                item['parentTitle'] = meta_1['parentTitle']
                item['parentUrls'] = meta_1['parentUrls']
                item['subUrls'] = meta_1['subUrls']
                item['subTitle'] = meta_1['subTitle']
                item['subFileName'] = meta_1['subFileName']
                item['sonUrls'] = sonUrls[i]
                items.append(item)

        # 发送每个小类下子链接url的Request请求，得到Response后连同包含meta数据
        # 一同交给回调函数 detail_parse 方法处理
        for item in items:
            yield scrapy.Request(url=item['sonUrls'], meta={'meta_2': item}, callback=self.detail_parse)

    # 数据解析方法，获取文章标题和内容
    def detail_parse(self, response):
        item = response.meta["meta_2"]
        content = ""
        # 文章标题
        head = response.xpath('//h1[@id="main_title"]/text()')
        # 文章内容
        content_list = response.xpath('//div[@id="artibody"]/p/text()').extract()

        # 将p标签里的文本内容合并到一起,因为文章是由很多p标签组成的
        for content_one in content_list:
            content += content_one

        item['head'] = head
        item['content'] = content

        yield item

