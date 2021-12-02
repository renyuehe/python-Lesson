
##################### 介绍format 之前先介绍占位符
# %d
age= 29
print("my age is %d" %age)
#my age is 29


# %s
name= "makes"
print("my name is %s" %name)
#my name is makes


# %f
print("%6.3f" % 2.3)
#2.300
print("%f" %2.3)
#2.300000

######################### format 方法
# 位置映射
print("{}:{}".format('192.168.0.100',8888))
#192.168.0.100:8888

# 关键字映射
print("{server}{1}:{0}".format(8888,'192.168.1.100',server='Web Server Info :'))
#Web Server Info :192.168.1.100:8888　


# 元素访问
print("{0[0]}.{0[1]}".format(('baidu','com')))
#baidu.com　

# 对齐填充
print("{0}*{1}={2:0>2}".format(3, 2, 2 * 3))
# 3*2=06
