import torch

func=nn.CrossEntropyLoss()
a=torch.Tensor([[ 0.0606,0.1610,0.2990,0.2101, 0.5104],
                [0.6388,0.4053, 0.4196, 0.7060, 0.2793],
                [ 0.3973,0.6114, 0.1127, 0.7732, 0.0592]])
b=[3,1,0]
b=torch.Tensor(b)
loss=func(a,b.long()) #交叉熵的第二个参数 tag 不需要one-hot 函数内部自动会做 one-hot
loss=func(a,b.long())
print("总loss:",loss)

###################################

a1=torch.Tensor([ 0.0606,0.1610,0.2990,0.2101, 0.5104])
a2=torch.Tensor([0.6388,0.4053, 0.4196, 0.7060, 0.2793])
a3=torch.Tensor([ 0.3973,0.6114, 0.1127, 0.7732, 0.0592])

b1=torch.Tensor([3])
b2=torch.Tensor([1])
b3=torch.Tensor([0])

loss_1=func(a1,b1.long())
loss_2=func(a2,b2.long())
loss_3=func(a3,b3.long())
