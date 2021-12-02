import torch
from torch import nn,optim

def padding():
    img = torch.randn(1,1,5,5)# N C HW

    '''
    in_channels： 输入的 核（通道：c）的个数
    out_channels： 输出的 核的个数
    kernel_size： 核的大小(x, y),或者 直接写 x 等价于 (x, x)
    padding：就是padding，可以解决模型太深 hw 变小不能更神的问题, padding一般只用在保证输入和输出的大小一致 ，padding 有时候也用于下采样 图像正好是下采样的倍数
    bias:偏移量,相当于 xw+b=h 中的 b
    '''
    conv = nn.Conv2d(in_channels=1, #
                     out_channels=1, #
                     kernel_size=(1,1),
                     padding=1, # padding
                     bias=False,
                     )

    out = conv(img)
    print(out)
    print(out.shape)



if __name__ == '__main__':
    padding();
    pass