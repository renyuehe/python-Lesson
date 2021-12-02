在PyTorch中，一共有10种类型的tensor：

torch.FloatTensor (32-bit floating point)
torch.DoubleTensor (64-bit floating point)
torch.HalfTensor (16-bit floating point 1)
torch.BFloat16Tensor (16-bit floating point 2)
torch.ByteTensor (8-bit integer (unsigned))
torch.CharTensor (8-bit integer (signed))
torch.ShortTensor (16-bit integer (signed))
torch.IntTensor (32-bit integer (signed))
torch.LongTensor (64-bit integer (signed))
torch.BoolTensor (Boolean)
由此可见，默认的Tensor是32-bit floating point，这就是32位浮点型精度的Tensor。


torch.HalfTensor 半精度, 既有优势也有劣势。
当有优势的时候就用torch.HalfTensor，而为了消除torch.HalfTensor的劣势，我们带来了两种解决方案：

1，梯度scale，这正是上一小节中提到的torch.cuda.amp.GradScaler，
通过放大loss的值来防止梯度的underflow（这只是BP的时候传递梯度信息使用，
真正更新权重的时候还是要把放大的梯度再unscale回去）；

2，回落到torch.FloatTensor，这就是混合一词的由来。那怎么知道什么时候用torch.FloatTensor，
什么时候用半精度浮点型呢？这是PyTorch框架决定的，在PyTorch 1.6的AMP上下文中，
如下操作中tensor会被自动转化为半精度浮点型的torch.HalfTensor：


如何在PyTorch中使用自动混合精度？
答案就是autocast + GradScaler。

