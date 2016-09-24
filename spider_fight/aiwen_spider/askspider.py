# coding=utf-8

import urllib
import urllib2
import re
import time
import page
import types
import mysql
import sys
from bs4 import BeautifulSoup


class Spider:
    # 初始化
    def __init__(self):
        self.page_num = 1
        self.total_num = None
        self.page_spider = page.Page()
        self.mysql = mysql.Mysql()

    # 获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))

    # 获取当前时间
    def getCurrentDate(self):
        return time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 通过网页的页码数来构建网页的URL
    def getPageURLByNum(self, page_num):
        page_url = "http://iask.sina.com.cn" + page_num
        return page_url

    # 通过传入网页页码来获取网页的HTML
    def getPageByNum(self, page_num):
        request = urllib2.Request(self.getPageURLByNum(page_num))
        try:
            response = urllib2.urlopen(request)
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print self.getCurrentTime(), "获取页面失败，错误代号", e.code
                return None
            if hasattr(e, "reason"):
                print self.getCurrentTime(), "获取页面失败，原因", e.reason
                return None
        else:
            page_my = response.read().decode('utf-8')
            return page_my

    # 获取所有的页码数
    def getTotalPageNum(self):
        print self.getCurrentTime(), "正在获取目录页面个数，请稍等"
        page_my = self.getPageByNum('/c/1073-all-1-new.html')
        # 匹配所有的页码数，\u4e0b\u4e00\u9875是下一页的UTF8编码
        pattern = re.compile(u'<a class="more" style="".*?<a.*?>(.*?)</a>.*?\u4e0b\u4e00\u9875</a>', re.S)
        match = re.search(pattern, page_my)
        if match:
            return int(match.group(1).encode('utf-8'))
        else:
            print self.getCurrentTime(), "获取总页码失败"

    # 获取下一页的Ip
    def getNextPage(self, html):
        pattern = re.compile(u'<a href="(.*?)".*?\u4e0b\u4e00\u9875</a>')
        match = re.search(pattern, html)
        if match:
            return match.group(1)
        else:
            return None

    # 分析问题的代码，得到问题的提问者，问题内容，回答个数，提问时间
    def getQuestionInfo(self, question):
        if not type(question) is types.StringType:
            question = str(question)
        pattern = re.compile(u'<div class="user-img">.*?<img.*?alt="(.*?)".*?</div>.*?<a href="(.*?)".*?>(.*?)</a>.*?answer_num.*?>(\d*).*?</span>.*?<span>(.*?)</span>', re.S)
        match = re.search(pattern, question)
        if match:
            # 获得提问者
            author = match.group(1)
            if author == '':
                author = '匿名用户'
            # 问题的链接
            href = match.group(2)
            # 问题的详情
            text = match.group(3)
            # 回答的个数
            ans_num = match.group(4)
            # 回答时间
            time = match.group(5)
            time_pattern = re.compile('\d{4}\-\d{2}\-\d{2}', re.S)
            time_match = re.search(time_pattern, time)
            if not time_match:
                time = self.getCurrentDate()
            return [author, href, text, ans_num, time]
        else:
            return None

    # 获取全部问题
    def getQuestions(self, page_num, page_id):
        # 获得目录页面的html
        page_my = self.getPageByNum(page_num)
        soup = BeautifulSoup(page_my, 'lxml')
        # 分析获得所有问题
        questions = soup.select("ul.list-group li")

        # 遍历每一个问题
        for question in questions:
            # 获得问题的详情
            info = self.getQuestionInfo(question)
            if info:
                # 得到问题的URL
                url = "http://iask.sina.com.cn" + info[1]
                # 通过URL来获取问题的最佳答案和其他答案
                ans = self.page_spider.getAnswer(url)
                print ans
                print self.getCurrentTime(), "当前爬取第", page_id, "的内容，发现一个问题", info[2], "回答数量", info[3]
                # 构造问题的字典，插入问题
                ques_dict = {
                    "text": info[2],
                    "questioner": info[0],
                    "date": info[4],
                    "ans_num": info[3],
                    "url": url
                }
                # 获得插入的问题的自增ID
                insert_id = self.mysql.insertData("iask_questions", ques_dict)
                # 得到最佳答案
                good_ans = ans[0]
                print self.getCurrentTime(), "保存到数据库， 此问题的ID为", insert_id
                # 如果存在最佳答案，那么就插入
                if good_ans:
                    print self.getCurrentTime(), insert_id, "号问题存在最佳答案", good_ans[0]
                    # 构造最佳答案的字典
                    good_ans_dict = {
                        "text": good_ans[0],
                        "answerer": good_ans[1],
                        "date": good_ans[2],
                        "is_good": str(good_ans[3]),
                        "question_id": str(insert_id)
                    }
                    # 插入最佳答案
                    if self.mysql.insertData("iask_answers", good_ans_dict):
                        print self.getCurrentTime(), "保存最佳答案成功"
                    else:
                        print self.getCurrentTime(), "保存最佳答案失败"

                    # 获得其他答案
                    other_anses = ans[1]
                    # 遍历每一个其他答案
                    for other_ans in other_anses:
                        # 如果答案存在
                        if other_ans:
                            print self.getCurrentTime(), insert_id, "号问题存在其他答案", other_ans[0]
                            # 构造其他答案的字典
                            other_ans_dict = {
                                "text": good_ans[0],
                                "answerer": good_ans[1],
                                "date": good_ans[2],
                                "is_good": str(good_ans[3]),
                                "question_id": str(insert_id)
                            }
                            # 插入这个答案
                            if self.mysql.insertData("iask_answers", other_ans_dict):
                                print self.getCurrentTime(), "保存其他答案成功"
                            else:
                                print self.getCurrentTime(), "保存其他答案失败"
        return page_my

    # 主函数
    def main(self):
        start_page = 1
        next_page = '/c/1073-all-1-new.html'
        page_file = open('page.txt', 'r')
        content = page_file.readline()
        if not content == '':
            start_page = int(content.strip())
            next_page = page_file.readline().strip()
        page_file.close()
        print self.getCurrentTime(), "开始页码", start_page
        print self.getCurrentTime(), "爬虫正在启动，开始爬去爱问知识人问题"
        self.total_num = self.getTotalPageNum()
        print self.getCurrentTime(), "获取到目录页面个数", self.total_num, "个"
        for x in range(start_page, self.total_num + 1):
            print self.getCurrentTime(), "正在抓取第", x, "个页面"
            try:
                page_my = self.getQuestions(next_page, x) # 要改的
            except urllib2.URLError, e:
                if hasattr(e, "reason"):
                    print self.getCurrentTime(), "某总页面内抓取或提取失败， 错误原因", e.reason
            except Exception, e:
                print self.getCurrentTime(), "某总页面内抓取或提取失败， 错误原因:", e
            if page_my:
                next_page = self.getNextPage(page_my)
            if next_page:
                f = open('page.txt', 'w')
                f.write(str(x + 1) + '\n')
                f.write(next_page)
                print self.getCurrentTime(), "写入新页码", x
                f.close()

spider = Spider()
spider.main()
# spider.getQuestions('/c/1073-all-1-new.html', 1)
