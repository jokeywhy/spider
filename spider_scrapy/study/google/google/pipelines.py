# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GooglePipeline(object):
    def process_item(self, item, spider):
        return item

    def close_spider(self, spider):
        print 'close'