### __init__ 方法 ###
'''
初始化方法：
在 __init__ 函数中初始化实例属性
'''

class Complex:
    # 类属性,实例对象和类共有的,只有一个
    number = 10
    def __init__(self, realpart, imagpart):
        # 对象属性,对象才有,不同的对象的对象属性是不同的，对象一一对应对象属性
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
y = Complex(3,-5)
print(x.r, x.i)   # 输出结果：3.0 -4.5
