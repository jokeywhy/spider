# coding=utf-8
from pyquery import PyQuery as pq
from lxml import etree

# pyquery传值
def pyquery_normal():
    # 直接传字符串
    doc = pq("<html></html>") # doc现在就相当于jQuery里面的$符号
    # 用lxml补全下html代码
    doc = pq(etree.fromstring("<html></html>"))
    # 直接传URL
    doc = pq('http://www.baidu.com')
    # 传文件
    doc = pq(filename='save/hello2.html')

# pyquery基本应用
def pyquery_test():
    doc = pq(filename='save/hello2.html')
    print doc.html()
    print type(doc)
    li = doc('li')
    print type(li)
    print li.text()

# pyquery属性操作
def pyquery_property():
    p = pq('<p id="hello" class=hello></p>')('p')
    print p.attr('id')
    print p.attr('id', 'plop')
    print p.attr('id', 'hello')

    p = pq('<p id="hello" class="hello"></p>')('p')
    print p.add_class('beauty')
    print p.remove_class('hello')
    print p.css('font-size', '16px')
    print p.css({'backgroup-color':'yellow'})

# dom运算
def pyquery_dom():
    p = pq('<p id="hello" class="hello"></p>')('p')
    print p.append(' check out <a href="http://reddit.com/r/python"><span>reddit</spn></a>')
    print p.prepend('Oh yes!')
    d = pq('<div class="wrap"><div id="test"><a href="http://cuiqingcai.com">Germy</a></div></div>')
    p.prepend_to(d('#test'))
    print p
    print d
    d.empty()
    print d

# 遍历
def pyquery_bianli():
    doc = pq(filename='save/hello2.html')
    lis = doc('li')
    for li in lis.items():
        print li.html()
    print lis.each(lambda e: e)

# 网络请求
def pyquery_request():
    print pq('http://cuiqingcai.com', headers={'user-agent':'pyquery'})
    print pq('http://httpbin.org/post', {'foo':'bar'}, method='post', verify=True)

if __name__ == '__main__':
    # pyquery_test()
    # pyquery_property()
    pyquery_dom()
    # pyquery_bianli()
    # pyquery_request()