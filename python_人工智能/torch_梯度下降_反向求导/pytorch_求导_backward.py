import torch
from torch.autograd import Variable

#生成一个内容为[2,3]的张量，Varibale 默认是不要求梯度的，如果要求梯度，
#需要加上requires_grad=True来说明
#这里的Variable是为了设置变量，把a0=2,a1=3设置为两个变量
a = Variable(torch.tensor([2,3]).float(),requires_grad=True)
b = Variable(torch.tensor([3,3]).float(),requires_grad=True)
c = a * b
out=c.mean() #求均值

print("a=",a)
print("b=",b)
print("c=",c)
print("out=",out)

out.backward() # 只有标量可以求导

print(a.grad)  #求out对a的偏导, 这里 a 居然和 out 是有联系的！！！
print(b.grad)
