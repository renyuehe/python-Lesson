from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    def __init__(self):
        pass
    @abstractmethod
    def get(self):
        ''''''


class Derive1(Base):
    def get(self):
        print("Derive1.get()")


class Derive2(Base):
    '''
    '''

    # def get(self):
    #     print("Derive2.get()")

if __name__ == '__main__':

    # 有抽象方法不能被实例化
    # b = Base()
    # b.get()

    # 重写了抽象方法，可以被实例化
    cc = Derive1()
    cc.get()

    # 子类没有重写方法，也不能被实例化
    dd = Derive2()
    dd.get()