# -*- coding: utf-8 -*-
import json
import codecs
from csdn.email_conf import EmailConf

class CsdnPipeline(object):

    def __init__(self):
        self.file = codecs.open('a.txt', mode='wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        print line
        self.file.write(line.decode("unicode_escape").strip())
        return item

    def close_spider(self, spider):
        self.file.close()
        # email= EmailConf()
        # email.send_attach('a.txt')