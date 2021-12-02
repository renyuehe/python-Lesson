import torch as t
from torch.autograd import Variable as v
x = v(t.ones(2, 2), requires_grad=True)
y = x + 1
y.backward()