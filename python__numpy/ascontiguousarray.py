...
'''
# ascontiguousarray
# 函数作用
# 返回一个连续的array，其内存是连续的。
'''

import numpy as np
arr = np.arange(12).reshape(3, 4)
print(arr.flags)  # C_CONTIGUOUS 为 True, 原本是连续的

arr1 = arr[:, 1:3] # 在行上的slice，则会改变连续性
print(arr1.flags)  # C_CONTIGUOUS 为 False

arr1 = np.ascontiguousarray(arr1) # 将其改为内存连续
print(arr1.flags) # C_CONTIGUOUS 改为 True, OWNDATA 改为 True
