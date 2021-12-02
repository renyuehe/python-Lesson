import torch

b = torch.tensor(2)
print(b)
print(b.shape) #
print(b.ndim) # 维度

b = torch.tensor([[1,2],[2,3],[4,5]])
print(b)
print(b.shape)
print(b.type())