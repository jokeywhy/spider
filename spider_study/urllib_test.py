# coding=utf-8
import urllib
import urllib2
import cookielib


# get 请求
def url_get():
    request = urllib2.Request('http:www.baidu.com')
    response = urllib2.urlopen(request)
    print response.read()


# post 请求
def url_post():
    values = {"username": "123@qq.com", "password": "abc123"}
    data = urllib.urlencode(values)
    url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    print response.read()


# 带header头的请求
def url_header():
    url = 'http://webxss.net/index.php?do=login&act=submit'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
    referer = 'http://webxss.net/index.php?do=login'
    content_type = 'application/x-www-form-urlencoded'
    values = {'user': 'jkwhy', 'pwd': 'jokeywhy123'}
    headers = {'User-Agent': user_agent, 'Content-Type': content_type, 'Referer': referer}
    data = urllib.urlencode(values)
    request = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(request)
    page = response.read()
    print page


# urllib2 代理设置
def url_proxy():
    enable_proxy = True
    proxy_handler = urllib2.ProxyHandler({"http": 'http://127.0.0.1:1080'})
    null_proxy_handler = urllib2.ProxyHandler({})
    if enable_proxy:
        opener = urllib2.build_opener(proxy_handler)
    else:
        opener = urllib2.build_opener(null_proxy_handler)
    urllib2.install_opener(opener)
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
    referer = 'http://www.ipchicken.com/'
    headers = {'User-Agent': user_agent, 'Referer': referer}
    request = urllib2.Request('http://www.ipchicken.com/', '', headers)
    response = urllib2.urlopen(request)
    print response.read()

# cookie 保存到变量
def cookie_vari():
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    for item in cookie:
        print 'Name = ' + item.name
        print 'Value = ' + item.value


# cookie保存到文件
def cookie_file():
    filename = 'save/cookie.txt'
    cookie = cookielib.MozillaCookieJar(filename)
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)

    response = urllib2.urlopen('http://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)


# cookie从文件中获取
def cookie_getfile():
    cookie = cookielib.MozillaCookieJar()
    cookie.load('save/cookie.txt', ignore_discard=True, ignore_expires=True)
    req = urllib2.Request("http://www.baidu.com")
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open(req)
    print response.read()

# 调试状态
def url_debuglog():
    httpHandler = urllib2.HTTPHandler(debuglevel=1)
    httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
    opener = urllib2.build_opener(httpHandler, httpsHandler)
    urllib2.install_opener(opener)
    response = urllib2.urlopen('http://www.baidu.com')


# 异常状态的抛出
def url_except():
    req = urllib2.Request('http://blog.csdn.net/cqcre')
    # try:
    #     response = urllib2.urlopen(req, timeout=10)
    #     print response.read
    # except urllib2.HTTPError, e:
    #     print e.code
    #     print e.reason

    #父类异常写在子类异常后面
    try:
        urllib2.urlopen(req, timeout=10)
    except urllib2.HTTPError, e:
        print e.code
        print e.reason
    except urllib2.URLError, e:
        print e.reason
    else:
        print "OK"


if __name__ == '__main__':
    # url_proxy()
    # url_debuglog()
    url_except()
