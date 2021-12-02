# 打印出0到9
for i in range(3, 10, 2):
    print(i, end=" ")

print("\n=======================")
# 遍历列表
a_list = {4, 5, 6, 7, 8, 9}
for a in a_list:
    print(a, end=" ")

print("\n=======================")
# 带索引的遍历
for i, a in enumerate(a_list):
    print(i, ":", a)

print("\n=======================")
# 遍历dict
b_dict = {"name": "zhang3", "sex": "男", "age": 36}
for key, value in b_dict.items():
    print(key, ":", value)
