# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
# 用于给图片重命名
import os
# 用于下载图片
from scrapy.pipelines.images import ImagesPipeline
# 用于获取setting中变量值
from scrapy.utils.project import get_project_settings
import json
class ImagePipeline(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):

        image_url = item["imageLink"]
        print image_url
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        # 固定写法，获取图片路径，同时判断这个路径是否正确，如果正确，就放到 image_path里，ImagesPipeline源码剖析可见
        image_path = [x["path"] for ok, x in results if ok]

        os.rename(self.IMAGES_STORE + "/" + image_path[0], self.IMAGES_STORE + "/" + item["nickName"] + ".jpg")
        item["iamgePath"] = self.IMAGES_STORE + "/" + item["nickName"]

        return item
