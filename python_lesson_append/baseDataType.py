import sys

#注意：在Python中，不允许自己定义和关键字相同名字的标识符。
#

# 不可变数据（3 个）：Number（数字）、str（字符串）、tuple（元组）；
# 可变数据（3 个）：list（列表）、dict（字典）、set（集合）。

########################################################
# 其中 Number（数字）支持 int、float、bool、complex（复数）。

number = 3
print(type(number)) #int

real = 3.3333333
print(type(real)) #float

b = True
print(type(b))

cpx = 2 + 3j
print(type(cpx))

########################################################

ss = "字符串"
print(type(ss)) #str

c = 'c'
print(type(c)) #str

arr = [1,1,2]
print(type(arr)) #list

tup = (1,1,2)
print(type(tup)) #tuple

set = {1,1,2}
print(type(set)) #set

dic = {1:'one',1:"one",2:"two"}
print(type(dic)) #dict

#打印当前行
print(sys._getframe().f_lineno)








