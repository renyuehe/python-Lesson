import torch
from torchvision import datasets, transforms

import warnings
warnings.filterwarnings('ignore')

from torch.utils.data import DataLoader
from torch.nn.functional import one_hot

from net import Net1
from torch import optim, nn


#root:放在哪个位置
#Train: true训练集， false测试机
train_dataset = datasets.MNIST(root=r"D:\Desktop\data\MNIST_data",train=True, transform=transforms.ToTensor(), download=True)
test_dataset = datasets.MNIST(root=r"D:\Desktop\data\MNIST_data",train=False, transform=transforms.ToTensor(), download=True)

train_dataloader  = DataLoader(train_dataset, batch_size=512, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=512, shuffle=True)


if __name__ == "__main__":
    net = Net1()

    # net.load_state_dict(torch.load("params/1.pt"))

    opt = optim.Adam(net.parameters())
    loss_func = nn.MSELoss()

    for epoch in range(10000):
        for i, (img, label) in enumerate(train_dataloader):
            net.train()

            # img (N,1,28,28) to (N, 784)
            img = img.reshape(-1, 784)
            out = net(img)
            label = one_hot(label, 10).float()
            # print(img.shape)
            # print(label.shape)

            loss = loss_func(out, label)

            opt.zero_grad()
            loss.backward()
            opt.step()

            if i%10==0:
                print("train_loss ", loss.item())

        for i, (img, label) in enumerate(test_loader):

            net.eval()

            # img (N,1,28,28) to (N, 784)
            img = img.reshape(-1, 784)
            out = net(img)
            label = one_hot(label, 10).float()
            # print(img.shape)
            # print(label.shape)

            loss = loss_func(out, label)

            # opt.zero_grad()
            # loss.backward()
            # opt.step()

            if i%10==0:
                print("test_loss ", loss.item())

        torch.save(net.state_dict(), f"params/{epoch}.pt")
