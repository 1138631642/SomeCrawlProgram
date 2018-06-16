# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguang.items import DongguangItem

class DgSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    rules = (
        Rule(LinkExtractor(allow=r'type=4&page=\d+'),callback='parse_item',follow=True),
        # Rule(LinkExtractor(allow=r'html/question/\d+/\d+.shtml'), callback='parse_item',follow=False),
    )

    def parse_item(self, response):
        # print response.url
        item = DongguangItem()
        item['title'] = response.xpath('//div[@class="pagecenter p3"]//strong[@class="tgray14"]/text()').extract()[0]
        item['number'] = item['title'].split(' ')[-1].split(':')[-1]
        item['content'] = response.xpath('//div[@class="c1 text14_2"]/text()').extract()[0]
        item['url'] = response.url
        print item['title']
        yield item

# title
# //div[@class="pagecenter p3"]//strong[@class="tgray14"]/text()

# number
# title.split(' ')[-1].split(':')[-1]

# content
# //div[@class="c1 text14_2"]/text()

# url
# response.url