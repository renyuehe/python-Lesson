import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import random
import numpy as np

# 生成一个想要的正太分布的散点
x = np.random.normal(0, 1, 100)
y = np.random.normal(0, 1, 100)
z = np.random.normal(0, 1, 100)

# pyplot 转化为立方体绘制
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x, y, z) # 散开

plt.show()