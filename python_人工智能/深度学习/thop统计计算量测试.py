import torch,thop
from torch import nn

if __name__ == '__main__':
    #现在不支持这种写法了,需要加入到 nn 中去
    conv = nn.Conv2d(3,16,3,1)
    x = torch.randn(1,3,16,16)

    x = torch.randn(1,3,16,16)
    flops, params = thop.profile(conv, (x,))

    print(flops) # 打印计算量
    print(params) # 打印参数量 27 * 16 + 16

    pass