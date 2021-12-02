# 反射
# 3w 1h
# 　what 是什么
# 反射 使用字符串数据类型的变量名来获取这个变量的值
# a = 1
# b = 2
# name = 'alex'
# why 为什么 三个场景
# input
# 用户输入得到如果是a，那么就打印1，如果输入的是b，就打印2，如果输入的是name，就打印alex
# 文件
# 从文件中独出的字符串，想转换成变量的名字
# 网络
# 将网络传输的字符串转换成变量的名字
# where 在哪用
# how 怎么用
# hasttr
# getattr

# 反射类中的变量: 静态属性,类方法,静态方法
# class Foo:
#     School = 'oldboy'
#     Country = 'china'
#     Language = 'chinese'

#     @classmethod
#     def class_method(cls):
#         print(cls.School)
#     @staticmethod
#     def static_method():
#         print('in static mehtod')
#     def wahaha(self):
#         print('wahaha')

# 条件判断实现
# print(Foo.School)
# print(Foo.Country)
# print(Foo.Language)

# 反射实现
# while 1:
#     inp = input('>>>')
#     if hasattr(Foo,inp):
#         print(getattr(Foo,inp))
# if inp == 'School':print(Foo.School)
# if inp == 'Country':print(Foo.Country)
# if inp == 'Language':print(Foo.Language)

# 解析getattr方法
# getattr(变量名：命名空间,字符串；属于这个命名空间内的变量名)
# getattr(Foo,'School') # Foo.School
# print(getattr(Foo,'class_method')) # Foo.class_method()
# getattr(Foo,'static_method')() # Foo.static_method()
# getattr(Foo,'wahaha')(1) # Foo.wahaha()
# getattr(Foo,'shuangwaiwai') Foo.shuangwaiwai
# print(hasattr(Foo,'wahaha'))
# print(hasattr(Foo,'shaungwaiwai'))

# 反射对象中的变量
# 对象属性
# 普通方法
# class Foo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def eating(self):
#         print('%s is eating' % self.name)
#

# alex = Foo('alex_sb',83)
# print(getattr(alex,'name'))
# print(getattr(alex,'age'))
# getattr(alex,'eating')()

# 反射模块中的变量
import os  # os 就是一个模块
# os.rename('D:\Files\Desktop\python\python\汇总','D:\Files\Desktop\python\python\python汇总')
# getattr(os,'rename')('D:\Files\Desktop\python\python\python汇总','D:\Files\Desktop\python\python\汇总')

# 反射本文件的变量
# a = 1
# b = 2
# name = 'alex'
# def qqxing():
#     print('qqxing')

# cls.xxx
# obj.xxx
# os.xxx

# 分析过程
# import sys
# # print(sys.modules['__main__'])
# # print(sys.modules['__main__'].a)
# print([__name__]) # 变量,内置的变量
# print(sys.modules[__name__]) # 反射本文件中的变量 固定的使用这个命名空间

# 反射本文件中的变量 结论
# import sys
# print(sys.modules[__name__])
# print(getattr(sys.modules[__name__],'a'))
# print(getattr(sys.modules[__name__],'b'))
# print(getattr(sys.modules[__name__],'name'))
# getattr(sys.modules[__name__],'qqxing')()
# print(getattr(sys.modules[__name__],'Foo'))
# obj = getattr(sys.modules[__name__],'Foo')()
# print(obj)

# setattr
# class Foo:
#     Country = 'china'
# def func():
#     print('qqxing')
# Foo.School = 'oldboy'
# setattr(Foo,'School','oldboy')  # 接收三个参数 命名空间 '变量名' 变量值
# print(Foo.__dict__)
# print(getattr(Foo,'School'))
# print(Foo.School)

# setattr(Foo,'func',func) # 一般没人往空间中添加函数
# print(Foo.__dict__)
# print(Foo.func)

# delattr
# del Foo.Country
# print(Foo.__dict__)
# delattr(Foo,'Country')
# print(Foo.__dict__)

# hasattr()
# getattr()
# setattr()
# delattr()

# 反射类中的变量
# 发射对象中的变量
# 反射模块中的变量
# 反射本文件中的变量

# 用反射的场景
# input
# 网路
# 文件

# 内置方法
# 在不是需要程序来程序员定义,本身就存在在类中的方法就是内置方法
# 内置的方法通常都长这样:__名字__
# 名字: 双下方法 魔法方法 内置方法

# __init__
# 不需要我们主动调用,而是在实例化的时候内部自动执行
# 所有的双下方法,都不需要我们直接去调用,都有另外一种自动触发它的语法

# __str__ __repr__
# class Course:
#     def __init__(self,name,period,price,teacher):
#         self.name = name
#         self.period = period
#         self.price = price
#         self.teacher = teacher
#

#     def __str__(self):
#         return 'str : %s %s %s %s' % (self.name, self.period, self.price, self.teacher)
#
#     def __repr__(self):
#         return 'repr : %s %s %s %s' % (self.name, self.period, self.price, self.teacher)
#

# course_lst = []
# python = Course('python','6 month',29800,'boss_jin')
# course_lst.append(python)
# linux = Course('linux','5 month',25800,'oldboy')
# course_lst.append(linux)
# for id,course in enumerate(course_lst,1):
#     print(id,course)
#     print('%s %s'%(id,course))
#     print(str(course))
#     print(repr(course))
#     print('%r' % course)

# 当你打印一个对象的时候    触发__str__
# 当你使用%s格式化的是否    触发__str__
# str强制转换数据类型的时候  触发__str__

# __repr__
# repr是str的备胎
# 有__str__的是否执行__str__,没有实现__str__的是否,执行__repr__
# repr(obj)内置函数对应的结果是__repr__的返回值
# 当你使用%r格式化的时候 触发__repr__

# 学生选择课程的时候,要显示所有的课程
# class Foo:
#     def __str__(self):
#         return 'Foo.str'
#     def __repr__(self):
#         return 'Foo.repr'
#

# class Son(Foo):
#     # def __str__(self):
#     #     return 'Son.str'
#

#     def __repr__(self):
#         return 'Son.repr'
#

# s1 = Son()
# print(s1)