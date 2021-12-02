import numpy as np
import cv2

img = cv2.imread(r"img/1.jpg")
cv2.imshow("img", img)

# 高斯金字塔
up = cv2.pyrUp(img)
cv2.imshow("gauss up",up)
down = cv2.pyrDown(img)
cv2.imshow("gauss down", down)

# 拉普拉斯金子塔
down=cv2.pyrDown(img)
down_up=cv2.pyrUp(down)
l_1=img-down_up
cv2.imshow("laplacian : src - up(down(src))", l_1)

cv2.waitKey(0)
cv2.destroyAllWindows()