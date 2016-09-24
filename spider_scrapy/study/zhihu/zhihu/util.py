#coding:utf-8

import ConfigParser

import MySQLdb

class MyParse(object):
    """
    a) 获取话题的链接 topic_url
    b) 获取表(link_id)的名称 link_id
    c) 获取赞阈值 zan_th
    d) 获取赞页数 pages
    e) 名称 topic
    f) 表名称 table
    
    g) 多少天之内才会被获取 day
    h) 多少赞才会被获取 zan
    """
    def __init__(self):
        cf = ConfigParser.ConfigParser()
        cf.read("/home/wang/python/scrapy/zhihu/zhihu/config.ini")
        self.topic = cf.get("setting", "topic")
        self.pages = cf.getint("setting", "pages")
        self.zan_th = cf.getint("setting", "zan_th")
        
        self.day = cf.getint('getinterest', 'day')
        self.zan = cf.getint('getinterest', 'zan')
        self.receiver = cf.get('getinterest', 'receiver')
        
        conn = MySQLdb.connect(
            host='localhost',
            user = 'root',
            passwd = '',
            port = 3306)
        cur = conn.cursor()
        conn.select_db('zhihu')
        
        cur.execute('select * from topic where topic = %s', self.topic)
        result = cur.fetchall()
        
        self.link_id = result[0][0]
        self.topic_url = 'http://www.zhihu.com/topic/%s/questions/' % self.link_id
        
        if cmp(self.topic, '电影') == 0:
            self.table = 'movie'
        elif cmp(self.topic, '编程') == 0:
            self.table = 'coding'
        else:
            self.table = 'table%s' % self.link_id
        
        cur.close()
        conn.close()
        