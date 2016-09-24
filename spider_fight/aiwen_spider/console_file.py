# coding=utf-8
import sys

'''
表示在输出的时候也能够很好将其保存到文件但是有弊端
'''
class __redirection__:

    def __init__(self):
        self.buff = ''
        self.__console__ = sys.stdout
        self.f = open('out.log', 'w')

    def write(self, output_stream):
        self.buff += output_stream

    def to_console(self):
        sys.stdout = self.__console__
        print self.buff

    def to_file(self):
        sys.stdout = self.f
        print self.buff

    def flush(self):
        self.buff=''
        self.f.close()

    def reset(self):
        sys.stdout=self.__console__
