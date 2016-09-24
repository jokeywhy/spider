# coding=utf-8

from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from csdn.items import CsdnItem


class CSNDSpider(Spider):
    name = 'csdn'

    # 减慢爬行速度
    # download_delay = 1
    allowed_domains = ['blog.csdn.net']
    start_urls = [
        'http://blog.csdn.net/u012150179/article/details/34486677'
    ]

    def parse(self, response):
        sel = Selector(response)

        item = CsdnItem()

        article_url = str(response.url)
        article_name = sel.xpath('//div[@id="article_details"]/div/h1/span/a/text()').extract()

        item['article_name'] = [n.encode('utf-8') for n in article_name]
        item['article_url'] = article_url.encode('utf-8')

        yield item

        urls = sel.xpath('//li[@class="next_article"]/a/@href').extract()
        for url in urls:
            url = "http://blog.csdn.net" + url
            yield Request(url, callback=self.parse)