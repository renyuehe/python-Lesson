import torch

w = torch.FloatTensor(10) # w 是个 leaf tensor
w.requires_grad = True    # 将 requires_grad 设置为 True
w.normal_()               # 在执行这句话就会报错
# 报错信息为
#  RuntimeError: a leaf Variable that requires grad has been used in an in-place operation.

# 很多人可能会有疑问, 模型的参数就是 requires_grad=true 的 leaf tensor,
# 那么模型参数的初始化应该怎么执行呢? 如果看一下 nn.Module._apply() 的代码, 这问题就会很清楚了

