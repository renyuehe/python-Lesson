# 循环不会打印出5
for i in range(10):
    if i == 5:
        continue
    print(i, end=" ")

print("\n=======================")
# # 循环不会打印出5后面的数
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
