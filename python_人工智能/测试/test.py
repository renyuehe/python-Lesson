import torch
from torch import nn

data = nn.Parameter(torch.Tensor([0.485, 0.456, 0.406]))

print(data)

ret = data.repeat(1,1,3,5)
print(ret)