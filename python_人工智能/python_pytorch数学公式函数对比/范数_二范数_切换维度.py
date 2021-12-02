import torch
a = torch.arange(9, dtype=torch.float) - 4
print(a)

b = a.reshape(3,3)
print(b)

ret = torch.norm(b, dim=0) #-1代表最后维
print(ret)

ret = torch.norm(b, dim=1) #-1代表最后维
print(ret)

ret = torch.norm(b, dim=-1) #-1代表最后维
print(ret)