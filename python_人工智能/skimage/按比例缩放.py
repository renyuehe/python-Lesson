

import cv2
import skimage
from skimage import data, transform

img = data.camera()
output_shape = (100,200)

# 按照比例缩放
dst = transform.rescale(img,[1, 0.5])

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

