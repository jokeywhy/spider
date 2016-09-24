# coding=utf-8
from lxml import etree
'''
//是指代标签，/指代子元素
'''
text = '''
<div>
<ul>
     <li class="item-0"><a href="link1.html">first item</a></li>
     <li class="item-1"><a href="link2.html">second item</a></li>
     <li class="item-inactive"><a href="link3.html">third item</a></li>
     <li class="item-1"><a href="link4.html">fourth item</a></li>
     <li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''

# 完善和修复html代码
def lxml_normal():
    html = etree.HTML(text)
    result = etree.tostring(html)
    print result

# 读取file html代码并修复
def lxml_file():
    html = etree.parse('save/hello.html')
    result = etree.tostring(html, pretty_print=True)
    print result

# XPath实例
def lxml_xpath():
    # 获取所有<li>标签
    html = etree.parse('save/hello.html')
    print type(html)
    result = html.xpath('//li')
    print result
    print len(result)
    print type(result)
    print type(result[0])

    # 获取<li>标签的所有class
    result = html.xpath('//li/@class')
    print result

    # 获取<li>标签下href为 link1.html的<a>标签
    result = html.xpath('//li/a[@href="link1.html"]')
    print result

    # 获取<li>标签下的所有<span>标签
    result = html.xpath('//li//span')
    print result

    # 获取<li>标签有class,不获取<li>class元素
    result = html.xpath('//li/a//@class')
    print result

    # 获取最后一个<li>的<a>的href
    result = html.xpath('//li[last()]/a/@href')
    print result

    # 获取倒数第二个元素的内容
    result = html.xpath('//li[last()-1]/a')
    print result[0].text

    # 获取class为bold的标签名
    result = html.xpath('//*[@class="bold"]')
    print result[0].tag

if __name__ == '__main__':
    # lxml_normal()
    # lxml_file()
    lxml_xpath()