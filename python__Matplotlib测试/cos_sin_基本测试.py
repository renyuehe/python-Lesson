import matplotlib.pyplot as plt
import numpy as np

# 生成要给线段
x = np.linspace(0, 2*np.pi, 100)

y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1)
plt.plot(x, y2)

plt.title("sin & cos")
plt.xlabel("x")
plt.ylabel("y")
plt.show()