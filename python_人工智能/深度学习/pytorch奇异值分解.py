import torch

a = torch.tensor([[1.,2.],[3.,4.]])
b = torch.tensor([[1.,2.],[3.,4.],[5.,6.]])
print(
    # 特征值分解 必须是方阵
    torch.eig(a, eigenvectors=True),
    # 奇异值分解 可以不是方阵
    print(torch.svd(b))
)