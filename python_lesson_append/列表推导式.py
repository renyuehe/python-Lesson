a_list = [1, 2, 3, 4, 5, 6]
b_list = []
for a in a_list:
    b_list.append(a * 2)
print(b_list)

# 将上面的代码简化为下面代码
c_list = [x * 2 for x in a_list]
print(c_list)
