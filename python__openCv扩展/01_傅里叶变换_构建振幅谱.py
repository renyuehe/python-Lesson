
# 构建振幅谱
# spectrum 光谱
# magnitud 震级

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img/1.jpg', 0)
img_float32 = np.float32(img)
print(img_float32.shape)

# 传入灰度图是 二维的，因为每个像素只有一个值 。
# 返回值根据参数来定， flags=cv2.DFT_COMPLEX_OUTPUT 表示每个像素都返回实部 和 虚部的值，所以是三维的。
# 如果参数是flags=cv2.DFT_REAL_OUTPUT 则每个像素还是只有一个值, 是二维的。
# 显示傅里叶变换的结果需要使用
# 实数图像（real image）和虚数图像（complex image），
# 或 幅度图像（magnitute image）加相位图像（phase image）
dft = cv2.dft(img_float32, flags = cv2.DFT_COMPLEX_OUTPUT)
print(dft.shape)
# dft1 = dft[1,1,1]
# dft0 = dft[1,1,0]
# print(dft0)
# print(dft1)
#
# cv2.imshow("dft 0", dft[0])
# cv2.imshow("dft 1", dft[1])
#
#
# # 将低频分布在中心、高频分布在外围
# dft_shift = np.fft.fftshift(dft)
# print(dft_shift.shape)
#
# # 得到灰度图能表示的形式
# magnitud 震级
# magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
# print(magnitude_spectrum.shape)
# # dft1 = magnitude_spectrum[1,1,1]
# # dft0 = magnitude_spectrum[1,1,0]
# # print(dft0)
# # print(dft1)
#
#
# plt.subplot(121),plt.imshow(img, cmap = 'gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
#
# plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
# plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
#
# plt.show()