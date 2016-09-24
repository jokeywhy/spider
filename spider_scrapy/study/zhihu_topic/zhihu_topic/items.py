# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuTopicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    topic = scrapy.Field()
    link_id = scrapy.Field()
    paren_topic = scrapy.Field()
    child_topic = scrapy.Field()
    followers = scrapy.Field()