# coding=utf-8
import random

class RotateUserAgent(object):
    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        header = random.choice(self.agents)
        print header
        request.headers.setdefault('User-Agent', header)

class ProxyMiddleware(object):

    def process_request(self, request, spider):
        proxy = 'http://127.0.0.1:1080'
        print proxy
        request.meta['proxy'] = proxy

