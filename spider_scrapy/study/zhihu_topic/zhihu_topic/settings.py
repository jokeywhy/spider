# -*- coding: utf-8 -*-

# Scrapy settings for zhihu_topic project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'zhihu_topic'

SPIDER_MODULES = ['zhihu_topic.spiders']
NEWSPIDER_MODULE = 'zhihu_topic.spiders'

ITEM_PIPELINES = {  
    'zhihu_topic.pipelines.ZhihuTopicPipeline': 800, 
}

DOWNLOADER_MIDDLEWARES = {  
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
        'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
        'zhihu_topic.spiders.rotate_useragent.RotateUserAgentMiddleware' :400  
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihu_topic (+http://www.yourdomain.com)'
