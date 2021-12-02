

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


# if __name__ == "__main__":
#   print("start")
#   f = Foo()
#   f.show()
#   # MyType __new__ => MyType __init__ => 'start' => MyType __call__ => Foo __new__ => Foo __init__ => 'Foo show'
#
