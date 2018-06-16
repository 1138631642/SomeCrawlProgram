# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguang.items import DongguangItem

class DgSpider(CrawlSpider):
    name = 'dg'
    allowed_domains = ['wz.sun0769.com']
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    page = 0
    start_urls = [url + str(page)]

    def parse(self,response):

        links = response.xpath('//a[@class="news14"]/@href').extract()
        for link in links:
            yield scrapy.Request(link,callback=self.parse_item)

        if self.page <=500:
            self.page += 30
            yield scrapy.Request(self.url+str(self.page),callback=self.parse)



    def parse_item(self, response):
        # print response.url
        item = DongguangItem()
        item['title'] = response.xpath('//div[@class="pagecenter p3"]//strong[@class="tgray14"]/text()').extract()[0]
        item['number'] = item['title'].split(' ')[-1].split(':')[-1]
        item['content'] = response.xpath('//div[@class="c1 text14_2"]/text()').extract()[0]
        item['url'] = response.url
        # print item['title']
        yield item

