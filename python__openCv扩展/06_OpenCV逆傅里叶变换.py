#-*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:39:10 2020
答疑：李立宗  lilizong@gmail.com
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('image/lena.bmp',0)

dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dftShift = np.fft.fftshift(dft)

ishift = np.fft.ifftshift(dftShift)
iImg = cv2.idft(ishift)

iImg= cv2.magnitude(iImg[:,:,0],iImg[:,:,1])
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('original'), plt.axis('off')
plt.subplot(122),plt.imshow(iImg, cmap = 'gray')
plt.title('inverse'), plt.axis('off')
plt.show()

