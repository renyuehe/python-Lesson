import torch    # 导入 torch
import matplotlib.pyplot as plt # 绘图
from torch import optim # 优化器

xs = torch.unsqueeze(torch.arange(0.01,1,0.01),dim=1)   # 升维度
ys = 3*xs+4
# print(xs)
# print(ys)
# plt.plot(xs,ys,".")
# plt.show()

#创建模型
class line(torch.nn.Module):
    def __init__(self):
        super(line, self).__init__()
        # 神经元连接
        self.w1 = torch.nn.Parameter(torch.randn(1,20))
        self.b1 = torch.nn.Parameter(torch.randn(20))
        self.w2 = torch.nn.Parameter(torch.randn(20,64))
        self.b2 = torch.nn.Parameter(torch.randn(64))
        self.w3 = torch.nn.Parameter(torch.randn(64, 128))
        self.b3 = torch.nn.Parameter(torch.randn(128))
        self.w4 = torch.nn.Parameter(torch.randn(128, 64))
        self.b4 = torch.nn.Parameter(torch.randn(64))
        self.w5 = torch.nn.Parameter(torch.randn(64, 1))
        self.b5 = torch.nn.Parameter(torch.randn(1))
    # 前向算法
    def forward(self,x):
        fc1 = torch.matmul(x,self.w1)+self.b1
        fc2 = torch.matmul(fc1,self.w2)+self.b2
        fc3 = torch.matmul(fc2, self.w3) + self.b3
        fc4 = torch.matmul(fc3, self.w4) + self.b4
        fc5 = torch.matmul(fc4, self.w5) + self.b5
        return fc5
if __name__ == '__main__':
    net = line()    # 实例模型
    opt = optim.Adam(net.parameters())  # 优化器 Adam
    loss_func = torch.nn.MSELoss()  # 损失函数

    # 开启绘画
    plt.ion()

    # 1000 次 梯度下降
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

    plt.ioff()  # 结束绘画

    plt.show()