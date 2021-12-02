
# 自定义迭代器对象: 在类里面定义__iter__和__next__方法创建的对象就是迭代器对象
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

print("----------------------- for 循环遍历生成器 ----------------------------")
myiter = MyIterator([1,2,3,100,200,333])
for i in myiter:
    print(i)
print("----------- *生成器 --------------")
myiter = MyIterator([1,2,3,100,200,333])
print(*myiter)
print("-----------生成器-转换成-list-tuple-dict-set-------------")
myiter = MyIterator([1,2,3,100,200,333])
ret1 = list(myiter)
print(ret1)
myiter = MyIterator([1,2,3,100,200,333])
ret = tuple(myiter)
print(ret)
myiter = MyIterator([1,2,3,100,200,333])
ret = dict(zip(myiter,ret1))
print(ret)
myiter = MyIterator([1,2,3,100,200,333])
ret = set(myiter)
print(ret)