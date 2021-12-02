# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:39:10 2020
答疑：李立宗  lilizong@gmail.com
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('image/text.jpg',0)
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

