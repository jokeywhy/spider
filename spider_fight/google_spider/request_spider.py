# coding=utf-8
import re
from urlparse import urljoin

import requests
from lxml import etree
from Queue import Queue
import thread
import threading
from multiprocessing.dummy import Pool
import tool

class GoogleSpider(object):

    def __init__(self):
        self.lock = threading.Lock()
        self.s = requests.Session()

    def requestG(self, url):
        headers ={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }
        # proxies = {
        #     "http": "http://127.0.0.1:1080",
        #     "https": "http://127.0.0.1:1080",
        # }
        response = self.s.get(url, headers=headers).text
        # html = etree.HTML(response.encode('utf-8'))
        # response = etree.tostring(html)
        mytool = tool.Tool()
        response = mytool.replace(response.encode('utf-8'))
        gSpider.getSoup(response, url)


    def threadherf(self, htmlherf):
        # pattern = re.compile(u'replace\("(.*?)"', re.S)
        follow = requests.get(htmlherf, timeout=5)

        follow.encoding = 'utf-8'
        # url = re.search(pattern, follow.text).group(1)
        self.lock.acquire()
        print follow.url
        self.lock.release()

    def getSoup(self, response, url):
        pattern1 = re.compile(r'<h3.*?<a.*?href="(.*?)"', re.S)
        pattern2 = re.compile(r'<a href="([^<>]*?)" class="n">(?=下一页)')
        htmlherfs = re.findall(pattern1, response)
        pool = Pool(10)
        for htmlherf in htmlherfs:
            pool.apply_async(func=self.threadherf, args=(htmlherf,))
        pool.close()
        pool.join()
        nextherf = re.search(pattern2, response)
        print '------------------------------------------------'
        print nextherf.group()
        if nextherf.group():
            nexturl = urljoin(url, nextherf.group(1))
            print nextherf.group(1)
            self.requestG(nexturl)
        else:
            print 'search over'


if __name__ == '__main__':
    url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=2&tn=baiduhome_pg&wd=inurl%3Ajjj.asp&rsv_spt=1&oq=inurl%3Ajjj.asp&rsv_pq=b67b96db00005d6e&rsv_t=b22cQuDkkbPisBTOMOZhfgTnXwBQzq34KAknZx%2F136GPDmC560PfD1EpVmgDZgtt%2Bq1l&rqlang=cn&rsv_enter=0'
    gSpider = GoogleSpider()
    gSpider.requestG(url)

