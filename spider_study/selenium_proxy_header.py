# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def selenimu_proxy():
    service_args = [
        '--proxy=127.0.0.1:1080',
        '--proxy-type=socks5', # 支持http, socks5， https
    ]
    driver = webdriver.PhantomJS(service_args=service_args)
    # driver.get('https://www.google.com.hk/?gws_rd=cr,ssl#safe=strict&q=%E6%99%BA%E9%9A%9C')
    driver.get('http://www.ipchicken.com/')
    print driver.page_source

def selenimu_headers():
    service_args = [
        '--proxy=127.0.0.1:8888',
        '--proxy-type=http'
    ]
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap['phantomjs.page.settings.userAgent'] = (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0'
    )
    driver = webdriver.PhantomJS(service_args=service_args, desired_capabilities=dcap)
    driver.get('http://www.cqupt.edu.cn')

if __name__ == '__main__':
    selenimu_proxy()
    # selenimu_headers()