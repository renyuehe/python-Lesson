import torch

# torch.inverse(input, out=None) → Tensor
# 对方阵输入input 取逆。

x = torch.rand(3, 3)
print(
    x
)
print(
torch.inverse(x)    # 矩阵的逆
)
print(
torch.mm(x,torch.inverse(x)) # 叉乘验证
)