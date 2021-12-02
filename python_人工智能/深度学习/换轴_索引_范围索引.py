import numpy as np

a = np.arange(24).reshape(2,3,4)

print(a)

print(a[:,0,[2,3]]) #:,是换轴。 0,是索引并降至下一个维度。 [2,3]也是范围索引


