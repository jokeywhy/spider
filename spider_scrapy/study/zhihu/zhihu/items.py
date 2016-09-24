# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field() # 标题
    content = scrapy.Field() # 内容
    zan = scrapy.Field() # 赞同人数
    publish_time = scrapy.Field() # 发布时间
    aid = scrapy.Field() # 该回答的唯一ID
