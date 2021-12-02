import torch
from torch import optim
from torch import nn

tags = torch.arange(12).reshape(3,4)
tags.float()
y = torch.ones((3,4))
y.float()
print(tags)
print(y)

print((tags -y) ** 2)

# net = nn.Module()
# opt = optim.Adam(net.parameters())

loss = torch.mean((tags - y) ** 2)  # 均方差，因为 tags 和 y 不是一个值而是一堆值，损失必须是一个标量，只有损失是标量才可以求导，所以这里要做个平均
print(loss)
# loss.requires_grad = True
print(loss)
loss.backward()

# ret = loss.backward()  # 自动求导