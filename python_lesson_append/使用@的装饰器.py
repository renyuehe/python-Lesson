def a_new_decorator(a_func):
    def wrapTheFunction():
        print("before")
        a_func()
        print("after")
    return wrapTheFunction

# 该装饰器就相当于 把 紧随的函数作为参数传递给装饰器函数装饰并返回后的函数
@a_new_decorator
def a_function_requiring_decoration():
    print("哈哈哈哈")

a_function_requiring_decoration()
