import torch
x = torch.tensor([[1,2,3,4], [5,6,7,8]],dtype=torch.float32,requires_grad=True)
y = x ** 2
z = y * 4
print(x)
print(y)
print(z)

loss1 = z.mean()
loss2 = z.sum()

# print("-------------")
# print(z)
z = z[0:1]
# z = z[2:4]
# print(z)
# print("-------------")


print(loss1,loss2)
print(x.grad)
loss1.backward(retain_graph=True)    # retain_graph 会让保持 grad ,下一个 grad 会和保持的相加
# print(loss1,loss2)
print(x.grad)
loss2.backward()    # 这时会引发错误
print(x.grad)
# print(loss1,loss2)