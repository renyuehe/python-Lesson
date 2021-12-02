# 包 torch 包含了多维张量的数据结构以及基于其上的多种数学操作。
# 另外，它也提供了多种工具，其中一些可以更有效地对张量和任意类型进行序列化。

import torch
import numpy as np

# 如果obj 是一个pytorch张量，则返回True
a = torch.arange(2,10)
print(a)

print(torch.is_tensor(a))

print(torch.is_storage(a))

# 返回张量的个数
a = torch.randn(1,2,3,4,5)
print(torch.numel(a))

# 返回一个二维张量，对角线全是1

t2 = torch.eye(10, 10, out=None)
print(t2)

# numpy 桥
a = np.arange(10,20)
print(torch.from_numpy(a))

# 返回一个1维张量，包含在区间start 和 end 上均匀间隔的steps个点。 输出1维张量的长度为steps。
# linspace 线性空间
a = torch.linspace(2, 20, steps=18, out=None)
print(a)

# 返回一个1维张量，包含在区间 10start 和 10end上以对数刻度均匀间隔的steps个点。
# 输出1维张量的长度为steps。
a = torch.logspace(1, 3, steps=10, out=None)
print(a)

# 返回一个张量，
# 包含了从区间[0,1)的均匀分布中抽取的一组随机数，
# 形状由可变参数sizes 定义。
print(
    torch.rand(2,2, out=None)
)

# 返回一个张量，
# 包含了从标准正态分布(均值为0，方差为 1，即高斯白噪声)中抽取一组随机数，
# 形状由可变参数sizes定义。
print(
    torch.randn(3,3, out=None)
)

# 给定参数n，返回一个从0 到n -1 的随机整数排列。
print(
    torch.randperm(99, out=None)
)

# 返回一个1维张量，
# 长度为 floor((end−start)/step)。
# 包含从start到end，以step为步长的一组序列值(默认步长为1)。
print(
    torch.arange(1,6),
    torch.arange(3),
    torch.arange(2,10,0.5)
)

# 返回一个1维张量，有 floor((end−start)/step)+1 个元素。
# 包含在半开区间[start, end）从start开始，以step为步长的一组值。
# step 是两个值之间的间隔，即 xi+1=xi+step
print(
    # torch.range(1, 6, step=1, out=None)
)

# 返回一个全为标量 0 的张量，形状由可变参数sizes 定义。

print(
    torch.zeros(3, 3, out=None)
)


# 索引,切片,连接,换位Indexing, Slicing, Joining, Mutating Ops

# 在给定维度上对输入的张量序列seq 进行连接操作。
# torch.cat()可以看做 torch.split() 和 torch.chunk()的反操作。
# cat() 函数可以通过下面例子更好的理解。
x = torch.randn(2, 3)
print(x)
print(
    torch.cat((x, x, x), 0)
)

# 在给定维度(轴)上将输入张量进行分块儿。
x = torch.arange(27).reshape(3,3,3)
print(
    "---------\n",
    torch.chunk(x, 2, dim=1)
)


# 沿给定轴dim，将输入索引张量index指定位置的值进行聚合。
# torch.gather(input, dim, index, out=None) → Tensor
# input (Tensor) – 源张量
# dim (int) – 索引的轴
# index (LongTensor) – 聚合元素的下标
# out (Tensor, optional) – 目标张量
print()
t = torch.Tensor([[1,2],[3,4]])
print(
    t
)
print(
    print(torch.LongTensor([[0,0],[1,0]])),
    torch.gather(t, 1, torch.LongTensor([[0,0],[1,0]]))
)



# 沿着指定维度对输入进行切片，
# 取index中指定的相应项(index为一个LongTensor)，
# 然后返回到一个新的张量，
# 返回的张量与原始张量_Tensor_有相同的维度(在指定轴上)。
# 注意： 返回的张量不与原始张量共享内存空间。
# torch.index_select(input, dim, index, out=None) → Tensor
# input (Tensor) – 源张量
# dim (int) – 索引的轴
# index (LongTensor) – 聚合元素的下标
# out (Tensor, optional) – 目标张量
print()
x = torch.randn(3, 4)
indices = torch.LongTensor([0, 2])
print(x)
print(indices)
print(
    torch.index_select(x, 0, indices)
)
print(
    torch.index_select(x, 1, indices)
)

# 根据掩码张量mask中的二元值，取输入张量中的指定项( mask为一个 ByteTensor)，将取值返回到一个新的1D张量，
# 张量 mask须跟input张量有相同数量的元素数目，但形状或维度不需要相同。 注意： 返回的张量不与原始张量共享内存空间。
# torch.masked_select(input, mask, out=None) → Tensor
# input (Tensor) – 输入张量
# mask (ByteTensor) – 掩码张量，包含了二元索引值
# out (Tensor, optional) – 目标张量
print()
a =torch.Tensor([1,2,4,4,5])
print(a)
print(torch.masked_select(a, a<4))





