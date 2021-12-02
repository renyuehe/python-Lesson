# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 16:10:33 2014
@author: duan
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

#读取梅西的图片
img = cv2.imread('img/9.jpg',0)
img2 = img.copy()

#读取梅西脸部图片用作匹配
template = cv2.imread('img/18.jpg',0)

# 等价于 h, w = template.shapes
w, h = template.shape[::-1] # 拿到宽高，骚操作

# All the 6 methods for comparison in a list
# TM_SQDIFF：计算平方不同，计算出来的值越小，越相关
# TM_CCORR：计算相关性，计算出来的值越大，越相关
# TM_CCOEFF：计算相关系数，计算出来的值越大，越相关
# TM_SQDIFF_NORMED：计算归一化平方不同，计算出来的值越接近0，越相关
# TM_CCORR_NORMED：计算归一化相关性，计算出来的值越接近1，越相关
# TM_CCOEFF_NORMED：计算归一化相关系数，计算出来的值越接近1，越相关
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
for meth in methods:
    img = img2.copy()

    #eval 语句用来执行储存在字符串或文件中的 Python 语句。
    # 例如，我们可以在运行时生成一个包含 Python 代码的字符串，然后使用 eval 语句执行这些语句。
    #eval 语句用来计算存储在字符串中的有效 Python 表达式

    method = eval(meth) #将一个字符串 变成一个表达式 也可以说是参数
    # Apply template Matching
    res = cv2.matchTemplate(img,template,method) # 模式匹配
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res) # 返回匹配后的值
    print(min_loc, max_loc)

    # 使用不同的比较方法，对结果的解释不同
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img, top_left, bottom_right, 255, 2)

    plt.subplot(121),plt.imshow(res, cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])

    plt.subplot(122),plt.imshow(img, cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])


    plt.suptitle(meth)
    plt.show()
