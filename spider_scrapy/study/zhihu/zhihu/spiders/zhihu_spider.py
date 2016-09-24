# -*- coding:utf-8 -*-
import re

from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle

from zhihu.items import *
from zhihu.util import *

class ZhihuSpider(CrawlSpider):
    my_parse = MyParse()
    download_delay = 0.8
    name = 'zhihu'
    start_urls = [
        my_parse.topic_url ]
    allowed_domains = ['zhihu.com']
    rules = [
        Rule(sle(allow = ('/question/\d+$', )), callback = 'prase_info', follow = False),
        Rule(sle(allow = ('\?page=\d{0,%s}$' % my_parse.pages, )), follow = True),
        Rule(sle(allow = ('/%s/questions/$' % my_parse.link_id, )), follow = True),
    ]
    
    #def parse(self, response): 
    #    print response.body
       
    
    def prase_info(self, response):
        """解析回答信息"""
        sel = Selector(response)
        tmp_title = sel.xpath('//title/text()').extract()
        for sel in response.xpath('//div[@class="zm-item-answer "]'):
            item = ZhihuItem()
            item['title'] = tmp_title
            item['content'] = sel.xpath('div[@data-action]/div/text()').extract()
            item['zan'] = sel.xpath('div/button/span[@class="count"]/text()').extract()
            item['publish_time'] = sel.xpath('@data-created').extract()
            item['aid'] = sel.xpath('@data-aid').extract()
            
            zan_str = re.search("'(.*?)'", unicode(item['zan']))
            print '-' * 15
            print zan_str.group(1)
            print '-' * 15

            # 赞大于zan_th的回答才是需要的
            if int(zan_str.group(1)) >= ZhihuSpider.my_parse.zan_th:
                yield item
