import numpy as np
import  matplotlib.pyplot as plt

x = np.arange(0.1, 10, 0.1)
y = np.log(x)
y1 = np.log(x)/np.log(3) # log以3为底
y2 = np.log(x)/np.log(0.5) # log以0.5为底

plt.plot(x, y)
plt.plot(x, y1)
plt.plot(x, y2)

plt.show()