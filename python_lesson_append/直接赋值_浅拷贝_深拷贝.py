import copy
'''
直接赋值：其实就是对象的引用（别名）。
浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。
深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。
'''

'''
不可变对象：int，string，float，tuple
可变对象 ：list，dictionary
'''
print("------------直接赋值-------------")

a = {1: [1,2,3]}
b = a
print(a)
print(b)
a[1].append(4)
print(a)
print(b)
print("a id:", id(a))
print("b id:", id(b))

print("------------浅拷贝-------------")

a = {1: [1,2,3]}
b = a.copy() # 字典可以直接 .copy() 是因为字典内部自己实现了
b = copy.copy(a) #对于任何类型,使用 copy模块, copy.copy() 就是浅拷贝
print(a)
print(b)
a[1].append(4)
a.update({2:"浅拷贝：拷贝父对象，不会拷贝对象的内部的子对象"})
print(a)
print(b)
print("a id:", id(a))
print("b id:", id(b))
print("------------深拷贝-------------")

a = {1: [1,2,3]}
import copy
c = copy.deepcopy(a) # 此处是深拷贝,是一份新的内存
print(a)
print(c)
a[1].append(5)
print(a)
print(c)
print("a id:", id(a))
print("c id:", id(c))