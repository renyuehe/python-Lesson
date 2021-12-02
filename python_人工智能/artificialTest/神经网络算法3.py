import torch
from torch import nn    # 神经元
import matplotlib.pyplot as plt # 绘图器
from torch import optim # 优化器

# 先生成一个一维张量， 再对一维张量升维
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
        # self.layer1 = nn.Linear(1,20)
        # self.layer2 = nn.Linear(20, 64)
        # self.layer3 = nn.Linear(64, 128)
        # self.layer4 = nn.Linear(128, 64)
        # self.layer5 = nn.Linear(64, 1)
        self.fc_layers = nn.Sequential(
            nn.Linear(1,20),
            nn.Linear(20,64),
            nn.Linear(64,128),
            nn.Linear(128,64),
            nn.Linear(64,1)
        )
    def forward(self,x):
        # fc1 = self.layer1(x)
        # fc2 = self.layer2(fc1)
        # fc3 = self.layer3(fc2)
        # fc4 = self.layer4(fc3)
        # fc5 = self.layer5(fc4)
        return self.fc_layers(x)
if __name__ == '__main__':
    net = line()    # 模型实例

    # 优化器
    opt = optim.Adam(net.parameters())

    # 损失函数
    loss_func = torch.nn.MSELoss()

    # 开始绘图
    plt.ion()
    for epoch in range(1000):
        # 前向算法
        out = net.forward(xs)

        # 损失函数 计算损失
        loss = loss_func(out,ys)

        opt.zero_grad()
        loss.backward() #
        opt.step()

        if epoch % 5 ==0:
            print(loss.item())

            plt.cla() # 清屏
            plt.title("loss%.4f" % loss.item()) # 显示损失
            plt.plot(xs,ys,".") # 将列表点画线
            plt.plot(xs,out.detach())   # ？？？

            plt.pause(0.001) # 动画间隔暂停

    # 结束绘图
    plt.ioff()
    plt.show()