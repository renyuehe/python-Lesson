#下采样 池化 特征降维
import torch
from torch import nn


def pooling():
    conv_img = torch.randn(1,1,5,5)
    print("conv_img:\n", conv_img)

    '''
    最大值池化,最大池化不会改变特征值,近似与高通滤波器的一种池化
    '''
    # max_pooling = nn.MaxPool2d(2)
    # out = max_pooling(conv_img)

    '''
    平均池化,一般不用,平均池化会改变特征值
    平均池化,只有在我们需要特征的平均特征的时候采用
    '''
    avg_pooling = nn.AvgPool2d(2)
    out = avg_pooling(conv_img)
    print("out:\n", out)

if __name__ == '__main__':
    pooling()