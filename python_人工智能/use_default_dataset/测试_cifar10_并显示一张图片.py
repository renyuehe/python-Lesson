# datasets 数据集
# transforms 归一化后的数据
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from torch.nn.functional import one_hot
import numpy as np

import warnings
warnings.filterwarnings('ignore')

# 数据集
train_dataset = datasets.CIFAR10(root=r"D:\Desktop\data\CIFAR10_data",train=True,  download=False)
test_dataset = datasets.CIFAR10(root=r"D:\Desktop\data\CIFAR10_data",train=False,  download=False)

print(np.array(train_dataset.data).shape)
print(np.array(train_dataset.targets).shape)

print(np.array(test_dataset.data).shape)
print(np.array(test_dataset.targets).shape)

print(train_dataset.classes)#得到标签的对应含义
print(train_dataset.targets[3])

unloader = transforms.ToPILImage()
img = unloader(train_dataset.data[0])
img.show()