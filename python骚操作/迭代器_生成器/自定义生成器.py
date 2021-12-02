#将生成器实现为一个类，只要把生成器函数的代码放到__iter__()方法中即可。

# 自定义一个生成器
class LineHistory:
    def __init__(self, number, times):
        self.times = times
        self.number = number
    def __iter__(self):
        for i in range(self.times):
            yield self.number
            self.number *= 2
print("----------------------- for 循环遍历生成器 ----------------------------")
lh = LineHistory(10, 5)
for i in lh:
    print(i)
print("----------- *生成器 --------------")
lh = LineHistory(1, 5)
print(*lh)
print("-----------生成器-转换成-list-tuple-dict-set-------------")
lh = LineHistory(1, 3)
ret1 = list(lh)
print(ret1)
ret = tuple(lh)
print(ret)
ret = dict(zip(lh,ret1))
print(ret)
ret = set(lh)
print(ret)
