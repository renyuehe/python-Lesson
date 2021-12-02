'''
参数说明

input：输入tensor
p (int, float, inf, -inf, 'fro', 'nuc', optional)：范数计算中的幂指数值。默认为'fro'


dim (int，2-tuple，2-list， optional): 指定计算的维度。如果是一个整数值，向量范数将被计算；
如果是一个大小为2的元组，矩阵范数将被计算；如果为None，当输入tensor只有两维时矩阵计算矩阵范数；
当输入只有一维时则计算向量范数。如果输入tensor超过2维，向量范数将被应用在最后一维


keepdim（bool，optional）：指明输出tensor的维度dim是否保留。
如果dim=None或out=None,则忽略该参数。默认值为False，不保留


out（Tensor, optional）:tensor的输出。
如果dim=None或out=None,则忽略该参数。


dtype（torch.dtype，optional）：指定返回tensor的期望数据类型。
如果指定了该参数，在执行该操作时输入tensor将被转换成 :attr:’dtype’
'''

import torch
a = torch.arange(9, dtype=torch.float) - 4
print(a)

b = a.reshape(3,3)
print(b)

ret = torch.norm(a) #默认为2范数  根号 (16*2 + 9*2 + 4*2 + 1*2)
print(ret)

ret = torch.norm(b)
print(ret)

