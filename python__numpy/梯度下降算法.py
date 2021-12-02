import random
import matplotlib.pyplot as plt

# 模拟真实数据
_x = [i/100 for i in range(100)] # 列表推导式 归一化
# _y = [e*3+4+random.random() for e in _x]
_y = [e*e*e+200+random.random()*10 for e in _x]
# print(_x)
# print(_y)
#
# plt.plot(_x, _y, ".")
# plt.show()

w = random.random() # 如果 w 不是一个常数呢
b = random.random()

for i in range(30):
    # zip 把可迭代对象组装成一个 python 内置函数
    # 循环遍历每一个真是数据 （）
    for x,y in zip(_x, _y):
        z = w * x + b
        o = z - y
        loss = o ** 2 # 损失
        # print(loss)

        dw = - 2 * o * x    # 对 w 求导
        db = -2 * o         # 对 b 求导

        w = dw * 0.1 + w    # 函数
        b = db * 0.1 + b    #

        print(w, b, loss)

plt.plot(_x, _y, ".")
v = [w*e + b for e in _x] # v 是 基于 w*x + b 的一元一次函数，但是原数据不是直线分布的时候，这个时候 w 不应该是常数
plt.plot(_x,v)
plt.show()