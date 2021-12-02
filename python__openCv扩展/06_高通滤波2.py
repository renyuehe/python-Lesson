# -*- coding: utf-8 -*-
"""
答疑：李立宗  lilizong@gmail.com
该程序在15.5.1上改进，增加了图像生成
其他没有区别
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2
img=np.random.randint(0,1,(512,512),dtype=np.uint8)
for i in range(0,512,1):
    img[:,i]=img[:,i]+ np.sin(i/30)*100+np.random.randint(1,30)+100
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
rows, cols = img.shape
crow,ccol = int(rows/2) , int(cols/2)
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
ishift = np.fft.ifftshift(fshift)
iimg = np.fft.ifft2(ishift)
iimg = np.abs(iimg)
plt.subplot(221),plt.imshow(img, cmap = 'gray')
plt.title('original'),plt.axis('off')
plt.subplot(223),plt.imshow(iimg, cmap = 'gray')
plt.title('iimg'),plt.axis('off')
r=500
plt.subplot(222)
plt.plot(img[r,:],color='r')
plt.subplot(224)
plt.plot(iimg[r,:],color='g')
plt.show()

