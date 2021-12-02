'''
结论：自定义对象是可变对象
不可变对象, =号 会创建一个新的对象
可变对象, =号 相当于 C++的引用
'''

print("---------------不可变对象, =号 会创建一个新的对象---------------")
# 不可变对象, =号 会创建一个新的对象
b = 10
c = b
b = 15
print(b)
print(c)

print("----------------可变对象, =号 相当于 C++的引用---------------")
l = [1,2,3]
l2 = l
l.append(5)
print(l)
print(l2)
print("----------------自定义对象是可变对象----------------")
class MY(object):
    def __init__(self):
        super(MY, self).__init__()
        self.aaa = 10

my = MY()
print(my.aaa)

me = my
print(me.aaa)

my.aaa = 12
print(my.aaa)
print(me.aaa) # 证明自定义对象是可变对象,所以=号就相当于是引用
