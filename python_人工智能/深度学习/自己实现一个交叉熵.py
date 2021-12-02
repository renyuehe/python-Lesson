# 交叉熵
import torch
from torch import nn

class CE(nn.Module):
    def __init__(self):
        super(CE, self).__init__()

    def forward(self, y, p):
        out = -(y*torch.log(p)) # y是p(x)预测出来的概率值， p是p(x)真实的概率值
        out = torch.mean(out) # 加起来求平均数
        return out