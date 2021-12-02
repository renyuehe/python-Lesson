from torch import nn
import torch

m = nn.SiLU()
input = torch.randn(2)
print(input)
output = m(input)
print(output)

sigmod = nn.SiLU()
output2 = input * sigmod(input)
print(output2)