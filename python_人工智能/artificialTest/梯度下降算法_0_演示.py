import random
import matplotlib.pyplot as plt

_x = [i/100 for i in range(100)]
_y = [3*e+4+random.random() for e in _x]


w = random.random() # 权重初始化为默认
b = random.random() # 偏移量初始化为默认

#开启会话
plt.ion()
# 梯度下降操作次数
for i in range(30):
    # 一次数据源梯度下降操作（一组数据）
    for x, y in zip(_x, _y):

        z = w * x + b
        o = z - y # 误差

        loss = o ** 2 # 均方差loss
        # loss = o

        # loss 对 o 求导 2*o
        # o对z求导 1
        # z 对 w 求导 x
        # 相乘 2 * o * 1 * w
        # 梯度下降 取反, - 2 * o * x
        dw = -2 * o * x #
        db = -2 * o
        # dw = -o #
        # db = -o

        print(dw, db, loss)

        # 更新梯度
        w = dw * 0.1 + w
        b = db * 0.1 + b

        # print(w, b, loss)
        #清屏
        plt.cla()
        plt.plot(_x, _y, ".") # 绘制 y

        v = [w * e + b for e in _x]
        plt.plot(_x, v)
        plt.pause(0.001)#暂停0.001秒

#关闭会话
plt.ioff()
plt.show()
