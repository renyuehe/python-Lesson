from abc import abstractmethod, ABCMeta

class Bar(metaclass=ABCMeta):
    @abstractmethod
    def fun(self):
        '''please Implemente in subclass'''


class SubBar(Bar):
    '''
    '''

    def fun(self):
        print('fun in SubBar')


b = SubBar()
b.fun()