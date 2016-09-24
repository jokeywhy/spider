# -*- coding: utf-8 -*-

import datetime,time
import codecs
import smtplib
from email_conf.mime.text import MIMEText
from email_conf.mime.image import MIMEImage
from email_conf.mime.multipart import MIMEMultipart
from email_conf.mime.application import MIMEApplication

import MySQLdb

from zhihu.spiders.zhihu_spider import *

def zan_cmp(a, b):
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
		self.receiver = ZhihuSpider.my_parse.receiver
		
	def read_answer(self, lst):
		order = 1
		l = len(lst)
		file_name = '%s.txt' % ZhihuSpider.my_parse.topic
		f = codecs.open(file_name, 'w')
		msg = MIMEMultipart("related")
		
		body = ''
		for answer in lst:
			f.write('%s个赞\n' % answer[1])
			f.write('时间%s\n' % time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(answer[2])))
			f.write('%s%s' % (answer[3], answer[4]))
			f.write('%s/%s\n' % (order, l))
			f.write('*' * 50)
			f.write('\n')
			'''body += "<h1>%s</h1>" % answer[3] # 问题
			body += "<p>%s个赞</p>" % answer[1]
			body += '<p>时间:%s</p>' % time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(answer[2]))
			body += '<p>%s</p>' % answer[4]
			body += '<p>%s/%s</p>' % (order, l)
			body += '<p>*********************************************************************</p>' '''
			body += "%s\n" % answer[3] # 问题
			body += "%s个赞\n" % answer[1]
			body += '时间:%s\n' % time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(answer[2]))
			body += '%s\n' % answer[4]
			body += '%s/%s\n' % (order, l)
			body += '*********************************************************************\n'
			order += 1
		f.close()
		'''if self.containsnonasciicharacters(body):
			msg_html = MIMEText(body.decode('utf-8','ignore').encode('utf-8'), 'html','utf-8')
		else:
			msg_html = MIMEText(body, 'html')  '''
		# msg_html = MIMEText(body, 'html')
		header = '<h1>抓抓小能手</h1>'
		msg_html = MIMEText(header, 'html')
		msg.attach(msg_html)
		
		part = MIMEApplication(body.decode('utf-8','ignore').encode('utf-8'))  
		part.add_header('Content-Disposition', 'attachment', filename=file_name.decode('utf-8').encode('gb2312'))  
		msg.attach(part) 
		##msg.attach(msg_html)
		self.send_email(self.receiver, msg)
		
	def containsnonasciicharacters(self, s):
		return not all(ord(c) < 128 for c in s) 
		
	def send_email(self, receiver, msg):
		"""
		1、receiver
		2、msg
		"""
		host = "smtp.qq.com"
		port = 465
		user = "714586001@qq.com"
		pwd = "wxq770260108"
		s = smtplib.SMTP_SSL(host, port)
		s.set_debuglevel(1)
		s.login(user, pwd)
		msg["subject"] = "topic:%s;zan>%s;time:%s天内" % (ZhihuSpider.my_parse.topic, ZhihuSpider.my_parse.zan, ZhihuSpider.my_parse.day)
		msg["from"] = '卖报小行家'
		msg["to"] = receiver
		# msg['Content-Type'] = "text/html; charset=utf-8"
		s.sendmail(user, receiver, msg.as_string())  # 给对方发邮件
		s.sendmail(user, user, msg.as_string()) # 给自己也发一份
		
		
	def start(self):
		month_time = 24 * 60 * 60 * ZhihuSpider.my_parse.day
		th_time = time.time() - month_time
		select_command = 'select * from %s where zan > %s ' % (ZhihuSpider.my_parse.table, ZhihuSpider.my_parse.zan)
		count = self.cur.execute(select_command + 'and publish_time > %s', th_time)
		results=self.cur.fetchall()
		lst = list(results)
		lst.sort(cmp = zan_cmp)
		self.read_answer(lst)
		self.cur.close()
		self.conn.close()

#GetInteresting().start()
