def a_new_decorator(a_func):
    def wrapTheFunction():
        print("before")
        a_func()
        print("after")
    return wrapTheFunction

def a_function_requiring_decoration():
    print("哈哈哈哈哈哈啊哈")

a_function_requiring_decoration()
print()

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
a_function_requiring_decoration()
