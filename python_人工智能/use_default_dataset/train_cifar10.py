import torch
from torchvision import datasets, transforms

import warnings
warnings.filterwarnings('ignore')

from torch.utils.data import DataLoader
from torch.nn.functional import one_hot

from net import Net1,Net2
from torch import optim, nn

DEVICE = "cuda"

#root:放在哪个位置
#Train: true训练集， false测试机
train_dataset = datasets.CIFAR10(root=r"D:\Desktop\data\CIFAR10_data",train=True, transform=transforms.ToTensor(), download=False)
test_dataset = datasets.CIFAR10(root=r"D:\Desktop\data\CIFAR10_data",train=False, transform=transforms.ToTensor(), download=False)

train_dataloader  = DataLoader(train_dataset, batch_size=512, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=512, shuffle=True)

classesLen = len(train_dataset.classes)

if __name__ == "__main__":
    net = Net2().to(DEVICE)

    # net.load_state_dict(torch.load())

    opt = optim.Adam(net.parameters())
    loss_func = nn.MSELoss()

    for epoch in range(10000):
        for i, (img, label) in enumerate(train_dataloader):
            img,label = img.to(DEVICE), label.to(DEVICE)
            net.train()

            # img (N,1,28,28) to (N, 32*32*3)
            img = img.reshape(-1, 32*32*3)
            out = net(img)
            label = one_hot(label, classesLen).float()
            # print(img.shape)
            # print(label.shape)

            loss = loss_func(out, label)

            opt.zero_grad()
            loss.backward()
            opt.step()

            if i%10==0:
                print("train_loss ", loss.item())

        acc_sum = 0
        for i, (img, label) in enumerate(test_loader):
            img, label = img.to(DEVICE), label.to(DEVICE)
            net.eval()

            # img (N,1,32,32) to (N, 32*32*3)
            img = img.reshape(-1, 32*32*3)
            out = net(img)

            label = one_hot(label, classesLen).float()
            loss = loss_func(out, label)

            out = torch.argmax(out, dim=1)
            label = torch.argmax(label, dim=1)

            acc = torch.mean(torch.eq(out, label).float())
            acc_sum += acc
            if i%10==0:
                print("test_loss ", loss.item())

        print("acc ==>> " , acc_sum/i)

        # torch.save(net.state_dict())
