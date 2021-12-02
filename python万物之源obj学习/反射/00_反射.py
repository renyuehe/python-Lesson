#!/usr/bin/env python
# coding=utf-8
pass
'''
# class_reflection.py 反射
# 通过反射机制,可动态修改程序运行时的状态/属性/方法
# Python的反射机制性能如何? 在Android中Java的反射产生垃圾而执行gc,从而导致UI不流畅,而且性能低
# Python的反射性能(1亿次测试): 直接获取属性值:反射获取属性值 = 1:1.164 ;直接设置属性值:反射设置属性值 = 1:1.754
'''

def setname(self, name):
  self.name = name

class Clazz(object):
  def __init__(self):
    self.name = "Clazz"

  def getname(self):
    return self.name


if __name__ == "__main__":
  c = Clazz()

  # --- 方法 ---
  if hasattr(c, "getname"):
    # 获取
    method = getattr(c, "getname", None)
    print(c.name)

  if not hasattr(c, "setname"):
    # 添加
    setattr(c, "setname", setname) # 添加方法
    method = getattr(c, "setname", None)
    method(c, "Reflection")
    print(c.name)

  if hasattr(c, "setname"):
    # 删除
    delattr(c, "setname")
    # c.setname(c, "Demo")

  #行不通
  # delattr(c, "getname")


  # --- 属性 ---
  if not hasattr(c, "age"):
    # 添加
    setattr(c, "age", 21) # 添加方法
    print(c.age)

  if hasattr(c, "age"):
    # 获取
    ret = getattr(c, "age", None)
    print(ret)

  if hasattr(c, "age"):
    # 删除
    delattr(c, "age")
    # print(c.age)
    delattr(c, "name")
    # print(c.name)

