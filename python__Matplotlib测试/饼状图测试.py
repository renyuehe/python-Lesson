import matplotlib as mpl
import matplotlib.pyplot as plt

label = ["A", "B", "C", "D"]
num = [12, 30, 50, 8]

plt.pie(x=num, autopct="%.2f%%", explode=None, labels=label, colors="rgby",shadow=True, startangle=30)
plt.show()