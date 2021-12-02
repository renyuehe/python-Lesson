'''
热力图的关键点生成
'''

import time
import numpy as np
import cv2
import matplotlib.pyplot as plt


def CenterLabelHeatMap(img_width, img_height, c_x, c_y, sigma):
    X1 = np.linspace(1, img_width, img_width)
    Y1 = np.linspace(1, img_height, img_height)
    [X, Y] = np.meshgrid(X1, Y1)
    X = X - c_x
    Y = Y - c_y
    D2 = X * X + Y * Y
    E2 = 2.0 * sigma * sigma
    Exponent = D2 / E2
    heatmap = np.exp(-Exponent)# e的x次幂, 只要x是负数y就小于1, x为0时y为1,要增大热力点的范围就是让-Exponent向0靠近。所以E2越大,热力点的范围就越大。
    return heatmap


#################另一种生成方法############


# Compute gaussian kernel
def CenterGaussianHeatMap(img_height, img_width, c_x, c_y, variance):
    gaussian_map = np.zeros((img_height, img_width))
    for x_p in range(img_width):
        for y_p in range(img_height):
            dist_sq = (x_p - c_x) * (x_p - c_x) + \
                      (y_p - c_y) * (y_p - c_y)
            exponent = dist_sq / 2.0 / variance / variance
            gaussian_map[y_p, x_p] = np.exp(-exponent)
    return gaussian_map


image_file = r'D:/Desktop/small_girl.jpg'
img = cv2.imread(image_file)
img = img[:, :, ::-1]

height, width, _ = np.shape(img)
cy, cx = height / 2.0, width / 2.0

start = time.time()
heatmap1 = CenterLabelHeatMap(width, height, cx, cy, 70)
t1 = time.time() - start

start = time.time()
heatmap2 = CenterGaussianHeatMap(height, width, cx, cy, 35)
t2 = time.time() - start

print(t1, t2)

plt.subplot(1, 2, 1)
plt.imshow(heatmap1)
plt.subplot(1, 2, 2)
plt.imshow(heatmap2)
plt.show()

print('End.')