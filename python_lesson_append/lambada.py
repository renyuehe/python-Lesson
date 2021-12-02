
# # 匿名函数定义、调用
# my_lambda = lambda arg : arg + 1
# print(my_lambda(10))

# 匿名函数做参数, map 是映射函数
foo = [1, 2, 3, 4, 5]
m = map(lambda x: x+10, foo)
for i in m:
    print(i)
