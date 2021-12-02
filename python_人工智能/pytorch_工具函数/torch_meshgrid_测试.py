import torch

'''
torch.meshgrid（）的功能是生成网格，可以用于生成坐标。
函数输入两个数据类型相同的一维张量，两个输出张量的行数为第一个输入张量的元素个数，列数为第二个输入张量的元素个数。

其中第一个输出张量填充第一个输入张量中的元素，各行元素相同；第二个输出张量填充第二个输入张量中的元素各列元素相同。
'''

print("-------- 二维网格:主要 ---------")
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6, 7])
grid_x, grid_y = torch.meshgrid(x, y, indexing='ij')
print(grid_x)
print(grid_y)


print("-------- 三维网格:拓展 ---------")
grid1, grid2, grid3 = torch.meshgrid(torch.arange(2), torch.arange(2), torch.arange(4))
print(grid1)
print(grid2)
print(grid3)