# coding=utf-8
from urlparse import urljoin

url = urljoin('http://www.asite.com/folder/currentpage.html', 'anotherpage.html')
print url
url = urljoin('http://www.asite.com/folder/currentpage.html', 'folder2/anotherpage.html')
print url
url = urljoin('http://www.asite.com/folder/currentpage.html', '/folder3/anotherpage.html')
print url
url = urljoin('http://www.asite.com/folder/currentpage.html', '../finalpage.html')
print url
url = urljoin('http://www.asite.com/folder/currentpage.html', 'http://www.baidu.com/1.txt')
print url
