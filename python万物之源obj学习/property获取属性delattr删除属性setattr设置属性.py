#!/usr/bin/env python
# coding=utf-8
# class_propertiemethod.py 属性方法
# 属性方法: 把方法变成静态属性

# 写法1
class PM_1(object):
  def __init__(self):
    self.__name_str = "PropertieMethod_1"

  # 获取, 使用了property方法后就可以反射了属性, 动态的通过"字符串的方式"设置属性以及删除属性
  @property
  def name(self): # 注意,方法名相同
    return self.__name_str

  # 设置
  @name.setter
  def name(self, name):
    self.__name_str = name

  # 删除
  @name.deleter
  def name(self):
    del self.__name_str


if __name__ == "__main__":
  pm = PM_1()
  print(pm.name)
  pm.name = "PM"
  print(pm.name)
  del pm.name
  # print(pm.name)

# ==========================================================


# 写法2
class PM_2(object):
  def __init__(self):
    self.__name_str = "PropertieMethod_2"

  # 获取
  def getname(self):
    return self.__name_str

  # 设置
  def setname(self, name):
    self.__name_str = name

  # 删除
  def delname(self):
    del self.__name_str

  # property(fget=None, fset=None, fdel=None, doc=None) # 返回一个property 属性, 实现原理见 内置函数 文章 property_my 块代码(http://blog.csdn.net/rozol/article/details/70603230)
  name = property(getname, setname, delname)


if __name__ == "__main__":
  p = PM_2()
  print(p.name)
  p.name = "PM2"
  print(p.name)
  del p.name
  # print(p.name)

