

# 类由type类实例化产生, 而type由解释器产生
# 元类 (type创建类原理)
# 元类是用于创建所有类的类, Python中是type类 (注意,类也是对象,也是被创建出来的,即万物皆对象), 下面将演示type类的功能

age = 21

def __init__(self):
  self.name = "origin"

def getname(self):
  return self.name

def setname(self, name):
  self.name = name

def delname(self):
  del self.name


# 用type创建类(类名, 基类元组, 类成员字典)
Foo = type('Foo', (object,), {'__init__' : __init__, "getname" : getname, "setname" : setname,
                              "delname": delname, "age" : age})

if __name__ == '__main__':
    # 实例化类
    f = Foo()

    # 使用
    print(f.age)

    print(f.getname())
    f.setname("ClassOrigin")
    print(f.getname())

    f.delname()
    # print(f.getname())

