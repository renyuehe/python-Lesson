class AAA():
    pass


class BBB():
    pass

class CCC(AAA, BBB):
    pass

c = CCC()

# 在当前的命名空间给一个整数object名字为a
ret = type(c)
print(ret)

ret = type(type(c))
print(ret)

ret = type(c).__base__
print(ret)

ret = type(c).__bases__
print(ret)

ret = dir(c) #都是 object 最原始的方法们
print(ret)