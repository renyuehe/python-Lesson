# 字符串是常量，不能被改变，只能重新赋值指向新的内存空间
#基本字符串
ss = "字符串"
print(type(ss))
c = 'c'
print(type(c))
sss = """
窗前明月光
疑似地上霜
"""
print(sss)
ssss = '''
举杯望明月
低头思故乡
'''
print(ssss)

#字符串格式化
a = 10;
b = 5;
print("{0}+{1}={2}".format(a, b, a+b))  # format 方式
print("%i + %i = %i"%(a, b, a+b))       # %i 方式
print("{0} + %i = {1}".format(a,a+b)%b) #可以混用，但不推荐

s = '1234abcd'

# 字符串切割
print(s[0:2])
print(s[1:2])
print(s[2:-2])
print(s[0:-1])
print(s[-1])
print(s[:])
print(len(s))
print(s[0:len(s)])

# 字符串方法
s = ' 1234 abcd '
print(s.title())
print(s.lower())
print(s.strip())
print(s.lstrip())
print(s.rstrip())