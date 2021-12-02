'''
compile(source, filename, mode[, flags[, dont_inherit]])

这是python自带的函数

source -- 字符串或者AST（Abstract Syntax Trees）对象。一般可将整个py文件内容file.read()传入。
filename -- 代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
mode -- 指定编译代码的种类。可以指定为 exec, eval, single。
flags -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
flags和dont_inherit是用来控制编译源码时的标志。

'''
func_def = \
    """ 
def add(x, y):
    return x+y

print(add(3,5))
    """
exec(func_def)

print("-------------------")
cm = compile(func_def, filename='<string>', mode='exec')
print(cm)
exec(cm)

print("-------------------")
import types
assert isinstance(cm, types.CodeType)

