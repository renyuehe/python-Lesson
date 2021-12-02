import torch
x1 = torch.tensor([2,4,6,8],dtype=torch.float32,requires_grad=True)
x2 = torch.tensor([1,2,3,4],dtype=torch.float32,requires_grad=True)
print("========= x1 and x2 ===========")
print(x1)
print(x2)


y = x1 - x2
print("========= x1 - x2 ===========")
print(y)

# print("-------------")
# print(y)
# y = y[0:2]
# y = y[2:4]
# print(y)
# print("-------------")

z1 = y ** 2
z2 = 4 * y


print("=========== z1 z2 ============")
print(z1)
print(z2)
print("=========== scalar ============")
# 采用 mean 求损失的时候,反向求导需要随对所有的结果都除以4
# z1_scalar = z1.mean()
# z2_scalar = z2.mean()
z1_scalar = z1.sum()
z2_scalar = z2.sum()
print(z1_scalar)
print(z2_scalar)
print("=======\=====grad==============")
print(x1.grad)
print(x2.grad)
z1_scalar.backward(retain_graph = True)    # retain_graph 会让保持 grad ,下一个 grad 会和保持的相加
# print(loss1,loss2)
print(x1.grad)
print(x2.grad)
z2_scalar.backward()    # 这时会引发错误
print(x1.grad)
print(x2.grad)