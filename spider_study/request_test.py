# coding=utf-8
import json

import requests

# 普通请求
def request_normal():
    r = requests.get('http://www.baidu.com')
    print type(r)
    print r.status_code
    print r.encoding
    print r.text
    print r.cookies

# get请求
def request_get():
    payload = {'key1': 'value1', 'key2': 'value2'}
    headers = {'content-type': 'application/json'}
    r = requests.get("http://httpbin.org/get", params=payload, headers=headers)
    print r.url

# post请求
def request_post():
    url = 'http://httpbin.org/post'
    payload = {'key1':'value1', 'key2':'value2'}
    # 普通请求
    r = requests.post(url, data=payload)
    # post json数据
    r = requests.post(url, data=json.dumps(payload))
    # 上传文件
    files = {'file': open('test.txt', 'rb')}
    r = requests.post(url, files=files)
    # 流式上传
    with open('massive-body') as f:
        requests.post('http://some.url/streamed', data=f)
    print r.text

# cookie包含
def request_cookie():
    url = 'http://example.com'
    r = requests.get(url)
    # 包含cookie
    cookie = dict(cookies_are='working')
    r = requests.get(url, cookies=cookie)
    print r.cookies
    print r.cookies['example_cookie_name']

# 会话
def rquest_session():
    s = requests.Session()
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
    r = s.get("http://httpbin.org/cookies")

    # 传递header
    s = requests.Session()
    s.headers.update({'x-test': 'true'})
    r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})  # 不想要header的全局变量可以用headers={'x-test': None}

    print r.text

# ssl证书
def request_ssl():
    r = requests.get('https://kyfw.12306.cn/otn', verify=False) # 判断是否要证书
    print r.text

# 代理设置
def request_proxy():
    proxies = {
        "http": "http://127.0.0.1:1080",
        "https": "http://127.0.0.1:1080",
    }
    r = requests.post("http://httpbin.org/post", proxies=proxies)
    print r.text

if __name__ == '__main__':
    # request_ssl()
    request_proxy()