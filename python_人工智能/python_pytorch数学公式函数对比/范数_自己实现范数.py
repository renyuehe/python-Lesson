import torch

data = torch.Tensor([[3,4],[5,6],[7,8],[9,8],[6,5]])
center = torch.Tensor([[1,1],[2,2],[2,2],[2,2],[1,1]])

diff = data - center
print(diff)

ret1 = torch.sqrt(torch.sum(torch.pow(diff, 2),dim=1))
ret2 = torch.norm(diff, p=2, dim=1)

print(ret1)
print(ret2)

print(torch.div(ret2))