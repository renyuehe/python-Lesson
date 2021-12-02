import math

import cv2

def rotateLine(center, point, angle, orientation=0):
    """
    更具锚点,旋转一条直线,并返回非锚点的点
    :param center:锚点（中点）
    :param point:目标点
    :param angle:角度
    :param orientation:0逆时针,1顺时针
    :return:
    """
    cx, cy = center[0], center[1]
    x, y = point[0], point[1]
    if orientation:
        # 为要转的点，（pointx, pointy)为中心点，如果顺时针角度为angle
        dst_x = (x - cx) * math.cos(angle) + (y - cy) * math.sin(angle) + cx
        dst_y = (y - cy) * math.cos(angle) - (x - cx) * math.sin(angle) + cy
    else:
        # 为要转的点，（pointx, pointy)为中心点，如果逆时针角度为angle
        dst_x = (x - cx) * math.cos(angle) - (y - cy) * math.sin(angle) + cx
        dst_y = (x - cx) * math.sin(angle) + (y - cy) * math.cos(angle) + cy

    return (dst_x, dst_y)

def drawRotateRect(img, cx, cy, w, h, angle):
    '''
    绘制一个旋转矩形
    :param img:
    :param cx:
    :param cy:
    :param w:
    :param h:
    :param angle:
    :return:
    '''
    center = (cx, cy)

    leftTop = (cx - w//2, cy - h//2)
    leftButton = (cx - w//2, cy + h//2)
    rightTop = (cx + w//2, cy - h//2)
    rightButton = (cx + w//2, cy + h//2)

    leftTop = rotateLine(center, leftTop, angle)
    leftButton = rotateLine(center, leftButton, angle)
    rightTop = rotateLine(center, rightTop, angle)
    rightButton = rotateLine(center, rightButton, angle)

    toint = lambda pt: (int(pt[0]), int(pt[1]))
    leftTop, leftButton, rightTop, rightButton = toint(leftTop), toint(leftButton), toint(rightTop), toint(rightButton)

    cv2.line(img, leftTop, leftButton, color=(0,0,255), thickness=2)
    cv2.line(img, leftTop, rightTop, color=(0, 0, 255), thickness=2)
    cv2.line(img, leftButton, rightButton, color=(0, 0, 255), thickness=2)
    cv2.line(img, rightTop, rightButton, color=(0, 0, 255), thickness=2)
