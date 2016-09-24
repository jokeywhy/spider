# coding:utf-8
import re

from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle

from zhihu_topic.items import *

class TopicSpider(CrawlSpider):
    download_delay = 0.8
    name = 'topic'
    start_urls = ['http://www.zhihu.com/topic/19776749']
    allowed_domains = ['zhihu.com']
    
    rules = [Rule(sle(allow = ('/topic/\d+$', )), callback = 'parse_topic', follow = True),]
    
    def parse_topic(self, response):
        sel = Selector(response)
        item = ZhihuTopicItem()
        item['topic'] = sel.xpath('//h1[@class="zm-editable-content"]/text()').extract()
        index = response.url.rfind('/')
        item['link_id'] = response.url[index+1:]
        item['followers'] = sel.xpath('//div[@class="zm-topic-side-followers-info"]/strong/text()').extract()
        item['paren_topic'] = sel.xpath('//div[@id="zh-topic-side-parents-list"]/div/div/a/text()').extract()
        item['child_topic'] = sel.xpath('//div[@id="zh-topic-side-children-list"]/div/div/a/text()').extract()
        print repr(item).decode('unicode-escape')
        print '*' * 20
        return item
        
    
    
    
    
    