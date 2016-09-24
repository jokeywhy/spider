#coding=utf-8
import re

# 参数flag
# re.I(全拼：IGNORECASE): 忽略大小写（括号内是完整写法，下同）
# re.M(全拼：MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
# re.S(全拼：DOTALL): 点任意匹配模式，改变'.'的行为
# re.L(全拼：LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
# re.U(全拼：UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
# re.X(全拼：VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。

# 正则基本测试
def re_test():
    pattern = re.compile(r'hello')
    result1 = re.match(pattern, 'hello')
    result2 = re.match(pattern, 'helloo CQC!')
    result3 = re.match(pattern, 'helo CQC!')
    result4 = re.match(pattern, 'hello CQC!')

    if result1:
        print result1.group()
    else:
        print '1匹配失败！'

    if result2:
        print result2.group()
    else:
        print '2匹配失败！'

    if result3:
        print result3.group()
    else:
        print '3匹配失败！'

    if result4:
        print result4.group()
    else:
        print '4匹配失败！'

# 正则的选取group的方式
def re_group():
    m = re.match(r'(\w+)(\w+)(?P<sign>.*)', 'hello world')

    print "m.string:", m.string
    print "m.re:", m.re
    print "m.pos:", m.pos
    print "m.endpos:", m.endpos
    print "m.lastindex:", m.lastindex
    print "m.lastgroup:", m.lastgroup
    print "m.group:", m.group()
    print "m.group(1,3):", m.group(1, 3)
    print "m.groups():", m.groups()
    print "m.groupdict():", m.groupdict()
    print "m.start(2):", m.start(2)
    print "m.end(2):", m.end(2)
    print "m.span(2):", m.span(2)
    print r"m.expand(r'\g \g \g'):", m.expand(r'\2 \1\3')

# 正则search
def re_search():
    pattern = re.compile(r'world')
    match = re.search(pattern, 'hello world!')
    if match:
        print match.group()

# 正则split
def re_split():
    pattern = re.compile(r'\d+')
    print re.split(pattern, 'one1two2three3four4')

# 正则findall
def re_findall():
    pattern = re.compile(r'\d+')
    print re.findall(pattern, 'one1two2three3four4')

# 正则sub(替换)
def re_sub():
    pattern = re.compile(r'(\w+) (\w+)')
    s = 'i say, hello world!'
    print re.sub(pattern, r'\2 \1', s)
    def func(m):
        return m.group(1).title() + ' ' + m.group(2).title()
    print re.sub(pattern, func, s)

# 正则subn(有次数返回)
def re_subn():
    pattern = re.compile(r'(\w+) (\w+)')
    s = 'i say, hello world'

    print re.subn(pattern,r'\2 \1', s)

    def func(m):
        return m.group(1).title() + ' '+ m.group(2).title()

    print re.subn(pattern, func, s)

if __name__ == '__main__':
    # re_test
    # re_group()
    # re_search()
    # re_split()
    # re_findall()
    re_sub()
    # re_subn()