# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
   nickName = scrapy.Field()
   imageLink = scrapy.Field()
   iamgePath = scrapy.Field()
   city = scrapy.Field()

