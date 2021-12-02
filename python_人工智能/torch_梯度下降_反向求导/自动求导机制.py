# 通过下面这种方式导入 Variable
"""
每个变量都有两个标志：requires_grad 和 volatile。
它们都允许从梯度计算中精细地排除子图，并可以提高效率。

requires_grad

如果有一个单一的输入操作需要梯度，它的输出也需要梯度。
相反，只有所有输入都不需要梯度，输出才不需要。
如果其中所有的变量都不需要梯度进行，后向计算不会在子图中执行。
"""

import torch
from torch.autograd import Variable

x = Variable(torch.randn(5, 5))
y = Variable(torch.randn(5, 5))
z = Variable(torch.randn(5, 5), requires_grad=True)

a = x + y
print(a)
print()
print(a.requires_grad)

b = a + z
print()
print(b.requires_grad)





