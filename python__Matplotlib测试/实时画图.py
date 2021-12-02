import matplotlib as mpl
import matplotlib.pyplot as plt

ax = []
ay = []

# 打开实时画图
plt.ion()
for i in range(100):
    ax.append(i)
    ay.append(i**2)
    plt.clf() # 清除缓存
    plt.plot(ax, ay)
    plt.pause(0.001)

# 关闭试试画图
plt.ioff()
