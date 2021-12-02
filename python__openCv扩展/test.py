# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 08:47:59 2020

@author: Administrator
"""
# import numpy as np
# i=1
# while(i<10):
#     a=np.random.randint(0,10)
#     b=np.random.randint(0,10)
#     c=a/b
#     print(a,b,c)
#     i=i+1

import cv2
import torch
img = cv2.imread(r"D:\Desktop\small_girl.jpg", 0)
# img = torch.from_numpy(img)
# print(img.shape)
# print(torch.mean(img.float(),dim=2).shape)

print(cv2.minMaxLoc(img))