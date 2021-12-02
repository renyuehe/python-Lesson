import matplotlib.pyplot as plt
import torch
from torch import nn


x = torch.linspace(-10, 10, 100)
x2 = torch.linspace(0, 0, 100)

lossfun = nn.SmoothL1Loss()
zero = torch.tensor(0)
xs = []
ys = []
for i in range(-99, 100):
    x = torch.tensor(i/10)
    y = lossfun(x, zero)
    xs.append(x)
    ys.append(y)

plt.plot(xs, ys)
plt.show()
