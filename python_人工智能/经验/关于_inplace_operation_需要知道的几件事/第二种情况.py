''''''
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

'''
为什么呢？
因为 f = matmul(d, w2), ∂f/∂w2 = g(d), f 对于 w2 的导数是关于 d 的函数。

在计算 f 的时候, d 是等于某个值的, f 对于 w2 的导数是和这时候的 d 值相关的
但是计算完 f 之后, d 的值变了, 这就会导致 f.backward() 对于 w2 的导数计算出错误, 为了防止这种错误, pytorch 选择了报错的形式.
造成这个问题的主要原因是因为 在执行 f = torch.matmul(d, w2) 这句的时候, pytorch 的反向求导机制 保存了 d 的引用为了之后的 反向求导计算.
'''


import torch
x = torch.FloatTensor([[1., 2.]])
w1 = torch.FloatTensor([[2.], [1.]])
w2 = torch.FloatTensor([3.])
w1.requires_grad = True
w2.requires_grad = True

d = torch.matmul(x, w1)
d[:] = 1   # 稍微调换一下位置, 就没有问题了
f = torch.matmul(d, w2)
f.backward()