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
            nn.Linear(1,100),
            nn.ReLU(),
            nn.Linear(100,1)
        )
    def forward(self,x):
        return self.fc_layers(x) #通过 __call__ 魔法方法来调用的方式（直接对象()）
if __name__ == '__main__':
    net = line()    # 模型对象
    opt = optim.Adam(net.parameters(), lr=0.01)  # Adam 优化器， 优化器是该模型生成的优化器
    loss_func = torch.nn.MSELoss()  # 均方差损失
    plt.ion()

    i = 0
    for epoch in range(1000):
        print(i)
        i += 1
        out = net.forward(xs)   # 模型做前向运算 ，返回神经网络 sequencial,实际上返回的神经网络前向计算的结构，最后的out

        loss = loss_func(out,ys) # 神经网络输出求损失

        opt.zero_grad() # net优化器 清空梯度
        loss.backward() # 损失反向求梯度
        opt.step()  # 梯度更新，相当于 w-🔺w 。。。

        if epoch % 5 ==0:
            print(loss.item())

            plt.cla()
            plt.title("loss%.4f" % loss.item())
            plt.plot(xs,ys,".")
            plt.plot(xs,out.detach().numpy())
            plt.pause(0.001)

    plt.ioff()
    plt.show()