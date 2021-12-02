#-*- coding: utf-8 -*-
#coding:utf-8
"""
Created on Mon Jun 22 14:39:10 2020
答疑：李立宗  lilizong@gmail.com
"""
import cv2
cap=cv2.VideoCapture("video/viptrain.avi")
while(cap.isOpened()):
    ret,frame=cap.read()
    cv2.imshow("original",frame)
    cy=cv2.Canny(frame,100,200)
    cv2.imshow("canny",cy)
    gr=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",gr)
    flipx=cv2.flip(frame,1)
    cv2.imshow("flipx",flipx)
    
    c=cv2.waitKey(25)
    if c==27:
        break
cap.release()
cv2.destroyAllWindows()