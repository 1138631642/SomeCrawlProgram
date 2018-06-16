# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class SinaPipeline(object):

    def process_item(self, item, spider):

        sonUrls = item['sonUrls']

        # 文件名为子链接url中间部分，并将 / 替换为 _，保存为 .txt格式
        filename = sonUrls[7:-6].replace('/', '_')
        filename += ".txt"
        # 让内容写入到指定的目录中
        fp = open(item['subFileName'] + '/' + filename, 'w')
        fp.write(item['content'])
        fp.close()

        return item
