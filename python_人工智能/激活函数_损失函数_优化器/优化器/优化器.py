import torch

torch.optim.SGD()

'''
########################################
SGD（实现随机梯度下降算法）（momentum、nesterov 可选）
params 
lr 学习率
momentum 动量
weight_decay 权重惩罚 l2惩罚 l2正则化
dampening (flaot-可选)-动量抑制因子
nesterov(bool,可选)-使用nesterov动量

---------------------------------
普通SGD有点：
1、鲁棒性比较好，稳定
缺点：
1、慢
2、SGD跨越鞍点的能力是很弱的，不能解决局部最优解的问题，只有维度高的高的时候能增加跨越鞍点的能力
不推荐

---------------------------------
使用动量（Momentum）的随机梯度下降算法（SGD）
优点：加快收敛速度，有一定摆脱局部最优解的能力，一定程度上缓解了没有动量的时候的问题。
缺点：仍然继承了一部分SGD的缺点。

---------------------------------
使用牛顿加速度（NAG, Nesterov accelerated gradlent)随机梯度下降法（SGD）
可以理解为往标准动量中添加了一个矫正因子
理解策略：Momentum中小球会盲目的跟从下坡的速度，容易发生错误，所以需要一个更聪明的小球，
能提前知道他要去哪里，还要知道
优点：
缺点：

'''

# torch.optim.ASGD()

'''
#######################################
ASGD（随机平均梯度下降）（Averaged Stochastic Gradlent Descent)
简单的说 ASGD 就是用空间换时间的一种 SGD,详细可看论文
params：
lr： 学习率（默认 1e-2）
lambd：衰减项
alpha：eta更新指数
t0： 知名在那一次开始平均化（默认： 1e6）
weidght_decy(float,可选) -- 权重衰减
'''

# torch.optim.Adagrad()
'''
########################################
AdaGrad优化器：
独立的适应所有的模型参数的学习率，梯度越大，学习率越小，梯度越小，学习率越大

Adagrad 使用于数据稀疏或者分布不均很的数据集
但是实际上如果数据分布不均匀，

parms: 
lr: 学习率
lr_decay: 学习率衰减
weight_decay: 权重衰减，l2惩罚

优点：它可以自动调节学习率，不需要认为调节
缺点：
1、仍依赖仍共设置一个全局学习率，随着迭代次数增多，学习率会越来越小，最终会趋于0
2、收敛不稳定

不推荐
'''

'''
#######################################
AdaDelta算法
优点：避免在训练后期，学习率过小，初期和中期，加速效果不快，训练速度块
缺点：还是需要手动指定学习率，初始梯度很大的花，会导致整个训练过程学习率很小，
在训练模型的后期，模型会反复的在局部最小值附近抖动，从而导致学习时间变长。
'''

# torch.optim.Rprop()
'''
#######################################
Rprop(弹性反向传播）
1、
2、在网络前馈迭代中，连续误差梯度符号不变时，采用加速策略，加快训练速度；
当连续误差梯度符号变化时，采用减速策略，以期稳定收敛。但是这种从策略容易卡在鞍点。
3、

缺点：优化方法适用于 full-batch,不适用于 mini-batch，因此基本上没什么用
推荐程度：不推荐！
'''

# torch.optim.RMSprop()
'''
RMSProp(Root Mean Square Prop, 均方根传递）
RProp的改进版，也是Adgrad的改进版。

思想：梯度震动较大的项，在下降时，减小其下降速度；
对于振动幅度小的项，在下降时，加速其下降速度。
理解：
震动较大的时候，要么就是全局最优解，要么接近全局最优解。
局部最优解震动再大也不会比全局最优解大，局部最优解震动必然小于全局最优解震动。
那么RMSProp就是在全局最优解的时候减小下降速度，局部最优解的增加下降速度。

对于RNN有很好的效果。

推荐程度：推荐！RMSProp算法在经验上已经被证明是一种有效的算法。
'''

# torch.optim.Adam()

'''
Adam(AMSGrad)
将Momenteum算法和RMSProp算法结合起来使用的一种算法。
即用动量来累计梯度，又是的收敛速度更快同时使得破洞幅度更小，并进行偏差修正。


推荐程度：非常推荐，基本上是最常用的优化方法
'''

'''
Adamax
Adam的改进点
优点：对学习率上提供了一个个更简单的范围
'''

'''
Nadom
Adom的改进版，类似于带有Nesterov动量项的Adam，
Nadom对学习率又了更强的约束，同时对梯度的更新也有更直接的影响。
在想使用带动量的RMSprop，或者Adam的地方，大多可以使用Nadam取得更好的效果。
'''

'''
SparseAdam

优点：相当于Adam的稀疏张量的专用版本
推荐程度：推荐，在处理稀疏张量的时候
'''

'''
AdamW
adam的进化版，是目前训练神经网络最快的方式

优点：比Adam收敛的更快
缺点：只有fastai使用，缺乏方法的框架，而且也具有更大的争议性

推荐程度：观望！希望以后能成为主流。
'''

'''
L-BFGS(Limited-memory Broyden-Fletcher-Goldfarb-Shanno)
'''