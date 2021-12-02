import torch
from torch import nn

class Net1(nn.Module):
    def __init__(self):
        super(Net1, self).__init__()

        self.fc_layers = nn.Sequential(
            nn.Linear(784, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 10),
            nn.Softmax(dim=1)
        )

    def forward(self, x):
        return self.fc_layers(x)

class Net2(nn.Module):
    def __init__(self):
        super(Net2, self).__init__()

        self.fc_layers = nn.Sequential(
            nn.Linear(32*32*3, 2048),
            nn.ReLU(),
            nn.Linear(2048, 1024),
            nn.ReLU(),
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 10),
            nn.Softmax(dim=1)
        )
    def forward(self, x):
        return self.fc_layers(x)

if __name__ == "__main__":
    # net = Net1()
    # x = torch.randn(3,784)
    # y = net(x)
    # print(y.shape)

    net = Net2()
    x = torch.randn(3,32*32*3)
    y = net(x)
    print(y)