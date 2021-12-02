''''''
"""
1. inspect.getmembers(object[, predicate])

第二个参数通常可以根据需要调用如下16个方法；

返回值为object的所有成员，以（name,value）对组成的列表

inspect.ismodule(object)： 是否为模块

inspect.isclass(object)：是否为类

inspect.ismethod(object)：是否为方法（bound method written in python）

inspect.isfunction(object)：是否为函数(python function, including lambda expression)

inspect.isgeneratorfunction(object)：是否为python生成器函数

inspect.isgenerator(object):是否为生成器

inspect.istraceback(object)： 是否为traceback

inspect.isframe(object)：是否为frame

inspect.iscode(object)：是否为code

inspect.isbuiltin(object)：是否为built-in函数或built-in方法

inspect.isroutine(object)：是否为用户自定义或者built-in函数或方法

inspect.isabstract(object)：是否为抽象基类

inspect.ismethoddescriptor(object)：是否为方法标识符

inspect.isdatadescriptor(object)：是否为数字标识符，数字标识符有__get__ 和__set__属性； 通常也有__name__和__doc__属性

inspect.isgetsetdescriptor(object)：是否为getset descriptor

inspect.ismemberdescriptor(object)：是否为member descriptor

2. inspect.getmoduleinfo(path)： 返回一个命名元组<named tuple>(name, suffix, mode, module_type)

　　name：模块名（不包括其所在的package）

      suffix：

      mode：open()方法的模式，如：'r', 'a'等

      module_type: 整数，代表了模块的类型

3. inspect.getmodulename(path)：根据path返回模块名（不包括其所在的package）
"""