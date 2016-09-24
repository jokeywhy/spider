# coding=utf-8
import urllib2
import cookielib


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


if __name__ == '__main__':
    cookie_file()
    # cookie_getfile()
