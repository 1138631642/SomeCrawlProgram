# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class TencentpositionSpider(scrapy.Spider):
    name = "tencentPosition"
    allowed_domains = ["tencent.com"]
    url = "https://hr.tencent.com/position.php?&start="
    page = 0
    start_urls = [url + str(page)]

    def parse(self, response):

        postion_list = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')

        for position in postion_list:
            item = TencentItem()
            item['positionName'] = position.xpath('./td[1]/a/text()').extract()[0]
            type = position.xpath('./td[2]/text()').extract()
            if len(type)<=0:
             item['positionType'] = " "
            else:
                item['positionType'] =type[0]

            item['positionLink'] = position.xpath('./td[1]/a/@href').extract()[0]
            item['positionLocation'] = position.xpath('./td[4]/text()').extract()[0]
            item['positionNum'] = position.xpath('./td[3]/text()').extract()[0]
            item['positionTime'] = position.xpath('./td[5]/text()').extract()[0]

            yield item

        if self.page <= 4000:
            self.page += 10
        print "-"*20
        yield scrapy.Request(self.url + str(self.page),callback=self.parse)
            # print positionName
            # print positionType

# //tr[@class="even"]|//tr[@class="odd"]
# positionName
# /td[1]/a/text()

# positionLink
# /td[1]/a/@href

# positionType
# /td[2]/text()

# positionNum
# /td[3]/text()

# positionLocation
# /td[4]/text()

# positionTime
# /td[5]/text()