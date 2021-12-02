# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 16:33:15 2014
@author: duan
"""
import cv2
import numpy as np

img_rgb = cv2.imread('img/19.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('img/20.jpg',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(image=img_gray, templ=template, method=cv2.TM_CCOEFF_NORMED) # 返回每个像素点有可能是匹配图像左上角的每个像素的概率
threshold = 0.95 # 相似度,相似度越大,匹配到成功的数量就越精准，也越少
# threshold = 0.35 # 相似度越小,匹配到的成功的数量就越多
loc = np.where( res >= threshold) # loc 是两个数组，第一个数组对应的是 y 轴（h）的坐标， 第二个数组对应的是 x轴（w）的坐标，同一个区域可能会出现多次匹配
print(loc)
# zip(a, b) 用来打包,  zip(*c)用来解压
for pt in zip(*loc[::-1]):
    print(pt)
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,np.random.randint(0,200),np.random.randint(0,255)), 1)

cv2.imshow("res img", img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()