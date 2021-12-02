import random
import matplotlib.pyplot as plt

_x = [i/100 for i in range(100)] # 列表推导式 归一化
_y = [e*3+4+random.random() for e in _x]
# _y = [e*e*e*100+4+random.random()*10 for e in _x]
# print(_x)
# print(_y)
#
# plt.plot(_x, _y, ".")
# plt.show()

w = random.random() # 因为我们知道是一元一次函数, 所以 w 是一个数, 更复杂的函数则需要用到线性代数的知识点。
b = random.random() # 常量

# 开启绘画
plt.ion()
for i in range(30):
    # zip 把可迭代对象组装成一个 python 内置函数
    for x,y in zip(_x, _y):
        z = w * x + b
        o = z - y
        loss = o ** 2 # 损失
        # print(loss)

        dw = - 2 * o * x    # 损失函数 和 模型函数 是一个复合函数，这里对模型的 w 求导，已知函数才能推出的导数
        db = -2 * o         # 损失函数 和 模型函数 是一个复合函数，这里对模型的 b 求导，已知函数才能推出的导数

        w = dw * 0.1 + w    # 函数
        b = db * 0.1 + b    # 常量

        print(w, b, loss)

        # 清屏幕
        plt.cla()
        plt.plot(_x, _y, ".")
        v = [w * e + b for e in _x]
        plt.plot(_x, v)
        plt.pause(0.0001)
        plt.show()

# 关闭绘画