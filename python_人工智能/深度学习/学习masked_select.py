import torch

x = torch.tensor([1,2,3,4,5])
print(
x
)

mask = torch.lt(x, 3)
print(
mask
)

ret = torch.masked_select(x , mask)
print(
ret
)