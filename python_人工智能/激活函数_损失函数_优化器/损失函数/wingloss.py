import matplotlib.pyplot as plt
import torch
from torch import nn
import math
class WingLoss(nn.Module):
    def __init__(self, omega=10, epsilon=2):
        super(WingLoss, self).__init__()
        self.omega = omega
        self.epsilon = epsilon

    def forward(self, pred, target):
        y = target
        y_hat = pred
        delta_y = (y - y_hat).abs()
        delta_y1 = delta_y[delta_y < self.omega]
        delta_y2 = delta_y[delta_y >= self.omega]
        loss1 = self.omega * torch.log(1 + delta_y1 / self.epsilon)
        C = self.omega - self.omega * math.log(1 + self.omega / self.epsilon)
        loss2 = delta_y2 - C
        return (loss1.sum() + loss2.sum()) / (len(loss1) + len(loss2))

x = torch.linspace(-10, 10, 100)
x2 = torch.linspace(0, 0, 100)

lossfun = WingLoss()
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
