# -*- coding: utf-8 -*-
import scrapy
from douyu.items import DouyuItem



import json
class DouyummSpider(scrapy.Spider):
    name = "douyumm"
    allowed_domains = ["capi.douyucdn.cn"]
    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    page = 0
    start_urls = [url + str(page)]

    def parse(self, response):

        data = json.loads(response.text)["data"]
        for each in data:
            item = DouyuItem()
            item["nickName"] = each["nickname"]
            item["city"] = each['anchor_city']
            item['imageLink'] = each['vertical_src']

            print each["nickname"]
            yield item

        if self.page <= 100:
            self.page += 20

        yield scrapy.Request(self.url + str(self.page),callback=self.parse)
