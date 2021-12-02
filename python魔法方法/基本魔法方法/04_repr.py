################ __repr__ 魔法方法，object 默认自我描述，也可以实现自我描述
'''
# 是Python类中的一个特殊方法，由object对象提供，由于所有类都是object类的子类，所以都会继承该方法！！！
# object提供的这个__repr__方法总是返回一个对象， （  类名 + obejct  at + 内存地址  ），
# 因此，如果你想在自定义类中实现  “自我描述” 的功能，那么必须重写 __repr__ 方法：
'''

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
person = Person('炫羽',20)
print(person) # 内存中的一个对象 <__main__.Person object at 0x0042A6A0>

print(person) # <__main__.Person object at 0x0025A6A0>
print(person.__repr__) # <method-wrapper '__repr__' of Person object at 0x0025A6A0>

################ 自定义 __repr__ 方法
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Person类，包含name=' + self.name + '和age=' + str(self.age) + '两个实例属性' + '\n'


person = Person('炫羽', 20)

print(person)  # Person类，包含name=吕星辰和age=20两个实例属性

################# __repr__ 默认返回值的实现
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '<{0}.{1} object at {2}>'.format(self.__module__, type(self).__name__, hex(id(self)))


person = Person('炫羽', 20)

print(person)  # <__main__.Person object at 0x5ba6a0>