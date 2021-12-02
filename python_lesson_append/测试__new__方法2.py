'''
* __new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供
* __new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类__new__出来的实例，或者直接是object的__new__出来的实例
* __init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值
* 我们可以将类比作制造商，__new__方法就是前期的原材料购买环节，__init__方法就是在有原材料的基础上，加工，初始化商品环节


* 使用 类名() 创建对象时，Python 的解释器 首先 会 调用 __new__ 方法为对象 分配空间
* __new__ 是一个 由 object 基类提供的 内置的静态方法，主要作用有两个：

	* 1) 在内存中为对象 分配空间
	* 2) 返回 对象的引用
* Python 的解释器获得对象的 引用 后，将引用作为 第一个参数，传递给 __init__ 方法

***

* __new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供
* __new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类__new__出来的实例，或者直接是object的__new__出来的实例
* __init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值
* 我们可以将类比作制造商，__new__方法就是前期的原材料购买环节，__init__方法就是在有原材料的基础上，加工，初始化商品环节


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