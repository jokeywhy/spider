# -*- coding: utf-8 -*-

import datetime,time

import MySQLdb

def followers_cmp(a, b):
	return -cmp(a[1], b[1])

class GetInteresting:
	def __init__(self):
		self.conn = MySQLdb.connect(
			host='localhost',
			user = 'root',
			passwd = '',
			port = 3306)
		self.cur = self.conn.cursor()
		self.conn.select_db('zhihu')
		
	def read_answer(self, lst):
		order = 1
		l = len(lst)
		f = open('topic.txt', 'w');
		for answer in lst:
			f.write( '%s followers\n' % answer[1])
			f.write( 'topic:%s\n' % answer[2])
			f.write( 'parents_topic:%s\n' % answer[4])
			f.write( 'child_topic:%s\n' % answer[3])
			f.write( '%s/%s\n' % (order, l))
			f.write( '*' * 50)
			f.write( '\n')
			order += 1
			
		
	def start(self):
		#count = self.cur.execute('select * from topic')
		topic = '电影'
		count = self.cur.execute('select * from topic')
		result = self.cur.fetchall()
		lst = list(result)
		#results=self.cur.fetchall()
		#lst = list(results)
		lst.sort(cmp = followers_cmp)
		self.read_answer(lst)
		
		
GetInteresting().start();