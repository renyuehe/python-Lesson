
from abc import ABCMeta, abstractmethod

class AAA(ABCMeta):
    def __init__(self):
        ...

    @abstractmethod
    def fun(self, name:str, number:int) -> str:
        pass



