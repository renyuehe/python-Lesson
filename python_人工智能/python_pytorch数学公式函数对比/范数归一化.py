import torch

a = torch.ones((2,3))  #建立tensor
print(a)
a2 = torch.norm(a)      #默认求2范数
print(a)
a1 = torch.norm(a,p=1)  #指定求1范数
print(a1)
a3 = torch.norm(a, dim=1)  # 指定维度
print(a3)

# a4 = torch.normalize(a, p=2, dim=1) # 归一化
# print(a4)

