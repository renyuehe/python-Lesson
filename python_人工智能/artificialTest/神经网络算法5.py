import torch
from torch import nn
import matplotlib.pyplot as plt
from torch import optim
import random

xs = torch.unsqueeze(torch.range(-20,20),dim=1)/20
ys = [e.pow(3)*random.randint(1,6) for e in xs]
ys = torch.stack(ys) #

# print(xs)
# print(ys)
# plt.plot(xs,ys,".")
# plt.show()

#创建模型
class line(torch.nn.Module):
    def __init__(self):
        super(line, self).__init__()
        self.fc_layers = nn.Sequential(
            nn.Linear(1,20),
            nn.ReLU(),
            nn.Linear(20,64),
            nn.ReLU(),
            nn.Linear(64,128),
            nn.ReLU(),
            nn.Linear(128,64),
            nn.ReLU(),
            nn.Linear(64,1)
        )
    def forward(self,x):
        return self.fc_layers(x)
if __name__ == '__main__':
    net = line()
    opt = optim.Adam(net.parameters(), 0.01) # 默认是 1e-3，学习率
    loss_func = torch.nn.MSELoss()
    plt.ion()
    for epoch in range(1000):
        out = net.forward(xs)

        loss = loss_func(out,ys)

        opt.zero_grad()
        loss.backward()
        opt.step()

        if epoch % 5 ==0:
            print(loss.item())

            plt.cla()
            plt.title("loss%.4f" % loss.item())
            plt.plot(xs,ys,".")
            plt.plot(xs,out.detach())
            plt.pause(0.001)

    plt.ioff()
    plt.show()