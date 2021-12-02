
#打印
print("nihaoma", end='')    #不换行
print('nihaoma')            #自动换行
print("张三", "李四", "王五")   #自带空格
print("\"\"")               #转义字符
print("000\aa")
print("000\bb")             #退格
print("000\ff")             #换页？
print("000\tt")             #八个空格
print("000\\反斜杠")    #反斜杠
print("000\nn")         #换行
print("000123123123\rr11")         #返回文本行首

#打印当前行
import sys
print(sys._getframe().f_lineno)

#变量： int型，float型，bool型，complex型
number = 3
print(type(number))
real = 3.333
print(type(real))
real2 = 3.1e-3
print(real2)
real3 = 3.14e3
print(real3)
b = True
print(type(b))
cpx = 2 + 3j
print(type(cpx))

#进制转换
number = 10;
print(bin(number))
print(oct(number))
print(int(number))
print(hex(number))

#字符串，数组，元组，集合，字典
ss = "字符串"
print(type(ss))
c = 'c'
print(type(c))

arr = [1, 1, 2]
print(type(arr))
tup = (1, 1, 2)
print(type(tup))
set = {1, 2, 3}
print(type(set))
dic = {1: "one", 2: "two"}
print(type(dic))

#多目标赋值 方式
a, b = 3, 4
print(a,b)

"""
#交换1
c = a
a = b
b = c
#交换2
a = a+b
b = a-b
a = a-b
#交换3
a = a ^ b
b = a ^ b
a = a ^ b
#交换4
a,b = b,a
"""




