import torch
x = torch.tensor([[1,2,3,4], [5,6,7,8]],dtype=torch.float32,requires_grad=True)
y = torch.tensor([[1,2],
                  [1,2],
                  [1,2],
                  [1,2],],dtype=torch.float32,requires_grad=True)
z = x @ y
print(y)

print("-------------")
print(z)

# z = z[0:1,0:1] # 对 z 输出矩阵 z 矩阵一个数进行求导
# z = z[1:2,0:1] # 对 z 输出矩阵 z 矩阵一个数进行求导
# z = z[0:1,1:2] # 对 z 输出矩阵 z 矩阵一个数进行求导
# z = z[1:2,1:2] # 对 z 输出矩阵 z 矩阵一个数进行求导

# z = z[:,0:1] # 对 z 输出矩阵 一个列求导 (此时是对一列的均值进行求导)
# z = z[:,1:2]
print(z)
# z = z[2:4]
# print(z)
print("-------------")

loss1 = z.mean()
print(x.grad)
print(y.grad)
loss1.backward()    # retain_graph 会让保持 grad ,下一个 grad 会和保持的相加
print(x.grad)
print(y.grad)