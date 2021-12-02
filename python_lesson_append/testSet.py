# 集合中元素不重复,无序的

mySet = {'runoob', 786, 786, 2.23, 'john', 70.2}

print(mySet)        # 输出完整元组
print(mySet.pop())     # 输出元组的第一个元素
print(mySet.pop())   # 输出第二个至第四个（不包含）的元素
print(mySet.pop())    # 输出从第三个开始至列表末尾的所有元素

print(mySet)
print(list(mySet))
print(786 in mySet)
print(78 in mySet)


myList = [1, 2, 3, 4, 5, 6, 1, 1, 1, 1]
print(myList)
print(set(myList))

# 集合运算
print()
a = {1, 2, 3, 4, 5, 6, 7, "one", "two", "three"}
b = {5, 6, 7, 8, 9, 10, "four", "five", "three"}
print(a - b)    # 差集
print(a | b)    # 并集
print(a & b)    # 交集
print(a ^ b)    # 补集

# 常用操作
print()
s = set([3, 4, 5, 9, 10])
print(s)
s.update([11, 22, 33])
print(s)

print()
t = set("Hello")
print(t)
t.add("x")
print(t)
t.remove("H")
print(t)
