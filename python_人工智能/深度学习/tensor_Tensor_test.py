import torch
from torch.nn.functional import one_hot
import numpy as np

onehot = torch.squeeze(one_hot(torch.arange(1), 10))
onehot = torch.unsqueeze(one_hot(torch.arange(1), 10), dim=1)


print(onehot.shape)

# a = torch.tensor([1])
# b = torch.Tensor([1])
#
# print(a)
# print(b)