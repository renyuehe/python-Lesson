

# 自定义迭代器对象: 在类里面定义__iter__和__next__方法创建的对象就是迭代器对象
class MyIterator(object):
    def __init__(self):
        super(MyIterator, self).__init__()
        ...
    def __iter__(self):
        print("iter")
        return self

    # 获取迭代器中下一个值
    def __next__(self):
        print("next")

myiter = MyIterator()
for i in myiter:
    # print(i)
    exit()
