# coding=utf-8
import codecs
import sys
from requests.packages.urllib3 import response

from scrapy import Spider
from scrapy import Request
from scrapy.selector import Selector
from google.items import GoogleItem

import sys

reload(sys)
sys.setdefaultencoding('utf8')


class GoogleSpider(Spider):
    name = 'google'
    # allowed_domains = ['google.com.hk']
    start_urls = [
        'https://www.google.com.hk/?gws_rd=cr,ssl#safe=strict&q=%E6%99%BA%E9%9A%9C&btnK=Google+%E6%90%9C%E7%B4%A2'
    ]

    def parse(self, response):
        # response.encoding = 'gbk'
        print response.text
        f = codecs.open('a.txt', mode='wb', encoding='utf-8')
        f.write(response.text)
        f.close()
        sel = Selector(response)
        item = GoogleItem()
        yield item
