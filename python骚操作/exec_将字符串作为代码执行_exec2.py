# def myfun():
#
#     exec('''
# def foo():
#     return "bar"
#
# print(foo())
#     ''')
#
# myfun()



def myfun():

    exec('''

from functools import partial
import math
def yolox_warm_cos_lr(
    lr,
    min_lr_ratio,
    total_iters,
    warmup_total_iters,
    warmup_lr_start,
    no_aug_iter,
    iters,
):
    min_lr = lr * min_lr_ratio
    if iters <= warmup_total_iters:
        lr = (lr - warmup_lr_start) * pow(
            iters / float(warmup_total_iters), 2
        ) + warmup_lr_start
    elif iters >= total_iters - no_aug_iter:
        lr = min_lr
    else:
        lr = min_lr + 0.5 * (lr - min_lr) * (
            1.0  + math.cos( math.pi * (iters - warmup_total_iters) / (total_iters - warmup_total_iters - no_aug_iter)
            )
        )
    return lr

import matplotlib.pyplot as plt

lr = 1
min_lr_ratio = 0.5
total_iters = 10
warmup_total_iters = 4
warmup_lr_start = 1
no_aug_iter = -10
# xs = [1,2,3,4,5,6,7,8,9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

xs = []
for i in range(20):
    xs.append(i)

ys = []
for iter in xs:
    ys.append(yolox_warm_cos_lr(lr, min_lr_ratio, total_iters, warmup_total_iters, warmup_lr_start, no_aug_iter, iter))

plt.plot(xs, ys, label="like", c="blue", marker=".")
plt.legend()
plt.show()

    ''')

myfun()
