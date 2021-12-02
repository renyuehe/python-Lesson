from collections import OrderedDict
from torch import nn

layers = []
for i in range(3):
    conv = nn.Conv2d(1,1*i,3)
    layers.append((f"{i}", conv))

print(layers)

ret = OrderedDict(layers)
print(ret)