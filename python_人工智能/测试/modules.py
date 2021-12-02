from torch import nn
import torch

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 12, 3)

    def forward(self, x):
        pass


if __name__ == '__main__':
    net = Net()
    print(net.modules())
    for i in net.modules():
        print(i)
