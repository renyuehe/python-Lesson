import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
x = np.linspace(-100, 100, 100)
y = 1/x

ax = fig.add_subplot(111)
ax.plot(x, y)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

# remove the ticks from the top and right edges
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.axhline(0,color = 'red',linestyle = '--',alpha = 0.5)

plt.show()
