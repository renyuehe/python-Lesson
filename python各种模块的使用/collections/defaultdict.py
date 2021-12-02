''''''
'''
defaultdict的作用是在于，当字典里的key不存在但被查找时，返回的不是keyError而是一个默认值。

如何使用defaultdict
defaultdict接受一个工厂函数作为参数，如下来构造：
dict =defaultdict( factory_function)

这个factory_function可以是list、set、str等等，
作用是当key不存在时，返回的是工厂函数的默认值，比如list对应[ ]，str对应的是空字符串，set对应set( )，int对应0，如下举例：
'''


from collections import defaultdict

dict1 = defaultdict(int)
dict2 = defaultdict(set)
dict3 = defaultdict(str)
dict4 = defaultdict(list)

dict1[2] ='two'


print("---", dict1[1])
print("---", dict2[1])
print("---", dict3[1])
print("---", dict4[1])
print(dict1[2])
