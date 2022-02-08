class Person:
    def __init__(self):
        # __为私有属性
        self.__name = 'wusir'

    @property
    def name(self):
        return self.__name

    # # 通过property就可以获取到name, 不需要这个了
    # @name.getter
    # def name(self):
    #     return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name


p = Person()

# 先通过property获取name属性
print('property/getter-name:   {}'.format(p.name))   # property/getter-name:   wusir
p.name = 'alex'  # 通过setter给person对象p添加那么属性
print('setter-name:   {}'.format(p.name))    #  setter-name:   alex
# del p.name    # 删除name属性
# print(p.name)   # 报错, 提示person对象没有name属性