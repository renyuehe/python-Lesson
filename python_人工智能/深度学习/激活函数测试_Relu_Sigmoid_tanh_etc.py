import torch.nn as nn
import torch

b = torch.Tensor([[1,2],[3,4]])

#定义激活函数
tanh = nn.Tanh()
sigmod = nn.Sigmoid()
relu = nn.ReLU()

print("原矩阵")
print(b)
print("tanh")
print(tanh(b))
print("sigmod")
print(sigmod(b))
print("relu")
print(relu(b))