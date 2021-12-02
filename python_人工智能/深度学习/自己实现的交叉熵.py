import torch
from torch import nn

class CE(nn.Module):
    def __init__(self):
        super(CE, self).__init__()

    def cross_entropy(self, y, p):
        out = -(y*torch.log(p))
        out = torch.mean(out)
        return out