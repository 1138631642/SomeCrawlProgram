# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    positionName = scrapy.Field()
    positionLink = scrapy.Field()
    positionLocation = scrapy.Field()
    positionTime = scrapy.Field()
    positionNum = scrapy.Field()
    positionType = scrapy.Field()
