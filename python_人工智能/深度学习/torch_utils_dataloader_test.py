"""
    批训练，把数据变成一小批一小批数据进行训练。
    DataLoader就是用来包装所使用的数据，每次抛出一批数据
"""
import torch
from torch.utils.data import DataLoader
import torch.utils.data as Data
import numpy as np

x = torch.linspace(1, 10, 10) # linspace: 返回一个1维张量,包含在区间start和end上均匀间隔的step个点
y = torch.linspace(10, 1, 10)

# 把数据放在数据集中
torch_dataset = Data.TensorDataset(x, y) # 特点 __len__() 特点二 __getItem__(index)
# print(torch_dataset.__len__())

# 从数据集中每次抽出batch size个样本
loader = DataLoader(dataset=torch_dataset, batch_size=3, shuffle=False, num_workers=2,)

def show_batch():
    for batch_id, data in enumerate(loader):
        # print(batch_id, batch_x.shape, batch_y.shape)
        print(batch_id, type(data))

if __name__ == '__main__':
    show_batch()

    # print(x)
    # print(type(x))
    # print(x.shape)
    #
    # print(y)
    # print(type(y))
    # print(y.shape)
    #
    # print(torch_dataset)
    # print(type(torch_dataset))
    # print(torch_dataset.tensors)
    # print(torch_dataset[0])
    # print(torch_dataset[1])
    # print(torch_dataset.tensors[0])