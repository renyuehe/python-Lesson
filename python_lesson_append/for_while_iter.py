# break
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)

print('循环结束。')

# continue
n = 5
while n > 0:
    n -= 1
    if n == 3:
        continue
    print(n)
print('循环结束。')


# 求质数
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')

# iter list
list = [1,2,3,4]
it = iter(list)
for x in it:
    print(x, end="")


# iter next
print()
import sys  # 引入 sys 模块
list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
while True:
    try:
        print(next(it))
    except StopIteration:
        break

# iter next
print()
list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
print(it)
# print(help(it))

print()
# class iter
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)