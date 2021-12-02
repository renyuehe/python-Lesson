import random
import matplotlib.pyplot as plt

# 构建 x 和 y 的对应关系 y = 3*x + 4
_x = [i/100 for i in range(100)]
_y = [3*e+4+random.random() for e in _x]

# 初始化, 随机 w 和 随机 b, 感知机公式 wx + b = h
w = random.random()
b = random.random()

#开启会话
plt.ion()
# 梯度下降操作次数
for i in range(30):
    # 一次数据源梯度下降操作（一组数据）
    for x, y in zip(_x, _y):
        # 感知机公式  h = w*x + b
        h = w * x + b       # 公式一
        # 均方損失
        loss = (h - y) ** 2 # 公式二

        # 对 w 进行求导（求梯度），对损失函数的求导公式。
        # 复合函数求导公式。
        # 操作：
        # 先对公式二求导得  2 * (h - y)，
        # 再对公式一求导 得 x，
        # 再相乘得 2 * (h - y) * x
        # 再将导数方向指向下降方向 得 - 2 * (h-y) * x
        dw = -2 * (h - y) * x # 对 w 求导（求梯度）
        # 对 B 求导，复合函数，
        # 公式一中 B 是个 变量 （ x^1 的导数为 1），B 的导数 为 1
        # 公式二中 B 的导数为 2 * (h - y)
        # 也做导数方向指向下降方向 得 - 2 * (h-y)
        db = -2 * (h - y)   # 对 b 求导（求梯度）

        # w 和 b 做梯度下降
        w = dw * 0.1 + w
        b = db * 0.1 + b

        print(w, b, loss)
        #清屏
        plt.cla()
        plt.plot(_x, _y, ".")
        v = [w * e + b for e in _x]
        plt.plot(_x, v)
        plt.pause(0.001)#暂停0.001秒
#关闭会话
plt.ioff()
plt.show()
