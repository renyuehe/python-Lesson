import matplotlib.pyplot as plt
import torch
from torch import nn

x = torch.linspace(-10, 10, 100)
print(x)
act = nn.Sigmoid()
y = act(x)
plt.plot(x, y)
plt.show()
