'''
partial 的核心作用就是把参数分成两个步骤来传入
第一次一般给内部使用,
第二次一般提供给外部调用
'''

from functools import partial

def add(a, b):
    return a + b

plus3 = partial(add, 3)
plus5 = partial(add, 5)

print(plus3(4))
print(plus3(7))
print(plus5(10))


def add2(a,b,c,d):
    return a + b + c + d
plusplus = partial(add2, 3,3)
print(plusplus(2,2))
