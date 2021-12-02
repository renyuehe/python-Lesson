...

'''首先 int 类型是不能这样追加的'''
# a = 10
# a.__myvar__ = 20 # AttributeError: 'int' object has no attribute '__myvar__'
# print(a.__myvar__)

'''通过types查看类型帮助'''
import types
help(types.FunctionType)



def myfun():
    print("hahah")

# myfun.__isabstractmethod__ = True

call = myfun.__get__("__call__")
myfun.__repr__()


print("__annotations__=>   ",myfun.__annotations__)
print("__closure__=>   ",myfun.__closure__)
print("__code__=>   ",myfun.__code__)
print("__defaults__=>   ",myfun.__defaults__)
print("__globals__=>   ",myfun.__globals__)
print("__kwdefaults__=>   ",myfun.__kwdefaults__)

obj = object


