# class_origin.py 类的由来
# 类由type类实例化产生, 而type由解释器产生

age = 21

def __init__(self):
  self.name = "origin"

def getname(self):
  return self.name

def setname(self, name):
  self.name = name

def delname(self):
  del self.name


if __name__ == "__main__1":
  # 用type创建类(类名, 基类元组, 类成员字典)
  Foo = type('Foo', (object,), {'__init__' : __init__, "getname" : getname, "setname" : setname,
                 "delname": delname, "age" : age})
  # 实例化类
  f = Foo()
  # 使用
  print(f.age)
  print(f.getname())
  f.setname("ClassOrigin")
  print(f.getname())
  f.delname()
  # print(f.getname())

# 元类 (type创建类原理)
# 元类是用于创建所有类的类, Python中是type类 (注意,类也是对象,也是被创建出来的,即万物皆对象), 下面将演示type类的功能
# ==================================================================================


# metaclass指定类有谁来创建
# Python创建类时会寻找__metaclass__属性,(包括父类)没有找到将使用内建元类type
class MyType(type):
  def __init__(self, *args, **kwargs):
    print("MyType __init__")

  def __call__(self, *args, **kwargs):
    print("MyType __call__")
    obj = self.__new__(self)
    self.__init__(obj, *args, **kwargs)
    return obj

  def __new__(cls, *args, **kwargs):
    print("MyType __new__")
    return type.__new__(cls, *args, **kwargs)


class Foo(object, metaclass=MyType): # (Python3.x写法) metaclass 用于创建类, Python创建类时会寻找__metaclass__属性,(包括父类)没有找到将使用内建元类type

  # __metaclass__ = MyType # Python2.x写法

  def __init__(self):
    print("Foo __init__")

  def __new__(cls, *args, **kwargs): # 用于实例化对象
    print("Foo __new__")
    return object.__new__(cls) # 必须是返回

  def show(self):
    print("Foo show")


if __name__ == "__main__":
  print("start")
  f = Foo()
  f.show()
  # MyType __new__ => MyType __init__ => 'start' => MyType __call__ => Foo __new__ => Foo __init__ => 'Foo show'

