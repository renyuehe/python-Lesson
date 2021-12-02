import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np

class PD():
    def __init__(self, Kp, Kd, setPoint):
        self.Kp = Kp
        self.Kd = Kd
        self.setPoint = setPoint

    def updata(self, setPoint, feedback):
        output = self.Kp * (1.0 * feedback + self.Kd * (feedback - setPoint))
        return output

# 定义数据
X1 = 5  # 横坐标固定为5，只改变小球的高度
X2 = 30  # 初始纵坐标
XP = 10  # 预设的纵坐标

v = 0  # 速度
a = 0  # 加速度

Kp = 0.3 # 比例速度
Kd = 2 # 微分项 阻尼

# 初始化误差
Err1 = X2 - XP #初始坐标-纵坐标
Err0 = 0 # 临时变量

# plt绘图
plt.figure(figsize=(12, 8), dpi=100)
plt.ion()

pd = PD(Kp, Kd, setPoint=0)

while True:
    # 清空旧的画布
    plt.cla()
    plt.xlim((-1, 20))
    plt.ylim((-1, 20))
    plt.plot([-1, 20], [XP, XP], 'r-') # 线

    # rgeion
    a = pd.updata(Err0, Err1)

    v = v - a # 调整速度
    X2 = X2 + v # 调整距离

    # endregion
    Err0 = Err1  # 保留旧的误差
    Err1 = X2 - XP  #调整误差

    plt.scatter(X1, X2,  # 散点的横、纵坐标序列
                s=30,    # 点
                c='blue',
                label="PD Algorithm")

    plt.legend()  # 显示图例说明

    plt.pause(0.008)