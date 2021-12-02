#-*- coding: utf-8 -*-
#coding:utf-8
"""
Created on Mon Jun 22 14:39:10 2020
答疑：李立宗  lilizong@gmail.com
"""
import cv2
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
out = cv2.VideoWriter('video/output.avi',fourcc, 20, (640,480))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) == 27:
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()