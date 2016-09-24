# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import re

import MySQLdb

class ZhihuTopicPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(
            host = 'localhost',
            user='root',
            passwd='',
            port=3306)
        self.cur = self.conn.cursor()
        
        try:
            self.cur.execute('create database if not exists zhihu')
        except MySQLdb.Error, e:
            print 'Mysql error %d: %s' % (e.args[0], e.args[1])
        self.conn.select_db('zhihu')
        try:
            self.cur.execute('create table topic(link_id int, followers int,topic varchar(64), paren_topic varchar(256), child_topic varchar(256), PRIMARY KEY (link_id))') # 主键
        except MySQLdb.Error, e:
            print 'Mysql error %d: %s' % (e.args[0], e.args[1])


    def process_item(self, item, spider):
        res_dict = dict(item)
        value = []
        for it in res_dict:
            reslut = re.findall("'(.*?)'", repr(res_dict[it]).decode('unicode_escape').encode('utf-8'), re.S)
            res_str = ''
            for i in reslut:
                res_str = '%s %s' % (res_str, i.strip())
            value.append(res_str.strip())
            
        value[0],value[1],value[2],value[3],value[4] = value[4],value[3],value[0],value[1],value[2]
        
        # 关注人数少于2000 不存储
        if value[1] == '' or long(value[1]) < 2000:
            return item
        
        # 只更新关注人数
        value.append(value[1])
        self.cur.execute('insert into topic values(%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE followers=%s', value)
                
        return item
