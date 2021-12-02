######## __new__ 方法 和 __init__方法 的关系 #######
'''
	* __new__ 分配空间
	* __init__ 对象初始化

'''
class Person(object):
    """Silly Person"""
    def __new__(cls, *args, **kwargs):
        print('__new__ called.')
        # python3 中 真正实例一个对象的空间大小是基类 object 中来实例化的,
        # 需要实例化的内存大小根据 cls 这个参数来决定, 就是当前类, cls 作为当前类的参数传入, cls 的写法是任意的
        return super(Person, cls).__new__(cls)

    # 其中的 self 就是通过 __new__ 函数 return 返回出来的实例对象
    def __init__(self, name, age):
        print('__init__ called.')
        self.name = name
        self.age = age

    def __str__(self):
        return '<Person: %s(%s)>' % (self.name, self.age)



if __name__ == '__main__':
    piglei = Person('piglei', 24)
    print(piglei)