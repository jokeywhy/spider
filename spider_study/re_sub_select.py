#-*-coding:utf-8 -*-
# 此函数用替换第n个
# 使用方法：如果想替换第n个匹配，subExt('(reg)','replace',string,number=n);
#               如果想替换倒数第n个匹配，subExt('(reg)','replace',string,number=-n)
import re

def list_sub(pattern, repl, t, rep_nu, flags):
    t[rep_nu] = re.sub(pattern, repl, t[rep_nu], flags=flags)
    return "".join(t)

def subExt(pattern, repl, string, flags=0, number=1):
    match_list = re.split(pattern, string, flags=flags)
    match_nu = (len(match_list) - 1) / 2

    if match_nu < int(number):
        return string
    elif number >= 0:
        rep_nu = number * 2 - 1
        return list_sub(pattern, repl, match_list, rep_nu, flags=flags)
    else:
        rep_nu = (match_nu + number + 1) * 2 - 1
        return list_sub(pattern, repl, match_list, rep_nu, flags=flags)

text = '123abc3./sa8sa'
print subExt('(\d+)', '@', text, number=3)