import torch
from torch.autograd import Variable

#生成一个内容为[2,4]的张量，Varibale 默认是不要求梯度的，如果要求梯度，
#需要加上requires_grad=True来说明
a = Variable(torch.Tensor([[2,4]]),requires_grad=True)
b = torch.zeros(1,2)

b[0,0] = a[0,0]**2+a[0,1]
b[0,1] = a[0,1]**3+a[0,0]
out = 2*b

print("a=",a)
print("a.grad=",a.grad)  #求out对a的偏导
print("--------------对tensor 做切割---------------")
# print(out[0][0])
# print(out[0][1])

out1 = out[0][0]
out2 = out[0][1]

# print(type(out1))
# print(type(b))
# print(type(out))
# print(b.requires_grad)
# print(out.requires_grad)
# print(out1.requires_grad)
# print(out1.grad)
print("-----------------------------")

#括号里面的参数要传入和out维度一样的矩阵,必须写参数,因为out不是标量
#这个矩阵里面的元素会作为最后加权输出的权重系数
# out.backward(torch.FloatTensor([[1,1]]))
# out.backward()

out1.backward()
out2.backward()


print("a=",a)
print("a.grad=",a.grad)  #求out对a的偏导
print("out=",out)
