print(" ============ list 操作 ============")
a = [1, 2, 3, 4]
print(len(a))  # 计算包含元素的个数
print(a[2])  # 获取集合第2个元素

# 修改第3个元素为5
a[3] = 5
print(a)


# 删除第3个元素
a.remove(a[3])
print(a)

# 向尾部添加一个元素
a.append(8)
print(a)

# 在第2个元素前插入一个元素7
a.insert(2, 7)
print(a)

# 将另一个集合添加到尾部
a.extend([0, 2, 5])
print(a)

# 查看元素7的索引
print(a.index(7))


# 排序
a.sort()
print(a)
a.sort(reverse=True)
print(a)

# 清空元素
a.clear()
print(a)

