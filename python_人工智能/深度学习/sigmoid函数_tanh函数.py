import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-9.9, 10, 0.1)
y = 1/(1+np.exp(-x)) # sigmoid函数
y1 = (np.exp(x) - np.exp(-x))/(np.exp(x) + np.exp(-x)) # tanh函数
plt.plot(x, y)
plt.plot(x, y1)

plt.show()