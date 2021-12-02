import numpy as np

a=np.array([[1,2,3],[4,5,6]])

print(a)
# [[1 2 3]
#  [4 5 6]]

np.array(a)[1]=[7,8,9]

print(a)
# [[1 2 3]
#  [4 5 6]]

np.asarray(a)[1]=[7,8,9]
print(a)
# [[1 2 3]
#  [7 8 9]]

np.asanyarray(a)[1]=[10,11,12]
print(a)
# [[ 1  2  3]
#  [10 11 12]]

print(np.array(a) is a) # 复制一份
print(np.asarray(a) is a) # 仅引用 a 中的 ndarry 部分
print(np.asanyarray(a) is a) # 可以引用 a ,只要 a 是 ndarry的子类