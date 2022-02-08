# property装饰器
# 作用： 将一个get方法转换为对象的属性。 就是 调用方法改为调用对象
# 使用条件： 必须和属性名一样

# setter方法的装饰器：
# 作用：将一个set方法转换为对象的属性。 就是 a调用方法改为调用对象
# 使用方法：@属性名.setter

class Person:
    def __init__(self,name):
        self._name = name
    # 利用property装饰器将获取name方法转换为获取对象的属性
    @property
    def name(self):
        return self._name

    # 利用property装饰器将设置name方法转换为获取对象的属性
    @name.setter
    def nam(self,name):
        self._name = name
        self.a=22

p = Person('小黑')
print(p.name)   # 原获取 p.neame()  , 现 p.name,已经将函数（方法变成了属性值获取）
p.nam = '小灰' # 原设置 p.name('小灰')  ,现 p.name = '小灰'，相当于直接用变量命名，给属性值来更改此变量
print(p.name)



class Person:
    def __init__(self,name):
        self._name = name
    @property
    def name(self):
        a=100
        return self._name,a
    @name.setter
    def name(self,name): # name是一个列表，包含2个元素
        self._name = name[0] # 第一个元素值赋给self._name
        a=name[1] # 第二个值赋给a了，可是在执行上一个name()函数时候会有a=100，因此才不会改变变量的

p = Person('小黑')
print(p.name)
p.name = [88,99] # 因为执行了a=100，所以执行a=name[1]时，也不会改变输出值
print(p.name)

class Person:
    def __init__(self,name,bb):
        self._name = name
        self.a = bb
    # 利用property装饰器将获取name方法转换为获取对象的属性
    @property
    def name(self):

        return self._name,self.a
    # 利用property装饰器将设置name方法转换为获取对象的属性
    @name.setter
    def name(self,name):
        self._name = name[0]
        self.a=name[1]

p = Person('小黑',100)
print(p.name)   # 原获取 p.name()  , 现 p.name,已经将函数（方法变成了属性值获取）
p.name = [88,'小慧'] # 多个@property的属性输出
print(p.name)