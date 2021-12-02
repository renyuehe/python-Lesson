from abc import ABC, abstractmethod

class Foo(ABC):
    @abstractmethod
    def fun(self):
        '''please Implemente in subclass'''

class SubFoo(Foo):
    '''
    基类Foo的fun方法被@abstractmethod装饰了，
    所以Foo不能被实例化；子类SubA没有实现基类的fun方法也不能被实例化；
    子类SubB实现了基类的抽象方法fun所以能实例化。
    '''
    def fun(self):
        print('fun in SubFoo')

    def haha(self):
        print("haha")

a = SubFoo()
a.fun()

