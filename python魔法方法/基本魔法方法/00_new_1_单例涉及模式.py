#### 通过 __new__ 来实现单例涉及模式 ####
class SingleTon:
    '''__new__()实现'''
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


if __name__ == '__main__':
    s1 = SingleTon()
    s2 = SingleTon()
    print(s1)
    print(s2)