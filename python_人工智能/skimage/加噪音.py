import numpy as np
from skimage import data

img = data.camera()

height,weight = img.shape

#随机生成5000个椒盐噪声
for i in range(5000):
    x = np.random.randint(0,height)
    y = np.random.randint(0,weight)
    img[x ,y] = 255

import cv2
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
