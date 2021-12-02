import torch,thop
from torch import nn

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.layers = nn.Sequential(
            nn.Conv2d(3,16,3,1),
            # nn.ReLU(),
            # nn.Conv2d(16,32,3,1),
            # nn.ReLU(),
            # nn.Conv2d(32,64,3,1)
        )
    def forward(self,x):
        return self.layers(x)

if __name__ == '__main__':
    conv = nn.Conv2d(3,16,3,1)
    x = torch.randn(1,3,16,16)

    net = Net()
    x = torch.randn(1,3,16,16)
    flops, params = thop.profile(net, (x,))
    print(net(x).shape)
    print(flops) # 打印计算量
    print(params) # 打印参数量 27 * 16 + 16

    pass