import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = Image.open(r"sea.jpg")
plt.imshow(img)
# plt.show()

a = []
b = []
plt.ion()
for i in range(100):
    # a.append(i**2)
    # b.append(i)
    # #绘制折线图
    # plt.plot(b, a)
    # plt.pause(0.01)
    arr = np.array(img)
    zeroarr = np.arange(it for it in arr.shape).reshape(arr.shape)

    plt.imshow(img)
    plt.pause(0.01)

#关闭绘画
plt.ioff()
plt.show()