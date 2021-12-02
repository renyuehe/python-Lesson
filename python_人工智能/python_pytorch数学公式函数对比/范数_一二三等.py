import torch
a = torch.arange(9, dtype=torch.float) - 4

print(a)

ret = torch.norm(a, p=1) # 一范数就是绝对值相加
print(ret)

# 开根号(16 + 9 + 4 + 1 + 1 + 4 + 9 + 16)
ret = torch.norm(a, p=2) # 二范数就是 (绝对值)平方和开根号 或者欧式距离
print(ret)

ret = torch.norm(a, p=3) # 三范数就是 绝对值的三次方和开三次根
print(ret)