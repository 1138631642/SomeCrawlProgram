# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencentCrawlSpider.items import TencentItem


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0']
    # 匹配规则，可以有多个
    rules = (
        # LinkExtractor(allow=r'start=\d+') ：是匹配出所有符合allow后面正则的链接
        # callback:回调函数。 follow：是否跟进连接
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )
    # 这个方法名出来不可以叫Parse，叫其他任意名字都可以
    def parse_item(self, response):
        postion_list = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')

        for position in postion_list:
            item = TencentItem()
            item['positionName'] = position.xpath('./td[1]/a/text()').extract()[0]
            type = position.xpath('./td[2]/text()').extract()
            if len(type) <= 0:
                item['positionType'] = " "
            else:
                item['positionType'] = type[0]

            item['positionLink'] = position.xpath('./td[1]/a/@href').extract()[0]
            item['positionLocation'] = position.xpath('./td[4]/text()').extract()[0]
            item['positionNum'] = position.xpath('./td[3]/text()').extract()[0]
            item['positionTime'] = position.xpath('./td[5]/text()').extract()[0]

            yield item
