# 数的类型转换
a = 1
print(type(a))
b = a
print(type(b), b)
b = float(a)
print(type(b), b)

print("=============================")
# 集合类型转换
c = [1, 2, 3]
print(type(c))
d = tuple(c)
print(type(d))

print("=============================")
# 利用类型转换去掉列表中重复元素
e = [1, 1, 2, 2, 3, 3]
print(e)
print(list(set(e)))
