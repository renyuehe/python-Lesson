from torch import nn
import torch
from matplotlib import pyplot

act = nn.Hardswish()

input = torch.linspace(-10,10,100)
output= act(input)

pyplot.plot(input, output)
pyplot.show()
