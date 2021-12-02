import torch
from torch import nn    # 神经元
import matplotlib.pyplot as plt # 绘图板
from torch import optim # 优化器

# 一维 升 二维， 升维， 核函数
xs = torch.unsqueeze(torch.arange(0.01,1,0.01),dim=1)
ys = 3*xs+4
# print(xs)
# print(ys)
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
        self.layer2 = nn.Linear(20, 64)
        self.layer3 = nn.Linear(64, 128)
        self.layer4 = nn.Linear(128, 64)
        self.layer5 = nn.Linear(64, 1)
    def forward(self,x):
        # fc1 = torch.matmul(x,self.w1)+self.b1
        # fc2 = torch.matmul(fc1,self.w2)+self.b2
        # fc3 = torch.matmul(fc2, self.w3) + self.b3
        # fc4 = torch.matmul(fc3, self.w4) + self.b4
        # fc5 = torch.matmul(fc4, self.w5) + self.b5
        fc1 = self.layer1(x)
        fc2 = self.layer2(fc1)
        fc3 = self.layer3(fc2)
        fc4 = self.layer4(fc3)
        fc5 = self.layer5(fc4)
        return fc5
if __name__ == '__main__':

    net = line() # 模型实例

    opt = optim.Adam(net.parameters())  # 优化器，Adam，Adam 自带学习率， Adam 快

    loss_func = torch.nn.MSELoss()  # 损失函数 MSELoss 均方损失函数

    plt.ion()
    for epoch in range(1000):
        out = net.forward(xs)   # 前向算法

        loss = loss_func(out,ys)    # 损失函数求损失

        opt.zero_grad() # 清空梯度

        loss.backward() # 反向传播求梯度，求导

        opt.step()  # 更新所有参数

        if epoch % 5 ==0:
            print(loss.item())

            plt.cla()
            plt.title("loss%.4f" % loss.item())
            plt.plot(xs,ys,".")
            plt.plot(xs, out.detach())
            plt.pause(0.001)

    plt.ioff()
    plt.show()