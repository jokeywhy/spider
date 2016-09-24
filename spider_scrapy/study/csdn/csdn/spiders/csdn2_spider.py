# coding=utf-8
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from csdn.items import CsdnItem


class CSDN2Spider(CrawlSpider):
    '''继承自CrawlSpider, 实现自动爬取的爬虫。'''

    name = "csdn2"
    # 设置下延时
    # download_delay = 3
    allowed_domains = ['blog.csdn.net']
    # 第一篇文章地址
    start_urls = [
        'http://blog.csdn.net/u012150179/article/details/34486677'
    ]

    # rule编写法一，官方文档方式
    #    #提取“下一篇”的链接并**跟进**,若不使用restrict_xpaths参数限制，会将页面中所有
    #    #符合allow链接全部抓取
    #    Rule(SgmlLinkExtractor(allow=('/u012150179/article/details'),
    #                          restrict_xpaths=('//li[@class="next_article"]')),
    #         follow=True)
    #
    #    #提取“下一篇”链接并执行**处理**
    #    #Rule(SgmlLinkExtractor(allow=('/u012150179/article/details')),
    #    #     callback='parse_item',
    #    #     follow=False),
    # ]

    # rules编写法二，更推荐自己的方式（自己测验，使用法一时经常出现爬到中间就finish情况，并无错误码）
    rules = [
        Rule(LinkExtractor(allow=('/u012150179/article/details'), restrict_xpaths=('//li[@class="next_article"]')),
             callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        item = CsdnItem()
        sel = Selector(response)
        article_url = str(response.url)
        article_name = sel.xpath('//div[@id="article_details"]/div/h1/span/a/text()').extract()

        item['article_name'] = [n.encode('utf-8') for n in article_name]
        item['article_url'] = article_url.encode('utf-8')

        yield item
