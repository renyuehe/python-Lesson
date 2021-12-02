#-*- coding: utf-8 -*-
#coding:utf-8
"""
Created on Mon Jun 22 14:39:10 2020
答疑：李立宗  lilizong@gmail.com
"""

import cv2
cap = cv2.VideoCapture(0)
a=cap.get(4)
print(a)
while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    c = cv2.waitKey(1)
    if c==27:   #ESC键
        break
cap.release()
cv2.destroyAllWindows()
