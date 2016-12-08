# coding=utf-8
import bs4
import re

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = bs4.BeautifulSoup(html, "lxml")


# 获取标签属性内容
def soup_normal():
    print soup.prettify()  # 将他转换成标准的html
    print soup.a  # 根据标签获取内容
    print soup.head.name  # 获取标签name
    print soup.p.attrs  # 获取标签里面的属性
    print soup.p['class']  # 获取class属性
    print soup.p.get('class')  # 同上


# 修改属性
def soup_chageatr():
    soup.p['class'] = 'newClass'
    print soup.p


# 获取标签内的文字
def soup_string():
    print soup.p.string  # NavigableString类型


# 对注释处理
def soup_note():
    print soup.a
    print soup.a.string
    print type(soup.a.string)  # comment类型
    if type(soup.a.string) == bs4.element.Comment:
        print soup.a.string


# 文档树的遍历子节点
def soup_iterator1():
    print soup.p.contents  # 将子节点以列表的方式输出
    # 获取所有的子节点
    for child in soup.body.children:
        print child
    # 获取所有子孙节点
    for child in soup.descendants:
        print child
    # 获取多个内容
    for string in soup.stripped_strings:  # stripped_strings可以去除空行空格
        print repr(string)

# 文档树的遍历父节点
def soup_iterator2():
    # 父节点获取
    p = soup.p
    print p.parent.name
    content = soup.head.title.string
    print content.parent.name
    # 全部父节点获取
    content = soup.head.title.string
    for parent in content.parents:
        print parent.name


# 文档树的遍历兄弟节点
def soup_iterator3():
    # 空白换行也可以被视作一个节点
    print soup.p.next_sibling
    print soup.p.prev_sibling
    print soup.p.next_sibling.next_sibling
    # 返回全部的兄弟节点(迭代输出，previous_siblings同样)
    for sibling in soup.a.next_siblings:
        print repr(sibling)


# 文档树的遍历前后节点
def soup_iterator4():
    # 节点包含所有的节点里面的内容
    print soup.head.next_element
    print soup.head.previous_element
    # 所有前后节点
    for element in soup.a.next_element.next_element.next_element.next_element.next_element.next_element.next_elements:
        print repr(element)


# 搜索型文档树
def soup_find():
    # 找出所有节点
    # 传字符串
    print soup.find_all('b')
    # 传正则表达式
    for tag in soup.find_all(re.compile("^b")):
        print tag.name
    # 传列表
    print soup.find_all(['a', 'b'])
    # 传True
    for tag in soup.find_all(True):
        print tag.name

    # 传方法
    def has_class_but_no_id(tag):
        return tag.has_attr('class') and not tag.has_attr('id')

    print soup.find_all(has_class_but_no_id)


# keyword参数
def soup_keyword():
    print soup.find_all(id='link2')
    print soup.find_all(href=re.compile('elsie'))
    print soup.find_all(href=re.compile('elsie'), id='link1')
    print soup.find_all('a', class_='sister')  # class关键词过滤
    # 有些tag属性在搜索时不能使用，HTML5 data-*属性
    data_soup = bs4.BeautifulSoup('<div data-foo="value">foo!</div>', 'lxml')
    print data_soup.find_all(attrs={"data-foo": "value"})

# soup参数
def soup_text():
    # text参数
    print soup.find_all(text='Lacie')
    print soup.find_all(text=['Tillie', 'Elsie', 'Lacie'])
    print soup.find_all(text=re.compile('Dormouse'))
    # limit参数
    print soup.find_all('a', limit=2)
    # recursive 为False表示只搜索tag的直接子节点
    print soup.html.find_all('title')
    print soup.html.find_all('title', recursive=False)

# css 选择器
def soup_css():
    # 通过标签名查找
    print soup.select('title')
    print soup.select('a')
    print soup.select('b')
    # 通过类名查找
    print soup.select('.sister')
    # 通过id名查找
    print soup.select('#link1')
    # 组合查找
    print soup.select('p #link1')
    # 子标签查找
    print soup.select("head > title")
    # 属性查找
    print soup.select('a[class="sister"]')
    print soup.select('a[href="http://example.com/elsie"]')
    print soup.select('p a[href="http://example.com/elsie"]')

# select 遍历
def soup_bianli():
    soup = bs4.BeautifulSoup(html, 'lxml')
    print type(soup.select('title'))
    print soup.select('title')[0].get_text()

    for title in soup.select('title'):
        print title.get_text()



if __name__ == '__main__':
    # soup_iterator1()
    # soup_iterator2()
    # soup_iterator3()
    # soup_iterator4()
    # soup_find()
    # soup_keyword()
    # soup_text()
    soup_css()
    # soup_bianli()