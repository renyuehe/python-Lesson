'''
1. all_gather 不进行梯度反向传播
首先，torch.distributed.all_gather 本身是不会进行梯度的反向传播的.


运行该代码，首先，其会打印出没采用 all_gather 的真正的梯度函数y.grad_fn.
然后，调用 all_gather 后，ys 的输出是没有 grad_fn 的，可以理解为其是没有梯度反向传播的.

实际场景中，推荐采用 torch.no_grad() 封装 all_gather 函数，以显式地表明没有梯度进行反向传播.
'''
import torch
import os

batch_size = 16
rank = int(os.environ.get('OMPI_COMM_WORLD_RANK', '0'))
world_size = int(os.environ.get('OMPI_COMM_WORLD_SIZE', '1'))
bs_each = batch_size // world_size
device_id = int(os.environ.get('OMPI_COMM_WORLD_LOCAL_RANK', '0'))
torch.cuda.set_device(device_id)


'''
如果报错：RuntimeError: Distributed package doesn't have NCCL built in
windows不支持NCCL backend

解决方案：
在dist.init_process_group语句之前添加backend=‘gloo’，也就是在windows中使用GLOO替代NCCL。
'''
torch.distributed.init_process_group(
    # backend='nccl',
    backend='gloo',
    init_method='tcp://localhost:12345',
    rank=rank,
    world_size=world_size,
)

#
from torch import nn

model = nn.Linear(1, 1, bias=False)
model.weight.data[:] = 1.
model = model.cuda()
x = torch.ones((bs_each, 1), requires_grad=True).cuda()
y = model(x)
ys = [torch.zeros_like(y) for i in range(nn.get_mpi_size())]
#
torch.distributed.all_gather(ys, y)
print(y.grad_fn)
#<MmBackward object at 0x7f2073fc3ba8>
for sub_y in ys:
     print(sub_y.grad_fn)
     #None