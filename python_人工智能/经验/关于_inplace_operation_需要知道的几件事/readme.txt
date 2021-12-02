在 pytorch 中, 有两种情况不能使用 inplace operation:

1.对于 requires_grad=True 的 叶子张量(leaf tensor) 不能使用 inplace operation
2.对于在 求梯度阶段需要用到的张量 不能使用 inplace operation


下面将通过代码来说明以上两种情况:

第一种情况: requires_grad=True 的 leaf tensor
import torch

w = torch.FloatTensor(10) # w 是个 leaf tensor
w.requires_grad = True    # 将 requires_grad 设置为 True
w.normal_()               # 在执行这句话就会报错
# 报错信息为
#  RuntimeError: a leaf Variable that requires grad has been used in an in-place operation.
很多人可能会有疑问, 模型的参数就是 requires_grad=true 的 leaf tensor, 那么模型参数的初始化应该怎么执行呢?
如果看一下 nn.Module._apply() 的代码, 这问题就会很清楚了
w.data = w.data.normal() # 可以使用曲线救国的方法来初始化参数

第二种情况: 求梯度阶段需要用到的张量
import torch
x = torch.FloatTensor([[1., 2.]])
w1 = torch.FloatTensor([[2.], [1.]])
w2 = torch.FloatTensor([3.])
w1.requires_grad = True
w2.requires_grad = True

d = torch.matmul(x, w1)
f = torch.matmul(d, w2)
d[:] = 1 # 因为这句, 代码报错了 RuntimeError: one of the variables needed for gradient computation has been modified by an inplace operation
f.backward()

为什么呢?

因为 [公式] , [公式] , [公式] 对于 [公式] 的导数是关于 [公式] 的函数: