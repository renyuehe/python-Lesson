# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 11:43:28 2020
答疑：李立宗  lilizong@gmail.com
"""


import cv2
#----------------读取并显示原始图像-------------------------------
o = cv2.imread('img/26.jpg')
cv2.imshow("original",o)
#----------------获取轮廓-------------------------------
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
contours, hierarchy = cv2.findContours(gray,
                                             cv2.RETR_LIST,
                                             cv2.CHAIN_APPROX_SIMPLE)
#----------------直接绘制边缘-------------------------------
adp = o.copy()
adp=cv2.drawContours(adp,contours,-1,(0,0,255),2)
cv2.imshow("result",adp)
#----------------epsilon=0.1*周长-------------------------------
adp = o.copy()
epsilon = 0.1*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)
adp=cv2.drawContours(adp,[approx],0,(0,0,255),2)
cv2.imshow("result0.1",adp)
#----------------epsilon=0.09*周长-------------------------------
adp = o.copy()
epsilon = 0.09*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)
adp=cv2.drawContours(adp,[approx],0,(0,0,255),2)
cv2.imshow("result0.09",adp)
#----------------epsilon=0.055*周长-------------------------------
adp = o.copy()
epsilon = 0.055*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)
adp=cv2.drawContours(adp,[approx],0,(0,0,255),2)
cv2.imshow("result0.055",adp)
#----------------epsilon=0.05*周长-------------------------------
adp = o.copy()
epsilon = 0.05*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)
adp=cv2.drawContours(adp,[approx],0,(0,0,255),2)
cv2.imshow("result0.05",adp)
#----------------epsilon=0.02*周长-------------------------------
adp = o.copy()
epsilon = 0.02*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)
adp=cv2.drawContours(adp,[approx],0,(0,0,255),2)
cv2.imshow("result0.02",adp)
#----------------等待释放窗口-------------------------------
cv2.waitKey()
cv2.destroyAllWindows()
