import zipfile
import random
import datetime
import sys
import threading

global i, pwd, pdict, flag
flag = False  # 用来判断是否找到了密码
i = 0  # 密码的生成位数，在递归中用到
pwd = str()  # 密码测试的字符串
pdict = '0123456789'  # 定义的密码字典，密码中所有出现的字符来自于此

pwds = []
def redict( loop):  # 递归顺序输出所有的排列组合的可能情况
    if flag:
        return
    global i, pdict, pwd
    i += 1
    if i > loop:
        return
    for d in pdict:
        pwd = pwd[:i - 1] + d
        if len(pwd) == 4:
            print(pwd)
            pwds.append(pwd)
        if i < loop:
            redict( loop)
            i -= 1
        else:  # 创建线程去执行测试密码的函数，加快破译速度
            ...

def extract():
    for pnum in range(1, 11):  # 定义破解的密码位数
        global loop, i, pwd
        pwd = '0'
        i = 0
        redict(pnum)
        if flag:
            break

if __name__ == '__main__':
    extract()
    print(pwds.__len__())

