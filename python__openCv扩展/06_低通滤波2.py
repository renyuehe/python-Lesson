# -*- coding: utf-8 -*-
"""
答疑：李立宗  lilizong@gmail.com
该程序在15.7.1上改进，增加了图像生成
其他没有区别
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2
img=np.random.randint(0,1,(512,512),dtype=np.uint8)
for i in range(0,512,1):
    img[:,i]=img[:,i]+ np.sin(i/30)*100+np.random.randint(1,30)+100
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dftShift = np.fft.fftshift(dft)
rows, cols = img.shape
crow,ccol = int(rows/2) , int(cols/2)
mask = np.zeros((rows,cols,2),np.uint8)
#两个通道，与频谱图像匹配
mask[crow-30:crow+30, ccol-30:ccol+30] = 1
fShift = dftShift*mask
ishift = np.fft.ifftshift(fShift)
iImg = cv2.idft(ishift)
iImg= cv2.magnitude(iImg[:,:,0],iImg[:,:,1])
plt.subplot(221),plt.imshow(img, cmap = 'gray')
plt.title('original'), plt.axis('off')
plt.subplot(223),plt.imshow(iImg, cmap = 'gray')
plt.title('inverse'), plt.axis('off')
r=500
plt.subplot(222)
plt.plot(img[r,:],color='r')
plt.subplot(224)
plt.plot(iImg[r,:],color='g')
plt.show()
