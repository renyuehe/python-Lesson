
# 自定义一个生成器
print("======================= 生成器不断向后生成：无需事先开辟内存,可以没有上限 ==========================")
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


# 自定义迭代器对象: 在类里面定义__iter__和__next__方法创建的对象就是迭代器对象
print("======================= 迭代不断向后生成：需要提前开辟内存,有上限,有范围 ==========================")
class MyIterator(object):

    def __init__(self, my_list):
        self.my_list = my_list
        # 记录当前获取数据的下标
        self.current_index = 0
    def __iter__(self):
        return self

    # 获取迭代器中下一个值
    def __next__(self):
        if self.current_index < len(self.my_list):
            self.current_index += 1
            return self.my_list[self.current_index - 1]
        else:
            # 数据取完了，需要抛出一个停止迭代的异常
            raise StopIteration


print("----------------------- for 循环遍历迭代器 ----------------------------")
myiter = MyIterator([1,2,3,4,111])
for i in myiter:
    print(i)
print("----------- *迭代器 --------------")
myiter = MyIterator([1,2,3,4,111])
print(*myiter)
print("-----------迭代器-转换成-list-tuple-dict-set-------------")
myiter = MyIterator([1,2,3,4,111])
ret1 = list(myiter)
print(ret1)
myiter = MyIterator([1,2,3,4,111])
ret = tuple(myiter)
print(ret)
myiter = MyIterator([1,2,3,4,111])
ret = dict(zip(myiter,ret1))
print(ret)
myiter = MyIterator([1,2,3,4,111])
ret = set(myiter)
print(ret)

print("============================ 关于 tuple set list和 dict 之间的一种转换 ============================")
data = ({1,"1"},(2,"2"),[3,"3"])
print(data.__class__)
print(data[0].__class__)
print(data[1].__class__)
print(data[2].__class__)
print("--------- 关于 list 和 dict 之间的一种转换 ------------")
print(data)
print(list(data))
print(dict(data))
print(dict(data).keys())
print(dict(data).values())
from collections import OrderedDict
print(OrderedDict(data))
print(OrderedDict(data).keys())
print(OrderedDict(data).values())

print("============================ 关于 dict 和 tuple set list 之间的一种转换 ============================")
dictdata = dict(data)
# dictdata = OrderedDict(data)
print(dictdata)

print("--------dict 转 list tuple set *")
print(list(dictdata))
print(tuple(dictdata))
print(set(dictdata))
print(*dictdata)
print("--------dict.values 转 list tuple set *")
print(list(dictdata.values()))
print(tuple(dictdata.values()))
print(set(dictdata.values()))
print(*dictdata.values())
print("--------dict.keys 转 list tuple set *")
print(list(dictdata.keys()))
print(tuple(dictdata.keys()))
print(set(dictdata.keys()))
print(*dictdata.keys())


