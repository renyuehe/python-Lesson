import random

import torch
from torch import nn
import matplotlib.pyplot as plt
from torch import optim

xs = torch.unsqueeze(torch.range(-20,20),dim=1) # 升维
ys = [e.pow(3)*random.randint(1,6) for e in xs]
ys = torch.stack(ys)    # ？？
# plt.plot(xs,ys,".")
# plt.show()



#创建模型
class line(torch.nn.Module):
    def __init__(self):
        super(line, self).__init__()
        # self.w1 = torch.nn.Parameter(torch.randn(1,20))
        # self.b1 = torch.nn.Parameter(torch.randn(20))
        # self.w2 = torch.nn.Parameter(torch.randn(20,64))
        # self.b2 = torch.nn.Parameter(torch.randn(64))
        # self.w3 = torch.nn.Parameter(torch.randn(64, 128))
        # self.b3 = torch.nn.Parameter(torch.randn(128))
        # self.w4 = torch.nn.Parameter(torch.randn(128, 64))
        # self.b4 = torch.nn.Parameter(torch.randn(64))
        # self.w5 = torch.nn.Parameter(torch.randn(64, 1))
        # self.b5 = torch.nn.Parameter(torch.randn(1))
        self.layer1 = nn.Linear(1,20)
        self.s1 = nn.ReLU() # 激活函数
        self.layer2 = nn.Linear(20, 64) # 内部包含了 SVD， 梯度下降。
        self.s2 = nn.ReLU()
        self.layer3 = nn.Linear(64, 128)
        self.s3 = nn.ReLU()
        self.layer4 = nn.Linear(128, 64)
        self.s4 = nn.ReLU()
        self.layer5 = nn.Linear(64, 1)
    def forward(self,x):
        # fc1 = torch.matmul(x,self.w1)+self.b1
        # fc2 = torch.matmul(fc1,self.w2)+self.b2
        # fc3 = torch.matmul(fc2, self.w3) + self.b3
        # fc4 = torch.matmul(fc3, self.w4) + self.b4
        # fc5 = torch.matmul(fc4, self.w5) + self.b5
        fc1 = self.layer1(x)
        fc1 = self.s1(fc1)
        fc2 = self.layer2(fc1)
        fc2 = self.s2(fc2)
        fc3 = self.layer3(fc2)
        fc3 = self.s3(fc3)
        fc4 = self.layer4(fc3)
        fc4 = self.s4(fc4)
        fc5 = self.layer5(fc4)
        return fc5
if __name__ == '__main__':
    net = line()
    opt = optim.Adam(net.parameters())
    loss_func = torch.nn.MSELoss()
    plt.ion()
    for epoch in range(10000):
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