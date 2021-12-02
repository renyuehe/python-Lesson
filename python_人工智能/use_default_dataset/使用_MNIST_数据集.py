
# datasets 数据集
# transforms 归一化后的数据
from torchvision import datasets, transforms
import warnings
warnings.filterwarnings('ignore')

from torch.utils.data import DataLoader
from torch.nn.functional import one_hot

#数据集,测试
#root:放在哪个位置
#Train: true训练集， false测试机
train_dataset = datasets.MNIST(root=r"D:\Desktop\data\MNIST_data",train=True, transform=transforms.ToTensor(), download=True)
test_dataset = datasets.MNIST(root=r"D:\Desktop\data\MNIST_data",train=False, transform=transforms.ToTensor(), download=True)

# print(test_dataset.data.size())
# print(test_dataset.targets.size())
# print(type(test_dataset.data[0]))

# ToPILImage 拿到图片
# img_data = train_dataset.data[0]
# unloader = transforms.ToPILImage()
# img = unloader(img_data)
# img.show()

train_dataloader  = DataLoader(train_dataset, batch_size=1, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=1, shuffle=True)

for i , (img, label) in enumerate(train_dataloader):
    print(img)
    print(img.shape)
    print(label)
    print(one_hot(label, 10))
    exit()