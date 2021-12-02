import  numpy as np
import matplotlib.pyplot as plt

x = [i/100 for i in range(100)]
y = [i*i for i in x]


plt.plot(x,y)
plt.show()