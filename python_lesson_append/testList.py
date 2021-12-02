list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']


print(list)
list.insert(1, 333)
print(list)
list.pop()
print(list)
list.remove(333)
print(list)


numberList = [1, 4, 7, 2, 3]
print(sorted(numberList)) #临时排序
print(numberList)
numberList.sort()   #永久排序
print(numberList)
numberList.sort(reverse=True)
print(numberList)

numberList.reverse()
print(numberList)

numberList.append(100)
numberList.append(200)
print(numberList)

tempNumberList = [444, 555, 666]
numberList.append(tempNumberList)
print(numberList)

print(list[0])   # 输出列表的第一个元素
print(list[0: 2])   # 输出第二个至第三个元素
print(list[1: 2])   # 输出第二个至第三个元素
print(list[2:])   # 输出从第三个开始至列表末尾的所有元素

print(tinylist * 2)   # 输出列表两次
print(list + tinylist)  # 打印组合的列表

for iter in list:
    print(iter)

