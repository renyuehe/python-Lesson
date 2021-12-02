#-*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:39:10 2020
答疑：李立宗  lilizong@gmail.com
"""

import cv2
import numpy as np
o = cv2.imread('img/lena.jpg')
cv2.imshow("o1",o)
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
contours, hierarchy = cv2.findContours(gray,
                                             cv2.RETR_LIST,
                                             cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(o,contours,-1,(255,255,255),-1)
cv2.imshow("o2" ,o)
cv2.waitKey()
cv2.destroyAllWindows()