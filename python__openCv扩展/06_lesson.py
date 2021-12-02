#-*- coding: utf-8 -*-
#coding:utf-8
"""
Created on Mon Jun 22 14:39:10 2020
答疑：李立宗  lilizong@gmail.com
"""
import cv2
import numpy  as np
import matplotlib.pyplot  as plt

o=cv2.imread("image/lena.bmp",0)

of=cv2.dft(np.float32(o),flags=cv2.DFT_COMPLEX_OUTPUT)
ofs=np.fft.fftshift(of)

rows,cols=o.shape
m=np.zeros((rows,cols,2),np.uint8)
print(m)
crows,ccols=int(rows/2),int(cols/2)
m[crows-30:crows+30,ccols-30:ccols+30]=1
f=m*ofs
if1=np.fft.fftshift(f)
io=cv2.idft(if1)
io1=cv2.magnitude(io[:,:,0],io[:,:,1])

plt.subplot(221)

plt.imshow(o,cmap="gray")
plt.subplot(223)
plt.imshow(io1,cmap="gray")
r=100


plt.subplot(222)
plt.plot(o[r,:],color="r")


plt.subplot(224)
plt.plot(io1[r,:],color="g")