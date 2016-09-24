# coding=utf-8
import smtplib
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

# 邮件
class EmailConf(object):
    def __init__(self):
        self.host = 'smtp.qq.com'
        self.port = 465
        self.user = '2469763120@qq.com'
        self.pwd = 'ffvhauxlliliecgh'
        self.receiver = ['425317014@qq.com']
        self.s = smtplib.SMTP_SSL(self.host, self.port)
        self.s.login(self.user, self.pwd)

    # 发送不带附件的email
    def send_email(self):
        message = MIMEText('爬虫跑完了啊！', 'plain', 'utf-8')
        message['From'] = Header('我的爬虫', 'utf-8')
        message['To'] = Header('jokeywhy', 'utf-8')

        subject = '赶紧去看看啊啊啊！！！'
        message['Subject'] = Header(subject, 'utf-8')

        self.s.sendmail(self.user, self.receiver, message.as_string())
        self.s.quit()
        print '成功通知~_~!'

    # 发送带附件的email
    def send_attach(self, filename):
        message = MIMEMultipart()
        msg = MIMEText('<h1>爬虫通知</h1>', 'html')
        message.attach(msg)

        fp = open(filename, 'rb')
        part = MIMEApplication(fp.read())
        part.add_header('Content-Disposition', 'attachment', filename=filename)
        message.attach(part)
        fp.close()

        message['Subject'] = '爬虫完成'
        message['From'] = 'jkw<2469763120@qq.com>'
        message['To'] = 'jokeywhy'
        self.s.sendmail(self.user, self.receiver, message.as_string())
        print u'发送成功'
