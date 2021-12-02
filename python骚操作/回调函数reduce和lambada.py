
from functools import reduce

lll = [(1,2),(2,2),(3,2)]

ret = reduce(lambda x, y: x + y , lll)
print(ret)

# 求阶乘
# ret2 = reduce(lambda a, b: a * b, range(1, 10))
# print(ret2)