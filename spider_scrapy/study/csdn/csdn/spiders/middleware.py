import base64
import random
from csdn import settings


class RotateUserAgent(object):
    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))
    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        proxy = random.choice(settings.PROXIES)
        if proxy['user_pass'] != '':
            request.meta['proxy'] = "http://%s" % proxy['ip_port']
            encoded_user_pass = base64.encodestring(proxy['user_pass'])
            request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
            print "********************ProxyMiddleware have pass******************" + proxy['ip_port']
        else:
            print "********************ProxyMiddleware no pass******************" + proxy['ip_port']
            request.meta['proxy'] = "http://%s" % proxy['ip_port']