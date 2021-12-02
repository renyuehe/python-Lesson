from functools import reduce

a, b = ['0','1','2', '3'], 3  # 4种字符，匹配5种字符
print(a)
print([a] * b)
ret = reduce(lambda x, y: [z0 + z1 for z0 in x for z1 in y],    [a] * b)

print(ret)
print(ret.__len__())
