#coding=utf-8
# class_my.py 定义类 (新式类)

# 定义类
class Person:
  # 类属性 (class) (注:类/类方法 能修改类属性; 对象不能修改类属性,更改的只是实例属性)
  name = "name" # 公共属性
  __adress = "adress" # 私有属性 (__属性 表示私有)

  # 构造方法(对象创建调用) (__init__ 表示构造)
  def __init__(self, name, address = "地球"):
    # 实例属性
    self.name = name # (注:类属性与实例属性名称相同时用实例属性,实例属性被删除后使用类属性)
    self.__adress = address
    Person.setData(self)

  # 析构方法(对象销毁调用) (__del__ 表示析构)
  def __del__(self):
    print("对象被销毁.")

  # toString()
  def __str__(self):
    return "Person.class"

  # 实例方法 (this)
  def setName(self, name): # self可为其他字符串 (this)
    self.name = name; # 修改 实例属性 (不存在自动添加)

  # 类方法 (static)
  @classmethod
  def setName_cls(cls, name):
    cls.name = name # 修改 类属性

  # 静态方法 (tools)
  @staticmethod
  def setName_sta(name): # (注:参数部分)
    return name

  def getName(self):
    return self.name

  def setData(self):
    # 实例属性
    self.__age = 21 # 私有属性
    self.sex = "女" # 公共属性

  def show(self):
    print("Hello! %s"%self.name)
    print("Address:%s"%self.__adress) # 使用自身私有属性
    self.__eat() # 使用自身私有方法

  def __eat(self): # 私有方法
    print("eat")



# ======= 函数调用 ======
if __name__ == "__main__":
  # - 创建对象 -
  ps = Person("LY")

  # --- 调用方法 ---
  # 调用实例方法
  ps.setName("LY") # 实例调用 实例方法
  ps.show()

  # 调用类方法
  Person.setName_cls("Person") # 类调用 类方法
  ps.setName_cls("Person") # 实例调用 类方法

  # 调用静态方法 ()
  print(ps.setName_sta("Per")) # 实例调用 静态方法
  print(Person.setName_sta("Per")) # 类调用 静态方法

  # --- 访问属性 ---
  print(ps.getName())
  print(ps.name) # 访问 类属性 的公共属性值
  print(ps.sex) # 访问 实例属性 的公共属性值

  # --- 修改属性 ---

  # 修改实例属性
  ps.name = "123" # 修改 类属性 (注:并非真修改,只是向对象中创建了一个实例属性)
  del ps.name # 删除 实例属性 (注:实例不能(非类方法)删除 类属性, 只是删除了对象中创建的实例属性,类属性依然存在)
  del ps.sex # 删除 实例属性 (注:真删除,删除后不能访问)

  # 修改类属性
  Person.name = "Person" # 修改类属性
  Person.setName_cls("Person") # 类 调用 类方法 修改 类属性 (注:类不能调用实例方法)
  ps.setName_cls("Person") # 对象 通过 类方法 修改 类属性
  del Person.name # 删除类属性

  # - 删除对象 -
  del ps
  # > Less is more! "静态方法"和"类方法/属性"同级都可理解为"静态",静态方法适合做工具箱,类方法/属性可认为在静态区,随手拿来即用,而实例则需要实例化才能使用. (--本人的个人理解)
# ======= 函数调用 ======
