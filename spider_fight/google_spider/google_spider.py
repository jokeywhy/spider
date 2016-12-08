# coding=utf-8
import re
from selenium import webdriver
import threading
import bs4
import os
from urlparse import urljoin
import urllib

class GoogleSpider(object):

    def __init__(self, url):
        self.current_url = url
        service_args = [
            '--proxy=127.0.0.1:1080',
            '--proxy-type=socks5',  # 支持http, socks5， https
        ]
        self.driver = webdriver.PhantomJS(service_args=service_args)

    def re_soup(self, pagesource):
        soup = bs4.BeautifulSoup(pagesource, 'lxml')
        urls = soup.select('h3.r > a')
        next_soup = soup.select('td[style="text-align:left"] > a')
        file = open('result.txt', 'a')
        for url in urls:
            pattern = re.compile(r'\/url\?q=(.*?)&amp;sa=U', re.S)
            herf = re.search(pattern, str(url))
            if herf:
                # print urllib.unquote(herf.group(1))
                file.write('{}\n'.format(urllib.unquote(herf.group(1))))
        file.close()
        if next_soup:
            pattern_next = re.compile(r'href=\"(.*?)\"', re.S)
            next_page = re.search(pattern_next, str(next_soup[0]))
            if next_page:
                print self.current_url
                self.current_url = urljoin(self.current_url, next_page.group(1))
                self.current_url = self.current_url.replace('&amp;', '&')
                self.selenimu_reqproxy()

    def selenimu_reqproxy(self):
        self.driver.get(self.current_url)
        self.re_soup(self.driver.page_source)

    def run(self):
        if os.path.exists('result.txt'):
            os.remove('result.txt')
        self.selenimu_reqproxy()

if __name__ == "__main__":
    url = 'https://www.google.com.hk/?gws_rd=cr,ssl#safe=strict&q=1' #搜索标签为'厉害'

    googles = GoogleSpider(url)
    googles.run()
